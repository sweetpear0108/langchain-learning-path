# LangChain Learning Path

这是一个面向中文开发者的 LangChain 章节化学习项目。

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
