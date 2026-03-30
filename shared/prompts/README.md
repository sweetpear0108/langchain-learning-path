# Shared Prompts

这里存放可跨章节复用的提示词模板，优先沉淀那些会在 `Prompt`、`RAG`、`Agent` 和综合实战中反复出现的资产。

## Files

- `learning-assistant-system.txt`: `AI 学习助手` 的通用系统提示词，适合第 4 章以后需要稳定角色边界的示例。
- `rag-grounded-answer.txt`: 基于检索资料回答问题的模板，适合第 5、6 章以及后续带知识库的问答场景。
- `query-rewrite.txt`: 把用户问题改写成更适合检索的搜索请求，适合第 6 章及之后的 RAG 优化实验。

## Usage Notes

- 这些模板先服务教学场景，因此强调边界清晰、输出可解释，而不是追求生产级复杂防护。
- 如果后续示例开始从文件读取 Prompt，可以优先复用这里的模板，而不是在脚本里重复写长字符串。
