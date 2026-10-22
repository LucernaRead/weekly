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
 *
 * <week> 是周次目录(小写,如 2026-w43),它本身就是一层 —— 先按周找,再按版找。
 * slug = <week 小写>-<目标语>-<母语>,如 2026-w43-fr-zh-cn。
 *
 * 硬规则:
 *   1. **层级固定两层** —— issues/ 下面只有周次目录,周次目录里只有版本目录,
 *      版本目录里不能再有子目录;版本必须放在它自己所属的周次目录下。
 *   2. **配对合法** —— 目标语 ≠ 母语;语言必须在 12 语种列表内;
 *      简体中文与繁體中文互为目标/母语的两个配对**不存在**(没人这样学外语)。
 *   3. **自包含** —— 版本目录里只许有 <slug>.md 和 <slug>.pdf;
 *      md 的 frontmatter 声明 pdf 文件名、字节数与 SHA-256,
 *      PDF 实体在仓内时必须与声明逐字节吻合(哈希对不上 = 文件被换过或传坏了)。
 */
import { readdirSync, readFileSync, writeFileSync, existsSync, statSync } from 'node:fs';
import { join } from 'node:path';
import { createHash } from 'node:crypto';

/** 12 个语种(目标语与母语共用同一套代码)。顺序即索引内的排序。 */
const LANGS = ['en', 'de', 'fr', 'es', 'it', 'pt', 'nl', 'ru', 'ja', 'ko', 'zh-cn', 'zh-tw'];
const ROOT_ALLOW = new Set([
  'issues', 'lint.mjs', 'index.json', 'README.md', 'AGENTS.md', 'CLAUDE.md',
  '.git', '.husky', 'package.json', 'package-lock.json', 'node_modules',
  '.github', '.gitignore',
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
    for (const f of files) {
      if (f !== mdName && f !== pdfName) fail(rel, `多余的文件 ${f}(只许 ${mdName} 与 ${pdfName})`);
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
    } else if (requirePdf) {
      fail(rel, 'PDF 实体不在仓内(--require-pdf)');
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
      discordThread: fm.discordThread,
      draft: fm.draft === 'true',
    });
  }
}

// 排序:期(weekStart)倒序 → 目标语按 LANGS 序 → 母语按 LANGS 序。不留给消费方算。
editions.sort((a, b) =>
  b.weekStart.localeCompare(a.weekStart) ||
  LANGS.indexOf(a.target) - LANGS.indexOf(b.target) ||
  LANGS.indexOf(a.native) - LANGS.indexOf(b.native));

const index = {
  about: 'Lucerna Weekly edition index. Generated by lint.mjs — do not edit by hand.',
  count: editions.length,
  editions,
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
