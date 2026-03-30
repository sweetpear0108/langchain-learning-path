# TODO - LangChain Learning Path

这份清单基于当前仓库状态整理，目标不是继续“加内容”，而是优先补齐 **新手体验、稳定性、工程完整度** 三块短板。

建议按优先级推进：**P0 → P1 → P2**。

---

## P0 - 必做项（先把项目变得稳定、可学、可维护）

### 1. 明确版本基线
- [ ] 在根目录 README 增加“推荐环境”小节
- [ ] 明确推荐 Python 版本（建议 3.11）
- [ ] 明确推荐 Node 版本（建议 20 LTS）
- [ ] 明确教程适配的 `langchain-core` / `langchain-text-splitters` 版本范围
- [ ] 在文档中说明：LangChain API 变化较快，教程以仓库锁定版本为准

**完成标准**
- 新用户在首页或快速开始页能直接看到环境要求
- 每个依赖的大版本边界都写清楚

---

### 2. 统一 Python 依赖管理
- [ ] 在仓库根目录新增 `pyproject.toml` 或根级 `requirements.txt`
- [ ] 给示例代码定义“公共基础依赖”
- [ ] 章节目录的 `requirements.txt` 保留为最小依赖说明，避免完全分裂管理
- [ ] 评估是否需要 `requirements-dev.txt`（lint / test / docs 校验）

**完成标准**
- 新用户不需要逐章猜依赖
- 维护者能统一升级/回退版本

---

### 3. 补 CI / 自动检查
- [ ] 新增 GitHub Actions：示例代码 smoke test
- [ ] 至少验证 `examples/chapter-01`
- [ ] 至少验证 `examples/chapter-02`
- [ ] 至少验证 `examples/chapter-09`
- [ ] 至少验证 `examples/chapter-10`
- [ ] 增加文档站构建检查（PR 级别）
- [ ] 可选：增加 Markdown 链接检查

**完成标准**
- PR 合并前能发现明显跑不通的问题
- 文档改动不会悄悄把站点搞坏

---

### 4. 补“真正的新手快速开始”
- [ ] 新增 `docs/guide/setup.md`
- [ ] 写清 Python 虚拟环境创建方式
- [ ] 写清 Node 依赖安装方式
- [ ] 写清如何运行单章示例
- [ ] 写清如何运行文档站
- [ ] 给出第一次学习的推荐顺序

**完成标准**
- 一个第一次接触仓库的人，30 分钟内能把 docs 和至少一个 example 跑起来

---

### 5. 补故障排查页
- [ ] 新增 `docs/faq/troubleshooting.md`
- [ ] 收录 `ModuleNotFoundError`
- [ ] 收录 Python 版本不兼容问题
- [ ] 收录 Node / npm 版本问题
- [ ] 收录 docs build 失败的常见原因
- [ ] 后续有真实模型接入后补 API key 问题

**完成标准**
- 新手遇到常见错误时，不需要翻 issue 才知道怎么排查

---

### 6. 标清教学示例的层级
- [ ] 在各章 README 里明确标注：这是 **toy / 教学版 / 真实框架版 / 工程版** 的哪一类
- [ ] 在章节正文里说明：当前示例重点是“理解流程”还是“使用真实 API”
- [ ] 避免读者误把 toy demo 当成完整生产实现

**完成标准**
- 读者能清楚知道每章示例的边界，不会学完 toy demo 就误以为自己已经掌握工程化实现

---

## P1 - 重要优化（会显著提升项目质量和教学体验）

### 7. 增加术语表
- [ ] 新增 `docs/faq/glossary.md` 或 `docs/glossary.md`
- [ ] 补充术语：Runnable
- [ ] 补充术语：LCEL
- [ ] 补充术语：Retriever
- [ ] 补充术语：Vector Store
- [ ] 补充术语：Tool Calling
- [ ] 补充术语：Agent
- [ ] 补充术语：LangGraph State
- [ ] 补充术语：Trace / Evaluation

**完成标准**
- 新读者在阅读章节时遇到高频术语有一个统一查询入口

---

### 8. 增加学习计划页
- [ ] 新增 `docs/guide/study-plan.md`
- [ ] 提供 7 天版学习路径
- [ ] 提供 14 天版学习路径
- [ ] 提供 30 天版学习路径
- [ ] 每章标注建议耗时、输入前提、完成标准

**完成标准**
- 读者不只是“知道章节顺序”，而是知道该怎么安排自己的学习节奏

---

### 9. 给每章增加“学完验收标准”
- [ ] 在每章结尾增加“你现在应该会”
- [ ] 增加最小验收 checklist
- [ ] 增加“建议动手改什么”
- [ ] 增加“如果卡住先回看哪一章”

**完成标准**
- 章节学习结果可判断，不再只是“看完了”

---

### 10. 把硬编码课程资料拆到数据文件
- [ ] 把 `chapter-05` 示例中的课程资料移到 `data/` 或 `shared/datasets/`
- [ ] 把 `chapter-06` 示例中的课程资料移到 `data/` 或 `shared/datasets/`
- [ ] 让示例代码和教学数据分离
- [ ] 顺手在文档里讲清“知识与逻辑分离”的工程意义

**完成标准**
- 示例结构更接近真实 RAG 项目
- 更容易替换数据源做练习

---

### 11. 为未来真实模型接入预留统一 `.env.example`
- [ ] 在需要扩展的章节目录下增加 `.env.example`
- [ ] 根目录可增加统一环境变量说明
- [ ] 变量命名保持一致（如 `OPENAI_API_KEY`, `MODEL_NAME`）

**完成标准**
- 后续切换到真实模型时，不需要重做目录规范

---

### 12. 增加 lint / 格式检查
- [ ] Python 接入 `ruff`
- [ ] 可选接入 `mypy`
- [ ] Markdown 接入基础 lint 或至少做格式约束
- [ ] 补贡献者最小规范

**完成标准**
- 仓库风格更统一，后续扩展成本更低

---

## P2 - 进阶增强（让项目从“好课程”更接近“强开源项目”）

### 13. 为关键章节增加“真实框架版”示例
- [ ] 第 3 章补一个真实 `langchain-core` 版本链式示例
- [ ] 第 5 章补一个更真实的基础 RAG 示例
- [ ] 第 6 章补一个更真实的检索优化示例
- [ ] 第 7/8 章补一个更接近实际框架接口的版本

**完成标准**
- 教学版与真实版形成对照，帮助读者从概念过渡到工程实践

---

### 14. 丰富 `shared/` 目录的真实内容
- [ ] 新建 `shared/prompts/`
- [ ] 新建 `shared/datasets/`
- [ ] 新建 `shared/diagrams/`
- [ ] 把跨章节会复用的资料沉淀进去

**完成标准**
- `shared/` 不再只是预留目录，而是开始承载共用资产

---

### 15. 给 `backend/` 一个最小可见成果
- [ ] 明确标注 backend 目前是 phase 2 占位
- [ ] 或者直接补一个最小 FastAPI 骨架
- [ ] 至少包含健康检查路由和一个 demo 接口
- [ ] 在 README 写清当前能力边界

**完成标准**
- 读者能分清“当前已实现”与“未来规划”

---

### 16. 增加对比型内容页
- [ ] 增加 `LangChain vs LlamaIndex`
- [ ] 增加 `Chain vs Agent`
- [ ] 增加 `RAG vs Fine-tuning`
- [ ] 增加 `LangGraph vs 普通链式调用`

**完成标准**
- 站点更适合作为公开传播入口，而不只是课程笔记

---

### 17. 增加真实应用改造建议页
- [ ] 课程助手如何扩展成知识库问答
- [ ] 如何改造成公司文档助手
- [ ] 如何改造成论文问答助手
- [ ] 如何改造成客服问答机器人

**完成标准**
- 读者能把教学项目迁移到自己的实际场景

---

## 建议执行顺序

### 第 1 轮（最值得先做）
1. 版本基线
2. 统一依赖管理
3. CI smoke tests
4. setup 文档
5. troubleshooting 文档
6. 标注 toy / real 边界

### 第 2 轮
7. 术语表
8. 学习计划页
9. 每章验收标准
10. 数据文件拆分
11. `.env.example`
12. lint

### 第 3 轮
13. 真实框架版示例
14. shared 资产沉淀
15. backend 最小骨架
16. 对比页
17. 场景改造页

---

## 可以直接转成 GitHub Issues 的主题
- [ ] docs: add environment baseline and version policy
- [ ] build: unify Python dependency management
- [ ] ci: add example smoke tests and docs build checks
- [ ] docs: add beginner setup guide
- [ ] docs: add troubleshooting page
- [ ] docs: label examples by teaching/engineering level
- [ ] docs: add glossary page
- [ ] docs: add study plan page
- [ ] docs: add chapter completion checklist
- [ ] refactor: move course materials into shared datasets
- [ ] chore: add env examples for future real-model chapters
- [ ] chore: add ruff and basic quality checks
- [ ] feat: add more realistic RAG/Agent examples
- [ ] feat: populate shared assets
- [ ] feat: add minimal FastAPI backend scaffold
- [ ] docs: add comparison pages for key concepts
- [ ] docs: add real-world adaptation guides

---

## 一句话总结

当前项目的核心问题不是“内容不够多”，而是：

1. **新手能不能稳定跑通**
2. **仓库能不能长期维护不坏**
3. **教学 demo 能不能顺滑过渡到真实工程认知**

先把这三件事补稳，这个项目的完成度会明显上一个台阶。
