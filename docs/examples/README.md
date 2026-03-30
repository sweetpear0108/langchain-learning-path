# 示例代码总览

每一章都对应一个最小可运行示例，统一放在仓库根目录的 `examples/` 下。

## 通用运行方式

纯标准库章节：

```bash
cd examples/chapter-01
python3 main.py
```

需要安装依赖的章节：

```bash
cd examples/chapter-03
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

## 章节与目录对应关系

| 章节 | 目录 | 运行入口 |
| --- | --- | --- |
| 第 1 章：LLM 应用基础 | `examples/chapter-01` | `python3 main.py` |
| 第 2 章：LangChain 核心抽象 | `examples/chapter-02` | `python3 main.py` |
| 第 3 章：第一个链式应用 | `examples/chapter-03` | `python3 main.py` |
| 第 4 章：Prompt 工程与输出控制 | `examples/chapter-04` | `python3 main.py` |
| 第 5 章：RAG 入门 | `examples/chapter-05` | `python3 main.py` |
| 第 6 章：RAG 进阶优化 | `examples/chapter-06` | `python3 main.py` |
| 第 7 章：Tools 与 Agent | `examples/chapter-07` | `python3 main.py` |
| 第 8 章：LangGraph 工作流 | `examples/chapter-08` | `python3 main.py` |
| 第 9 章：评估、观测与调试 | `examples/chapter-09` | `python3 main.py` |
| 第 10 章：综合实战与公开部署 | `examples/chapter-10` | `python3 main.py` |

## 使用建议

- 先看对应章节正文，再跑示例
- 不要只跑通一次，要改一个小地方再运行一次
- 如果章节示例使用第三方依赖，优先看目录内的 `README.md`
- 如果你在做主项目升级，尽量按章节顺序推进
