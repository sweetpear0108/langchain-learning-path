# 第 2 章示例：LangChain 核心抽象

这个示例对应课程第 2 章，目标是把 `PromptTemplate + model + parser` 的最小链路跑通。

它演示的是一个教学版的 LCEL 思维模型：

- `PromptTemplate` 负责组织输入
- `DemoModel` 负责生成文本
- `StructuredParser` 负责把文本转成结构化结果
- `chain = prompt | model | parser` 负责把三者串起来

## 章节目标

- 理解 LangChain 最核心的三类角色
- 体验链式组合的基本结构
- 为后续第 3 章和第 4 章打下基础

## 运行前提

- Python 3.10+
- 不需要 API key
- 不需要额外网络资源

## 安装方式

本示例只使用 Python 标准库，不需要安装第三方依赖。

## 运行命令

```bash
python3 main.py
```

## 预期输出

你会看到：

- 由 `PromptTemplate` 生成的提示词
- 模型返回的摘要文本
- 解析器提取出的结构化字典

## 你在学什么

你在学的是“如何把一个 LLM 应用拆成稳定的模块”。

这不是为了模拟某个框架的全部 API，而是为了让你一开始就形成正确的工程思维：输入、模型和输出解析应该分开，而不是揉成一个大函数。
