# LangChain 术语表

阅读章节时如果你总在 `Runnable`、`Retriever`、`Trace` 这些词之间来回跳，这一页就是统一查询入口。建议把它当成“读到陌生词时先回来对齐定义”的速查表，而不是替代章节正文。

## 这页怎么用

- 想知道某个词“解决什么问题”，先看“一句话理解”
- 想知道它在课程哪一章重点出现，直接看“重点章节”
- 想避免把相近概念混在一起，优先看“不要混淆”

## 快速索引

- [Runnable](#runnable)
- [LCEL](#lcel)
- [Retriever](#retriever)
- [Vector Store](#vector-store)
- [Tool Calling](#tool-calling)
- [Agent](#agent)
- [LangGraph State](#langgraph-state)
- [Trace](#trace)
- [Evaluation](#evaluation)

## Runnable

- 一句话理解：`Runnable` 是 LangChain 里可被统一调用、可组合、可串联的执行单元。
- 它解决什么问题：让 Prompt、模型、解析器和自定义步骤能用同一套接口接起来，而不是每个组件各写一套调用方式。
- 在这个项目里：第 2 章会把 `AI 学习助手` 的最小链拆成多个可组合步骤，帮助你理解为什么后续 RAG、Agent、工作流都能沿着同一接口扩展。
- 重点章节：[第 2 章：LangChain 核心抽象](../chapters/chapter-02-langchain-core.md)
- 不要混淆：`Runnable` 是“组件接口”，不是“完整应用架构”。

## LCEL

- 一句话理解：`LCEL` 是 LangChain Expression Language，用来把多个 `Runnable` 用表达式方式串成链。
- 它解决什么问题：把“步骤怎么连接”写得更短、更清楚，减少手写胶水代码。
- 在这个项目里：你会先用 `prompt | model | parser` 这种最小模式理解链路，再把它迁移到后面的结构化输出、RAG 和更复杂流程。
- 重点章节：[第 2 章：LangChain 核心抽象](../chapters/chapter-02-langchain-core.md)
- 不要混淆：`LCEL` 是组织步骤的方式，不负责检索、决策或状态管理。

## Retriever

- 一句话理解：`Retriever` 负责回答“面对一个问题，我应该先找哪些资料片段”。
- 它解决什么问题：把“找相关上下文”和“生成最终回答”分开，避免模型直接凭记忆乱答。
- 在这个项目里：`AI 学习助手` 会先从课程文档里检索相关片段，再把片段交给模型组织答案。
- 重点章节：[第 5 章：RAG 入门](../chapters/chapter-05-rag-basics.md) 、[第 6 章：RAG 进阶优化](../chapters/chapter-06-rag-optimization.md)
- 不要混淆：`Retriever` 负责“找什么”，不是“怎么说”。最终措辞通常还是由生成链负责。

## Vector Store

- 一句话理解：`Vector Store` 是保存文本向量和原始片段的索引层，支持相似度检索。
- 它解决什么问题：让系统能把大批资料先存成可查询结构，再按问题快速召回可能相关的内容。
- 在这个项目里：课程文档先被切分、向量化，再存进 `Vector Store`，后续 `Retriever` 才能从里面挑出候选片段。
- 重点章节：[第 5 章：RAG 入门](../chapters/chapter-05-rag-basics.md)
- 不要混淆：`Vector Store` 是“存和查的底座”，`Retriever` 是“面向问题的检索入口”。

## Tool Calling

- 一句话理解：`Tool Calling` 是模型按约定格式请求外部工具执行动作的能力。
- 它解决什么问题：让模型不只会生成文本，还能显式调用搜索、查询、计算这类外部能力。
- 在这个项目里：学习助手可以查询章节目录、读取章节摘要、生成练习题，而不是只靠内部知识硬答。
- 重点章节：[第 7 章：Tools 与 Agent](../chapters/chapter-07-tools-and-agents.md) 、[第 9 章：评估、观测与调试](../chapters/chapter-09-evaluation-observability-debugging.md)
- 不要混淆：`Tool Calling` 只说明“模型能请求工具”，不自动等于“系统会自主规划多步流程”。

## Agent

- 一句话理解：`Agent` 是让模型根据当前上下文决定是否调用工具、调用哪个工具、以及何时结束的一种运行方式。
- 它解决什么问题：当流程无法预先写死时，用动态决策把多个能力串起来。
- 在这个项目里：学习助手面对“先查大纲，再读章节摘要，最后生成练习题”这类不固定任务时，会比固定链更灵活。
- 重点章节：[第 7 章：Tools 与 Agent](../chapters/chapter-07-tools-and-agents.md)
- 不要混淆：`Agent` 不是默认更高级的链。流程稳定时，固定链通常更便宜、更稳、更好调试。

## LangGraph State

- 一句话理解：`LangGraph State` 是工作流执行过程中共享、会被节点不断读写的状态对象。
- 它解决什么问题：让复杂流程不只依赖当前输入，还能保留路由结果、检索结果、工具结果和中间决策。
- 在这个项目里：学习助手从“会用工具”升级到“会组织工作流”时，需要用状态记录自己现在在哪一步、下一步该去哪里。
- 重点章节：[第 8 章：LangGraph 工作流](../chapters/chapter-08-langgraph-workflows.md)
- 不要混淆：`State` 不是数据库表，也不是聊天记录的全部，它首先是当前工作流的共享上下文。

## Trace

- 一句话理解：`Trace` 是一次请求从输入到输出的关键中间步骤记录。
- 它解决什么问题：帮你定位问题到底出在检索、工具调用、提示词、状态转移，还是最终生成阶段。
- 在这个项目里：你会用 trace 观察检索到了什么、工具有没有被调用、哪一步抛错，而不是只盯着最后回答。
- 重点章节：[第 9 章：评估、观测与调试](../chapters/chapter-09-evaluation-observability-debugging.md)
- 不要混淆：`Trace` 不等于一行日志。它更强调完整链路和步骤间因果关系。

## Evaluation

- 一句话理解：`Evaluation` 是用固定问题集和明确标准判断系统效果是否真的变好。
- 它解决什么问题：避免“我手测几次感觉还行”的错觉，把效果比较变成可记录、可复查的过程。
- 在这个项目里：学习助手会为基础概念题、RAG 问答题、工具调用题建立最小评估集，作为回归基线。
- 重点章节：[第 9 章：评估、观测与调试](../chapters/chapter-09-evaluation-observability-debugging.md)
- 不要混淆：`Evaluation` 关注“质量是否达标”，`Trace` 关注“运行时发生了什么”。

## 怎么把这些词串起来

如果按这套课程的主线去理解，可以把它们串成一条升级路径：

1. 先用 `Runnable` 和 `LCEL` 搭出可组合的最小链。
2. 再引入 `Vector Store` 和 `Retriever`，让系统能基于资料做 RAG。
3. 然后通过 `Tool Calling` 和 `Agent` 让系统获得外部能力与动态决策。
4. 当流程更复杂时，用 `LangGraph State` 把中间状态显式化。
5. 最后用 `Trace` 和 `Evaluation` 判断系统哪里出错、效果有没有真的变好。

如果你正在章节里反复遇到这些词，建议顺着上面的顺序回看，而不是单独死记名词。
