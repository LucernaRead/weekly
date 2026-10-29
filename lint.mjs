#!/usr/bin/env node
/**
 * Lucerna Weekly 内容仓的结构校验 **兼索引生成器**。零依赖,`node lint.mjs` 直接跑。
 *
 *     node lint.mjs                校验 + 检查 index.json 是否最新(CI 用,不写盘)
 *     node lint.mjs --write        校验 + 写出 index.json(加完一版就跑这个)
 *     node lint.mjs --require-pdf  额外要求每版的 PDF 实体已在仓内(发布前检查用)
 *
 * 为什么索引由 lint 生成:消费方(站点/社区)运行时从 GitHub 取内容。没有索引,
 * 渲染一个列表要把每版的 md 都拉下来 —— 上游请求数是 O(版本数),而 GitHub
 * 未鉴权 API 只有 60 次/小时/IP。有了索引,列表只取 1 个文件。
 *
 * ⚠️ 索引会**漂移**:改了 md 忘了跑 --write,index 里还是旧数据,而且不报任何错。
 * 所以默认模式会把重新生成的索引和仓里的 index.json 比对,不一致直接红。
 *
 * 这个仓只有一种形态,校验的就是它:
 *
 *     issues/<week>/
 *       <slug>/
 *         <slug>.md     这一版的元数据(frontmatter)+ 一段简介
 *         <slug>.pdf    整期网页版 PDF(可选实体;见 README 的「PDF」一节)
 *         <slug>.text.md 这一版的正文 markdown(可选;见规则 9)
 *
 * <week> 是周次目录(小写,如 2026-w43),它本身就是一层 —— 先按周找,再按版找。
 * slug = <week 小写>-<目标语>-<母语>,如 2026-w43-fr-zh-cn。
 *
 * 另有一种形态 —— 网站封面块,站点靠索引找到它:
 *
 *     covers/<week>/
 *       <week>-cover-<语种>/
 *         <week>-cover-<语种>.html   静态封面块(零交互,见规则 5)
 *         <week>-cover-<语种>.md     印刷版封面的元数据(可选)
 *         cover-<week 短码>-<语种>.pdf 印刷版封面 PDF(可选)
 *
 * 封面块按周 + 语种进索引的 covers 一节,有 .html 的才进索引,站点凭它定位封面。
 *
 * 硬规则:
 *   1. **层级固定两层** —— issues/ 下面只有周次目录,周次目录里只有版本目录,
 *      版本目录里不能再有子目录;版本必须放在它自己所属的周次目录下。
 *   2. **配对合法** —— 目标语 ≠ 母语;语言必须在 12 语种列表内;
 *      简体中文与繁體中文互为目标/母语的两个配对**不存在**(没人这样学外语)。
 *   3. **自包含** —— 版本目录里只许有 <slug>.md、<slug>.pdf 和(可选的)<slug>.text.md;
 *      md 的 frontmatter 声明 pdf 文件名、字节数与 SHA-256,
 *      PDF 实体在仓内时必须与声明逐字节吻合(哈希对不上 = 文件被换过或传坏了)。
 *   4. **文本层** —— 版本目录里的 PDF 必须带可提取文本层(pdftotext 能提出文字);
 *      图片版 PDF 没有文本层,站点 SEO 读不到,不进仓。
 *   5. **封面块零交互** —— 仓内任何 .html 不得含交互元素
 *      (脚本/按钮/链接/表单/导航/页脚/侧栏/点击事件等),只留静态内容;
 *      没有 .html 时此条空过,主线保持绿。
 *   6. **excerpt 目标语** —— 非拉丁书写目标语(ru/ja/ko/zh-cn/zh-tw)的 excerpt 若 ASCII 字母占比过高(>50%),视为英文 excerpt 错放,校验失败;拉丁书写目标语无法用书写区分,故不查。
 *   7. **封面块进索引** —— covers/ 下每语种目录至多一个 .html,语种须在 12 语种列表内;
 *      有 .html 的才进索引(只有印刷版 md/pdf、没有 .html 的目录不进索引);
 *      索引的 covers 一节按周倒序、语种按 LANGS 序排列,站点凭它找到每期每语种的封面。
 *      每条带 slug(封面目录名)和 html 的字节数、SHA-256(从文件实算),站点镜像时据此验真。
 *   8. **封面块标出每篇报道的学习语言** —— <body> 上写 data-story-langs="<语种> <语种> …",
 *      按文档顺序依次对应每个 <article>:12 个语种各出现一次,<article> 恰好 12 个。
 *      站点凭它把每篇报道变成「学这种语言、用本封面读者语言讲解」那一版的入口(封面块本身仍零交互)。
 *   9. **正文 md(可选)** —— 版本目录里可以多放一份 <slug>.text.md:这一版的正文,markdown。
 *      不许是空文件。有就进索引的 text 字段(路径、字节数、SHA-256,从文件实算),没有时 text 为 null。
 *      站点把它渲染成单期页的正文;没有时站点只能用 PDF 抽出的文字。
 */
import { readdirSync, readFileSync, writeFileSync, existsSync, statSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { join } from 'node:path';
import { createHash } from 'node:crypto';

/** 12 个语种(目标语与母语共用同一套代码)。顺序即索引内的排序。 */
const LANGS = ['en', 'de', 'fr', 'es', 'it', 'pt', 'nl', 'ru', 'ja', 'ko', 'zh-cn', 'zh-tw'];
const ROOT_ALLOW = new Set([
  'issues', 'lint.mjs', 'index.json', 'README.md', 'AGENTS.md', 'CLAUDE.md',
  '.git', '.husky', 'package.json', 'package-lock.json', 'node_modules',
  '.github', '.gitignore', 'covers',
]);
const REQUIRED_FM = [
  'title', 'excerpt', 'abstract', 'publishedAt', 'week', 'weekStart', 'weekEnd', 'vol',
  'masthead', 'target', 'targetName', 'targetLabel', 'native', 'nativeName',
  'nativeLabel', 'exercises', 'pages', 'pdf', 'pdfBytes', 'pdfSha256',
  'discordThread', 'draft',
];
const SLUG_RE = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;
const WEEK_RE = /^\d{4}-w\d{2}$/;
const DATE_RE = /^\d{4}-\d{2}-\d{2}$/;
const SHA_RE = /^[0-9a-f]{64}$/;
const INDEX_FILE = 'index.json';

/** 非拉丁书写目标语:excerpt 可用书写判定语言。 */
const NON_LATIN_TARGETS = new Set(['ru', 'ja', 'ko', 'zh-cn', 'zh-tw']);
/** excerpt 中 ASCII 字母占全部字母的比例(数字与标点不计)。 */
function asciiLetterFraction(s) {
  const letters = [...s].filter((c) => /\p{L}/u.test(c));
  if (!letters.length) return 0;
  const ascii = letters.filter((c) => c.charCodeAt(0) < 128).length;
  return ascii / letters.length;
}

const write = process.argv.includes('--write');
const requirePdf = process.argv.includes('--require-pdf');

const problems = [];
const fail = (where, msg) => problems.push(`${where}: ${msg}`);

/** frontmatter 极简解析:只认 `key: value`(值可带引号),够校验与生成索引用。 */
function frontmatter(raw, where) {
  if (!raw.startsWith('---\n')) {
    fail(where, '缺少 frontmatter(文件必须以 --- 开头)');
    return null;
  }
  const end = raw.indexOf('\n---', 4);
  if (end === -1) {
    fail(where, 'frontmatter 没有闭合的 ---');
    return null;
  }
  const out = {};
  for (const line of raw.slice(4, end).split('\n')) {
    const m = line.match(/^([A-Za-z][A-Za-z0-9]*):\s*(.*)$/);
    if (!m) continue;
    let v = m[2].trim();
    if (v.startsWith('"') && v.endsWith('"')) v = v.slice(1, -1);
    out[m[1]] = v;
  }
  return out;
}

const root = process.cwd();

// 根目录白名单
for (const name of readdirSync(root)) {
  if (!ROOT_ALLOW.has(name)) fail('根目录', `不允许的条目 ${name}`);
}

// 封面块零交互:仓内任何 .html 不得含交互元素,只留静态内容。
// <a\b 不命中 <article>/<aside>;<link> 不是 <a>;不禁 <header>,不查 cursor/:hover。
// 没有 .html 时空过。默认模式即 enforce,CI 与提交钩子都跑 plain lint。
const INTERACTIVE_PATTERNS = [
  [/<script\b/i, '<script>'],
  [/<button\b/i, '<button>'],
  [/<a\b/i, '<a>'],
  [/<form\b/i, '<form>'],
  [/<input\b/i, '<input>'],
  [/<select\b/i, '<select>'],
  [/<textarea\b/i, '<textarea>'],
  [/<nav\b/i, '<nav>'],
  [/<footer\b/i, '<footer>'],
  [/<aside\b/i, '<aside>'],
  [/onclick\b/i, 'onclick'],
  [/addEventListener/i, 'addEventListener'],
  [/tabindex\s*=/i, 'tabindex'],
  [/role\s*=\s*["']button["']/i, 'role="button"'],
];
const SKIP_DIRS = new Set(['.git', 'node_modules']);
function scanHtml(dir, rel) {
  for (const name of readdirSync(dir).sort()) {
    const p = join(dir, name);
    const r = rel ? `${rel}/${name}` : name;
    if (statSync(p).isDirectory()) {
      if (!SKIP_DIRS.has(name)) scanHtml(p, r);
      continue;
    }
    if (!name.toLowerCase().endsWith('.html')) continue;
    let text;
    try {
      text = readFileSync(p, 'utf8');
    } catch {
      fail(r, '封面 HTML 读取失败');
      continue;
    }
    for (const [re, label] of INTERACTIVE_PATTERNS) {
      if (re.test(text)) {
        fail(r, `封面块不得含有交互元素（脚本/按钮/链接/表单/导航/页脚/侧栏/点击事件等），只留静态内容（命中 ${label}）`);
        break;
      }
    }
  }
}
scanHtml(root, '');

const issuesDir = join(root, 'issues');
if (!existsSync(issuesDir)) {
  fail('issues/', '目录不存在');
  report();
}

const editions = [];
const seenPairs = new Set();

for (const weekDirName of readdirSync(issuesDir).sort()) {
  const weekPath = join(issuesDir, weekDirName);
  if (!statSync(weekPath).isDirectory()) {
    fail(`issues/${weekDirName}`, 'issues/ 下只许放周次目录');
    continue;
  }
  if (!WEEK_RE.test(weekDirName)) {
    fail(`issues/${weekDirName}`, '周次目录名必须是 YYYY-wNN 小写(如 2026-w43)');
  }

  for (const slug of readdirSync(weekPath).sort()) {
    const dir = join(weekPath, slug);
    const rel = `issues/${weekDirName}/${slug}`;
    if (!statSync(dir).isDirectory()) {
      fail(rel, '周次目录里只许放版本目录');
      continue;
    }
    if (!SLUG_RE.test(slug)) fail(rel, 'slug 只能用小写字母、数字与连字符');
    if (!slug.startsWith(`${weekDirName}-`)) {
      fail(rel, `版本必须放在它所属的周次目录下(slug 应以 ${weekDirName}- 开头)`);
    }

    const files = readdirSync(dir);
    for (const f of files) {
      const p = join(dir, f);
      if (statSync(p).isDirectory()) fail(`${rel}/${f}`, '版本目录里不能再有子目录');
    }
    const mdName = `${slug}.md`;
    const pdfName = `${slug}.pdf`;
    const textName = `${slug}.text.md`;
    for (const f of files) {
      if (f !== mdName && f !== pdfName && f !== textName) {
        fail(rel, `多余的文件 ${f}(只许 ${mdName}、${pdfName} 与 ${textName})`);
      }
    }
    if (!files.includes(mdName)) {
      fail(rel, `缺少 ${mdName}`);
      continue;
    }

    const where = `${rel}/${mdName}`;
    const fm = frontmatter(readFileSync(join(dir, mdName), 'utf8'), where);
    if (!fm) continue;

    for (const key of REQUIRED_FM) {
      if (!(key in fm) || fm[key] === '') fail(where, `frontmatter 缺少 ${key}`);
    }
    if (problems.length && fm.target === undefined) continue;

    // 配对规则
    const { target, native: nat } = fm;
    if (!LANGS.includes(target)) fail(where, `未知目标语 ${target}`);
    if (!LANGS.includes(nat)) fail(where, `未知母语 ${nat}`);
    if (target === nat) fail(where, '目标语与母语不能相同');
    if ((target === 'zh-cn' && nat === 'zh-tw') || (target === 'zh-tw' && nat === 'zh-cn')) {
      fail(where, '简繁互译配对不存在(简体与繁體是同一语言的两种书写,没人这样学)');
    }
    const pair = `${fm.week}|${target}|${nat}`;
    if (seenPairs.has(pair)) fail(where, `配对重复:${pair}`);
    seenPairs.add(pair);

    // slug 必须由 week + 配对推出,保证目录名永远可解析
    const expectSlug = `${String(fm.week).toLowerCase()}-${target}-${nat}`;
    if (slug !== expectSlug) fail(where, `slug 应为 ${expectSlug},实际 ${slug}`);

    // 字段格式
    for (const d of ['publishedAt', 'weekStart', 'weekEnd']) {
      if (fm[d] && !DATE_RE.test(fm[d])) fail(where, `${d} 必须是 YYYY-MM-DD`);
    }
    for (const n of ['vol', 'exercises', 'pages', 'pdfBytes']) {
      if (fm[n] !== undefined && !/^\d+$/.test(fm[n])) fail(where, `${n} 必须是整数`);
    }
    if (fm.pdfSha256 && !SHA_RE.test(fm.pdfSha256)) fail(where, 'pdfSha256 必须是 64 位小写十六进制');
    if (fm.pdf && fm.pdf !== pdfName) fail(where, `pdf 字段必须是 ${pdfName}`);

    // excerpt 语言门(保守版):只对非拉丁书写目标语查 ASCII 字母占比。
    // 拉丁书写目标语(de/fr/es/it/pt/nl/en)的 excerpt 本就是拉丁字母,无法用书写区分英文,故不查。
    if (NON_LATIN_TARGETS.has(target) && fm.excerpt && asciiLetterFraction(fm.excerpt) > 0.5) {
      fail(where, `excerpt 必须用目标语 ${target} 写(当前 ASCII 字母占比过高,疑似英文 excerpt)`);
    }

    // PDF 实体在仓内时,逐字节核对(大小 + SHA-256)
    const pdfPath = join(dir, pdfName);
    const pdfInRepo = existsSync(pdfPath);
    if (pdfInRepo) {
      const data = readFileSync(pdfPath);
      if (data.length !== Number(fm.pdfBytes)) {
        fail(where, `PDF 大小不符:声明 ${fm.pdfBytes},实际 ${data.length}`);
      }
      const sha = createHash('sha256').update(data).digest('hex');
      if (sha !== fm.pdfSha256) fail(where, 'PDF 的 SHA-256 与 frontmatter 声明不符');
      // 文本层:pdftotext 能提出文字才算有文本层;图片版 PDF 只有图片,没有文字。
      // pdftotext 是 poppler 的工具(ubuntu-latest runner 自带);本地没有时报错明示,不静默放行。
      try {
        const text = execFileSync('pdftotext', [pdfPath, '-'], { encoding: 'utf8', maxBuffer: 64 * 1024 * 1024 });
        if (text.replace(/\s/g, '').length === 0) {
          fail(where, 'PDF 没有可提取文本层(图片版 PDF 不进仓,先用 webpdf.py 生成带文本层的网页版)');
        }
      } catch (e) {
        if (e.code === 'ENOENT') fail(where, 'PDF 文本层校验需要 pdftotext(安装 poppler-utils 后再跑)');
        else fail(where, `PDF 文本层校验失败:${e.message}`);
      }
    } else if (requirePdf) {
      fail(rel, 'PDF 实体不在仓内(--require-pdf)');
    }

    // 正文 md(规则 9,可选):有就进索引,带字节数与 SHA-256(从文件实算),站点渲染成单期页的正文。
    let text = null;
    if (files.includes(textName)) {
      const data = readFileSync(join(dir, textName));
      if (data.toString('utf8').trim().length === 0) fail(`${rel}/${textName}`, '正文 md 是空的');
      text = {
        path: `${rel}/${textName}`,
        bytes: data.length,
        sha256: createHash('sha256').update(data).digest('hex'),
      };
    }

    editions.push({
      slug,
      title: fm.title,
      excerpt: fm.excerpt,
      abstract: fm.abstract,
      publishedAt: fm.publishedAt,
      week: fm.week,
      weekStart: fm.weekStart,
      weekEnd: fm.weekEnd,
      vol: Number(fm.vol),
      masthead: fm.masthead,
      target,
      targetName: fm.targetName,
      targetLabel: fm.targetLabel,
      native: nat,
      nativeName: fm.nativeName,
      nativeLabel: fm.nativeLabel,
      exercises: Number(fm.exercises),
      pages: Number(fm.pages),
      dir: rel,
      md: `${rel}/${mdName}`,
      pdf: `${rel}/${pdfName}`,
      pdfBytes: Number(fm.pdfBytes),
      pdfSha256: fm.pdfSha256,
      pdfInRepo,
      text,
      discordThread: fm.discordThread,
      draft: fm.draft === 'true',
    });
  }
}

// 封面块进索引:站点凭 covers 一节找到每期每语种的封面块(规则 7)。
// 目录形态 covers/<week>/<week>-cover-<语种>/,每语种目录至多一个 .html;
// 只有印刷版、没有 .html 的目录不进索引(也不报错)。
const covers = [];
const coversDir = join(root, 'covers');
if (existsSync(coversDir)) {
  for (const weekDirName of readdirSync(coversDir).sort()) {
    const weekPath = join(coversDir, weekDirName);
    if (!statSync(weekPath).isDirectory()) {
      fail(`covers/${weekDirName}`, 'covers/ 下只许放周次目录');
      continue;
    }
    if (!WEEK_RE.test(weekDirName)) {
      fail(`covers/${weekDirName}`, '周次目录名必须是 YYYY-wNN 小写(如 2026-w45)');
      continue;
    }
    for (const coverDirName of readdirSync(weekPath).sort()) {
      const dir = join(weekPath, coverDirName);
      const rel = `covers/${weekDirName}/${coverDirName}`;
      if (!statSync(dir).isDirectory()) {
        fail(rel, '周次目录里只许放封面目录');
        continue;
      }
      const m = coverDirName.match(new RegExp(`^${weekDirName}-cover-(.+)$`));
      if (!m) {
        fail(rel, `封面目录名应为 ${weekDirName}-cover-<语种>`);
        continue;
      }
      const lang = m[1];
      if (!LANGS.includes(lang)) {
        fail(rel, `未知语种 ${lang}`);
        continue;
      }
      const files = readdirSync(dir);
      const htmls = files.filter((f) => f.toLowerCase().endsWith('.html'));
      if (htmls.length === 0) continue; // 只有印刷版的封面目录:不进索引,也不报错
      if (htmls.length > 1) {
        fail(rel, `封面目录里至多一个 .html,实际 ${htmls.length} 个`);
        continue;
      }
      const pdfs = files.filter((f) => f.toLowerCase().endsWith('.pdf'));
      if (pdfs.length > 1) {
        fail(rel, `封面目录里至多一个 PDF,实际 ${pdfs.length} 个`);
        continue;
      }
      const mdName = `${coverDirName}.md`;
      const htmlRel = `${rel}/${htmls[0]}`;
      const htmlData = readFileSync(join(dir, htmls[0]));
      checkStoryLangs(htmlData.toString('utf8'), htmlRel);
      covers.push({
        slug: coverDirName,
        week: weekDirName,
        lang,
        dir: rel,
        html: htmlRel,
        htmlBytes: htmlData.length,
        htmlSha256: createHash('sha256').update(htmlData).digest('hex'),
        md: files.includes(mdName) ? `${rel}/${mdName}` : null,
        pdf: pdfs.length === 1 ? `${rel}/${pdfs[0]}` : null,
      });
    }
  }
}
/** 规则 8:<body data-story-langs> 列出 12 个语种各一次,且与 <article> 一一对应(按文档顺序)。 */
function checkStoryLangs(text, where) {
  const m = text.match(/<body\b[^>]*\sdata-story-langs\s*=\s*"([^"]*)"/i);
  if (!m) {
    fail(where, '封面块 <body> 缺少 data-story-langs(按顺序列出每篇 <article> 的学习语言,见 AGENTS.md「加封面」)');
    return;
  }
  const langs = m[1].trim().split(/\s+/).filter(Boolean);
  const unknown = langs.filter((l) => !LANGS.includes(l));
  if (unknown.length) fail(where, `data-story-langs 里有未知语种 ${unknown.join(' ')}`);
  const missing = LANGS.filter((l) => !langs.includes(l));
  if (missing.length) fail(where, `data-story-langs 缺少语种 ${missing.join(' ')}`);
  if (new Set(langs).size !== langs.length) fail(where, 'data-story-langs 里有重复语种');
  const articles = (text.match(/<article\b/gi) ?? []).length;
  if (articles !== langs.length) {
    fail(where, `data-story-langs 列了 ${langs.length} 个语种,但封面块里有 ${articles} 个 <article>,两者必须一一对应`);
  }
}

covers.sort((a, b) =>
  b.week.localeCompare(a.week) ||
  LANGS.indexOf(a.lang) - LANGS.indexOf(b.lang));

// 排序:期(weekStart)倒序 → 目标语按 LANGS 序 → 母语按 LANGS 序。不留给消费方算。
editions.sort((a, b) =>
  b.weekStart.localeCompare(a.weekStart) ||
  LANGS.indexOf(a.target) - LANGS.indexOf(b.target) ||
  LANGS.indexOf(a.native) - LANGS.indexOf(b.native));

const index = {
  about: 'Lucerna Weekly edition + cover index. Generated by lint.mjs — do not edit by hand.',
  count: editions.length,
  editions,
  coverCount: covers.length,
  covers,
};
const rendered = JSON.stringify(index, null, 2) + '\n';

if (problems.length) report();

if (write) {
  writeFileSync(join(root, INDEX_FILE), rendered);
  console.log(`index.json 已写出:${editions.length} 版`);
} else {
  const current = existsSync(join(root, INDEX_FILE))
    ? readFileSync(join(root, INDEX_FILE), 'utf8')
    : '';
  if (current !== rendered) {
    console.error('index.json 与内容不一致(漂移)—— 跑 `node lint.mjs --write` 重新生成并提交。');
    process.exit(1);
  }
  console.log(`OK:${editions.length} 版,index.json 最新`);
}

function report() {
  if (problems.length) {
    console.error(`校验失败,${problems.length} 个问题:`);
    for (const p of problems) console.error(`  - ${p}`);
    process.exit(1);
  }
}
