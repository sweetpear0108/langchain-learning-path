# LangChain Learning Path

这是一个面向中文开发者的 LangChain 章节化学习项目。

仓库以一个持续演进的主项目 `AI 学习助手` 为主线，把 LangChain 的核心能力拆成循序渐进的章节内容，而不是把概念、API 和示例零散堆放。

## 项目定位

这个项目同时承担三件事：

- 提供一条面向中文开发者的 LangChain 学习路径
- 用章节化内容解释从基础抽象到工程实践的过渡
- 通过同一个主项目把 Prompt、Chain、RAG、Agent、LangGraph 等主题串起来

当前重点不是提供在线产品，而是先把教程结构、内容框架和教学示例稳定下来。

## 当前发布基线

当前仓库冻结为第一个可发布的 `Phase 1` 基线。

- 当前阶段：`Phase 1 / 静态教学站`
- 当前目标：先把学习路径、章节内容和示例代码稳定下来
- 当前状态：适合公开展示学习路线和仓库结构，还不包含在线运行的 LangChain 实验能力

### 这个基线已经包含什么

- `VitePress` 文档站骨架
- 首页、路线图、章节目录和项目页入口
- `chapter-01` 到 `chapter-10` 的章节文档草稿
- 每章对应的最小示例目录与 `main.py`

### 这个基线还不包含什么

- `Phase 2` 外部后端还只有最小 `FastAPI` 骨架，当前只是占位成果
- 在线 playground、真实 API 调用和交互式实验页暂未提供
- `backend/` 目录现在提供 `GET /health` 和 `GET /demo` 两个占位接口，用来明确未来接入方向，不代表后端能力已经完成
- RAG、Tools、Agent、LangGraph 的在线演示仍以文档与本地示例为主

项目目标不是堆概念，而是沿着一个持续演进的主项目 `AI 学习助手`，把以下能力连成一条主线：

- LangChain 基础抽象
- Prompt 工程
- 链式应用
- RAG 与优化
- Tools / Agent
- LangGraph 工作流
- 评估、观测、调试与公开部署

## 学习路径

本项目按以下章节顺序展开：

- 第 1 章：LLM 应用基础
- 第 2 章：LangChain 核心抽象
- 第 3 章：第一个链式应用
- 第 4 章：Prompt 工程与输出控制
- 第 5 章：RAG 入门
- 第 6 章：RAG 进阶优化
- 第 7 章：Tools 与 Agent
- 第 8 章：LangGraph 工作流
- 第 9 章：评估、观测与调试
- 第 10 章：综合实战与公开部署

## 当前边界

`Phase 2` 尚未开始。仓库当前仍以文档、图示和本地示例为主，后续才会补：

- 真正可承载实验的外部 `FastAPI` / LangChain 运行时
- 站内交互式实验页面
- 更真实的线上演示、调试与观测链路

为了让边界更清楚，仓库已经补了一个最小后端占位成果：

- `backend/app/main.py` 提供可启动的 `FastAPI` 骨架
- `GET /health` 用于确认服务存活
- `GET /demo` 用于说明未来 Phase 2 会往这里继续扩展

当前可以将 `backend/` 理解为“已建立接口入口，但尚未承诺真实实验能力”。

## 文档入口

- [文档首页](./docs/index.md)
- [学习路线图](./docs/guide/roadmap.md)
- [学习计划](./docs/guide/study-plan.md)
- [完整设计方案](./docs/DESIGN.md)
- [完整课程大纲](./docs/COURSE_OUTLINE.md)
- [章节目录](./docs/chapters/index.md)
- [术语表](./docs/faq/glossary.md)
- [常见问题排查](./docs/faq/troubleshooting.md)

## 仓库结构

- `docs/`：VitePress 文档站内容
- `examples/`：每章最小可运行代码
- `backend/`：第二阶段在线实验后端
- `shared/`：共享提示词、数据集和图示
- `.github/workflows/`：自动化工作流
