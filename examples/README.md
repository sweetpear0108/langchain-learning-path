# Examples

这里存放 10 个章节对应的最小可运行示例。

## 目录结构

- `chapter-01`：LLM 应用基础
- `chapter-02`：LangChain 核心抽象
- `chapter-03`：第一个链式应用
- `chapter-04`：Prompt 工程与输出控制
- `chapter-05`：RAG 入门
- `chapter-06`：RAG 进阶优化
- `chapter-07`：Tools 与 Agent
- `chapter-08`：LangGraph 工作流
- `chapter-09`：评估、观测与调试
- `chapter-10`：综合实战与公开部署

## 示例层级说明

为了避免把课程示例误读成生产实现，仓库统一使用下面三档层级：

- `Toy`：用本地假数据或占位实现讲清一个最小概念，不追求真实 API 接入。
- `教学版`：保留真实工程结构，但会简化模型、检索、工具或状态管理，重点是理解流程和模块边界。
- `更真实的工程版`：更接近真实项目里的检查、评估或交付方式，但仍然是课程仓库中的可控样例，不等于可直接上线。

当前各章示例的大致定位如下：

- `chapter-01` 到 `chapter-02`：`Toy`
- `chapter-03` 到 `chapter-08`：`教学版`
- `chapter-09` 到 `chapter-10`：`更真实的工程版`

## 使用方式

优先阅读每个章节目录下的 `README.md`。

如果你要连续跑多个 LangChain 章节，优先在仓库根目录准备一套共享环境：

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

典型单章流程仍然保留：

```bash
cd examples/chapter-03
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

`chapter-03` 到 `chapter-06` 的章节级 `requirements.txt` 会自动复用根目录的版本边界；如果某一章不需要第三方依赖，会在该章节的 `README.md` 中直接说明。
