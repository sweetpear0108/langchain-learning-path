# Shared Assets

这里存放共享提示词、数据集、图示和其他跨模块资源。

## Prompts

- `shared/prompts/learning-assistant-system.txt`: `AI 学习助手` 的通用系统提示词
- `shared/prompts/rag-grounded-answer.txt`: 基于检索资料回答问题的模板
- `shared/prompts/query-rewrite.txt`: 把学习者问题改写成检索查询的模板

## Datasets

- `shared/datasets/chapter-05/course_materials.json`: 第 5 章 RAG 入门示例的课程资料
- `shared/datasets/chapter-06/course_materials.json`: 第 6 章 RAG 优化示例的课程资料
- `shared/datasets/learning_assistant_assets.json`: 跨章节共享资产与教学场景清单

把教学数据放在 `shared/datasets`，可以让示例代码聚焦在检索流程本身，也让后续替换数据源或扩展成更真实的知识库结构更直接。

## Diagrams

- `shared/diagrams/rag-baseline-flow.md`: 基础 RAG 流程图
- `shared/diagrams/rag-optimization-loop.md`: RAG 优化回路图

这些共享资产的目标是把“可复用的知识材料”沉淀到统一位置，避免每一章都重复维护一份近似内容。
