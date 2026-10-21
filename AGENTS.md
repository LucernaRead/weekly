# 周报内容 Agent 指南

## 开始前

- 先读 README.md。本仓只维护内容(周报各版本的元数据与 PDF),不放站点代码。
- 一版能不能进仓,只看一条:它在生产端已经走完周报 SOP —— 独立校对
  完整一轮零问题、几何遮挡审计零标记。没过门的版不要往这里放。

## 加一版

1. 建目录 `issues/<week 小写>/<week 小写>-<目标语>-<母语>/`(如 `issues/2026-w43/2026-w43-fr-zh-cn/`)—— 周次本身是一层。
2. 写 `<slug>.md`:frontmatter 字段照 README,一个不能少。
   pdfBytes 与 pdfSha256 从**最终定稿**的网页版 PDF 实测(SHA-256 全小写)。
3. 有 PDF 实体要一并提交时,文件名必须是 `<slug>.pdf`,放进同一目录。
4. 跑 `node lint.mjs --write`,再跑 `node lint.mjs` 确认绿;把生成的
   index.json 和 md 一起提交。**不要手工编辑 index.json。**
5. 提交钩子会重算索引,不得跳过。提交前看 git diff,别混入无关文件。

## 不许做的事

- 不许改已入仓版本的 frontmatter 来「修正」历史 —— 版有错,走生产端的
  更正流程出新文件,再更新 md 的 pdfBytes/pdfSha256 并注明。
- 不许出现简繁互译的配对目录(zh-cn × zh-tw):lint 会拦,也不要试图绕过。
- 不许把印刷版 PDF 放进仓里。
