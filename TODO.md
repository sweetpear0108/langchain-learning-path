# TODO - LangChain Learning Path

这份清单基于当前仓库的实际状态重排，目标是把项目从“已经有内容的仓库”推进到“稳定、可发布、可维护的公开学习项目”。

执行原则：

- 先做发布基线和工程稳定性
- 再补新手体验和教学闭环
- 最后再做二期能力和传播增强

建议按优先级推进：`P0 -> P1 -> P2`

---

## P0 - 当前必须优先完成

### 1. 冻结仓库发布基线

- [ ] 创建第一次正式提交
- [ ] 统一首版提交信息和版本说明
- [ ] 在 README 中补“如何启用 GitHub Pages”说明
- [ ] 明确当前仓库属于 phase 1：静态学习站 + 本地示例
- [ ] 标出 phase 2 仍未开始的能力边界

**完成标准**

- 仓库存在清晰的首个可发布基线
- 新读者能看懂“当前已经实现什么、还没实现什么”

---

### 2. 明确版本基线

- [ ] 在根目录 README 增加“推荐环境”小节
- [ ] 明确推荐 Python 版本为 `3.11`
- [ ] 明确推荐 Node 版本为 `20 LTS`
- [ ] 明确教程适配的 `langchain-core` 版本范围
- [ ] 明确教程适配的 `langchain-text-splitters` 版本范围
- [ ] 在文档中说明：LangChain API 变化较快，教程以仓库锁定版本为准

**完成标准**

- 首页或 README 能直接看到环境要求
- 依赖大版本边界写清楚

---

### 3. 统一 Python 依赖管理

- [ ] 在仓库根目录新增 `pyproject.toml` 或根级 `requirements.txt`
- [ ] 定义公共基础依赖
- [ ] 保留章节目录中的 `requirements.txt`，但避免完全分裂管理
- [ ] 评估是否需要 `requirements-dev.txt`
- [ ] 给未来章节扩展留出统一升级入口

**完成标准**

- 新用户不需要逐章猜依赖
- 维护者能统一升级和回退

---

### 4. 补 CI / 自动检查

- [ ] 新增 GitHub Actions：文档站 build check
- [ ] 新增 GitHub Actions：示例代码 smoke test
- [ ] 至少验证 `examples/chapter-01`
- [ ] 至少验证 `examples/chapter-02`
- [ ] 至少验证 `examples/chapter-09`
- [ ] 至少验证 `examples/chapter-10`
- [ ] 可选增加 Markdown 链接检查

**完成标准**

- PR 合并前能发现明显跑不通的问题
- 文档改动不会静默破坏站点构建

---

### 5. 补真正的新手 setup 文档

- [ ] 新增 `docs/guide/setup.md`
- [ ] 写清 Python 虚拟环境创建方式
- [ ] 写清 Node 依赖安装方式
- [ ] 写清如何运行单章示例
- [ ] 写清如何运行文档站
- [ ] 给出第一次学习的推荐顺序

**完成标准**

- 一个第一次接触仓库的人，30 分钟内能把 docs 和至少一个 example 跑起来

---

### 6. 补故障排查页

- [ ] 新增 `docs/faq/troubleshooting.md`
- [ ] 收录 `ModuleNotFoundError`
- [ ] 收录 Python 版本不兼容问题
- [ ] 收录 Node / npm 版本问题
- [ ] 收录 docs build 失败的常见原因
- [ ] 后续有真实模型接入后补 API key 问题

**完成标准**

- 新手遇到常见错误时，不需要翻 issue 才知道怎么排查

---

### 7. 标清示例的教学层级

- [ ] 在各章 example README 中明确标注：这是 `toy / 教学版 / 真实框架版 / 工程版` 的哪一类
- [ ] 在章节正文里说明：当前示例重点是“理解流程”还是“使用真实 API”
- [ ] 避免读者误把 toy demo 当成生产实现

**完成标准**

- 读者能清楚知道每章示例的边界

---

## P1 - 下一轮最值得做的增强

### 8. 给每章增加“学完验收标准”

- [ ] 在每章结尾增加“你现在应该会”
- [ ] 增加最小验收 checklist
- [ ] 增加“建议动手改什么”
- [ ] 增加“如果卡住先回看哪一章”

**完成标准**

- 学习结果可判断，不再只是“看完了”

---

### 9. 增加术语表

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

- 新读者阅读章节时遇到高频术语有统一查询入口

---

### 10. 增加学习计划页

- [ ] 新增 `docs/guide/study-plan.md`
- [ ] 提供 7 天版学习路径
- [ ] 提供 14 天版学习路径
- [ ] 提供 30 天版学习路径
- [ ] 每章标注建议耗时、输入前提、完成标准

**完成标准**

- 读者知道该怎么安排自己的学习节奏

---

### 11. 把教学数据拆到数据文件

- [ ] 把 `chapter-05` 示例中的课程资料移到 `shared/datasets/`
- [ ] 把 `chapter-06` 示例中的课程资料移到 `shared/datasets/`
- [ ] 让示例代码和教学数据分离
- [ ] 在文档里说明“知识与逻辑分离”的工程意义

**完成标准**

- 示例结构更接近真实 RAG 项目
- 更容易替换数据源做练习

---

### 12. 为未来真实模型接入预留统一 `.env.example`

- [ ] 在需要扩展的章节目录下增加 `.env.example`
- [ ] 根目录增加统一环境变量说明
- [ ] 变量命名保持一致，如 `OPENAI_API_KEY`、`MODEL_NAME`

**完成标准**

- 后续切换到真实模型时，不需要重做目录规范

---

### 13. 增加 lint / 格式检查

- [ ] Python 接入 `ruff`
- [ ] 可选接入 `mypy`
- [ ] Markdown 接入基础 lint
- [ ] 补贡献者最小规范

**完成标准**

- 仓库风格更统一
- 后续扩展成本更低

---

### 14. 给 backend 一个最小可见成果

- [ ] 明确标注 backend 当前是 phase 2 占位
- [ ] 或直接补一个最小 FastAPI 骨架
- [ ] 至少包含健康检查路由
- [ ] 至少包含一个 demo 接口
- [ ] 在 README 写清当前能力边界

**完成标准**

- 读者能分清“当前已实现”和“未来规划”

---

## P2 - 进阶增强

### 15. 为关键章节增加真实框架版示例

- [ ] 第 3 章补一个真实 `langchain-core` 版本链式示例
- [ ] 第 5 章补一个更真实的基础 RAG 示例
- [ ] 第 6 章补一个更真实的检索优化示例
- [ ] 第 7 章补一个更接近实际框架接口的版本
- [ ] 第 8 章补一个更接近实际框架接口的版本

**完成标准**

- 教学版与真实版形成对照
- 帮助读者从概念过渡到工程实践

---

### 16. 丰富 `shared/` 目录的真实内容

- [ ] 补充 `shared/prompts/`
- [ ] 补充 `shared/datasets/`
- [ ] 补充 `shared/diagrams/`
- [ ] 把跨章节复用的资料沉淀进去

**完成标准**

- `shared/` 不再只是预留目录

---

### 17. 增加对比型内容页

- [ ] 增加 `LangChain vs LlamaIndex`
- [ ] 增加 `Chain vs Agent`
- [ ] 增加 `RAG vs Fine-tuning`
- [ ] 增加 `LangGraph vs 普通链式调用`

**完成标准**

- 站点更适合作为公开传播入口

---

### 18. 增加真实应用改造建议页

- [ ] 课程助手如何扩展成知识库问答
- [ ] 如何改造成公司文档助手
- [ ] 如何改造成论文问答助手
- [ ] 如何改造成客服问答机器人

**完成标准**

- 读者能把教学项目迁移到自己的实际场景

---

## 建议执行顺序

### 第 1 轮

1. 冻结仓库发布基线
2. 明确版本基线
3. 统一 Python 依赖管理
4. 补 CI / 自动检查
5. 补真正的新手 setup 文档
6. 补故障排查页
7. 标清示例的教学层级

### 第 2 轮

8. 每章增加学完验收标准
9. 增加术语表
10. 增加学习计划页
11. 把教学数据拆到数据文件
12. 为未来真实模型接入预留统一 `.env.example`
13. 增加 lint / 格式检查
14. 给 backend 一个最小可见成果

### 第 3 轮

15. 为关键章节增加真实框架版示例
16. 丰富 `shared/` 目录
17. 增加对比型内容页
18. 增加真实应用改造建议页

---

## 可以直接转成 GitHub Issues 的主题

- [ ] chore: create initial release baseline and publish notes
- [ ] docs: add environment baseline and version policy
- [ ] build: unify Python dependency management
- [ ] ci: add docs build checks and example smoke tests
- [ ] docs: add beginner setup guide
- [ ] docs: add troubleshooting page
- [ ] docs: label examples by teaching level
- [ ] docs: add chapter completion checklist
- [ ] docs: add glossary page
- [ ] docs: add study plan page
- [ ] refactor: move teaching data into shared datasets
- [ ] chore: add env examples for future real-model chapters
- [ ] chore: add ruff and basic quality checks
- [ ] feat: add minimal FastAPI backend scaffold
- [ ] feat: add more realistic framework-based examples
- [ ] feat: populate shared assets
- [ ] docs: add comparison pages
- [ ] docs: add scenario adaptation guides
