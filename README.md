# weekly

Lucerna 周报(Lucerna Weekly)的内容仓。**只放内容,不放代码** —— 每一期周报的
每个版本(edition)在这里归档,站点与社区工具在运行时从这里读 `index.json`
和各版本的元数据。

## 一个版本 = 一个目录

周报的一版 = **目标语正文 × 读者母语讲解**的一个配对。12 个目标语 × 11 个
母语 ≈ 130 版/周(简繁两个跨书写配对不存在)。目录名就是这一版的标识:

```
issues/2026-w43-fr-zh-cn/
  2026-w43-fr-zh-cn.md    ← 元数据(frontmatter)+ 简介
  2026-w43-fr-zh-cn.pdf   ← 整期网页版 PDF(可选实体,见下)
```

slug 规则:`<week 小写>-<目标语>-<母语>`,语言代码:
`en` `de` `fr` `es` `it` `pt` `nl` `ru` `ja` `ko` `zh-cn` `zh-tw`。

md 开头是 frontmatter(title、excerpt、publishedAt、week、weekStart/weekEnd、
vol、masthead、target/targetName/targetLabel、native/nativeName/nativeLabel、
exercises、pages、pdf、pdfBytes、pdfSha256、discordThread、draft),
字段齐全性由 lint 硬拦。

## 三条硬规则

`node lint.mjs` 会挡住,CI 也会:

1. **只有一层目录** —— 版本目录里不能再有子目录;目录里只许有
   `<slug>.md` 与 `<slug>.pdf` 两个文件。
2. **配对合法** —— 目标语 ≠ 母语,语言必须在 12 语种列表内;
   简体中文与繁體中文互为目标/母语的配对不存在。
3. **PDF 与声明逐字节吻合** —— frontmatter 里钉死了 PDF 的字节数与
   SHA-256;PDF 实体在仓内时,大小或哈希对不上就拦下。

## PDF

PDF 是二进制文件。本仓的索引在 md 入仓时就生成,pdfBytes 与 pdfSha256
已经钉进 frontmatter 与 index.json —— 所以**任何来源的 PDF 副本都能对着
索引验真**。PDF 实体通过普通 git 推送进对应目录(文件名必须是
`<slug>.pdf`);推送后跑一次 `node lint.mjs --require-pdf` 可确认全部
实体到齐且完好。印刷版 PDF 不进本仓(体积过大),只归档网页版。

## 索引

`index.json` 是消费方渲染列表要读的那一个文件 —— 有它,列表只取 1 次
上游请求;没它就得把每版的 md 都拉下来(而 GitHub 未鉴权 API 是
60 次/小时/IP)。排序在 lint 里定死(期倒序 → 目标语 → 母语),不留给
消费方算。

```bash
node lint.mjs            # 零依赖,不用 npm install。校验 + 检查 index.json 是否最新
node lint.mjs --write    # 校验 + 写出 index.json(加完一版必须跑这个)
node lint.mjs --require-pdf   # 额外要求每版 PDF 实体都在仓内且哈希吻合
```

改完 md 忘了跑 `--write`,默认模式会比对出来并报错。

## 分支

`main` 是唯一的长期分支(本仓新建时即如此;与 blog_content 的
dev/master 双分支不同,那是那个仓的历史形态)。
