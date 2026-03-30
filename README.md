# LangChain Learning Path

这是一个面向中文开发者的 LangChain 章节化学习项目。

## 当前发布基线

当前仓库冻结为第一个可发布的 `Phase 1` 基线。

- 当前阶段：`Phase 1 / 静态教学站`
- 当前目标：先把学习路径、章节内容、示例代码和 GitHub Pages 发布链路稳定下来
- 当前状态：适合公开展示学习路线和仓库结构，还不包含在线运行的 LangChain 实验能力

### 这个基线已经包含什么

- `VitePress` 文档站骨架
- 首页、路线图、章节目录和项目页入口
- `chapter-01` 到 `chapter-10` 的章节文档草稿
- 每章对应的最小示例目录与 `main.py`
- GitHub Pages 部署工作流：`.github/workflows/deploy-pages.yml`

### 这个基线还不包含什么

- `Phase 2` 外部后端能力还没有开始交付
- 在线 playground、真实 API 调用和交互式实验页暂未提供
- `backend/` 目录当前只用于预留结构，不代表后端已经完成
- RAG、Tools、Agent、LangGraph 的在线演示仍以文档与本地示例为主

项目目标不是堆概念，而是沿着一个持续演进的主项目 `AI 学习助手`，把以下能力连成一条主线：

- LangChain 基础抽象
- Prompt 工程
- 链式应用
- RAG 与优化
- Tools / Agent
- LangGraph 工作流
- 评估、观测、调试与公开部署

## 本地启动文档站

```bash
npm install
npm run docs:dev
```

## 构建静态站

```bash
npm run docs:build
```

## 启用 GitHub Pages

仓库已经包含基于 GitHub Actions 的 Pages 部署工作流。

1. 进入仓库 `Settings -> Pages`
2. 在 `Build and deployment` 中选择 `GitHub Actions`
3. 确认默认分支为 `main`
4. 推送到 `main`，或在 Actions 页面手动触发 `Deploy VitePress Site`

工作流会执行 `npm install` 和 `npm run docs:build`，然后把 `docs/.vitepress/dist` 发布到 GitHub Pages。

## 当前阶段说明

本仓库现在只承诺 `Phase 1` 范围：

- 重点是章节化教学内容、主项目演进路线和本地可运行示例
- 目标是让新读者先看懂“学什么、按什么顺序学、每章会得到什么”

`Phase 2` 尚未开始，后续才会补：

- 外部 `FastAPI` / LangChain 运行时
- 站内交互式实验页面
- 更真实的线上演示、调试与观测链路

## 文档入口

- [文档首页](./docs/index.md)
- [完整设计方案](./docs/DESIGN.md)
- [完整课程大纲](./docs/COURSE_OUTLINE.md)
- [章节目录](./docs/chapters/README.md)

## 仓库结构

- `docs/`：VitePress 文档站内容
- `examples/`：每章最小可运行代码
- `backend/`：第二阶段在线实验后端
- `shared/`：共享提示词、数据集和图示
- `.github/workflows/`：自动化和 GitHub Pages 部署
