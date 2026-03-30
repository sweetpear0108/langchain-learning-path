# 第 2 章：LangChain 核心抽象

## 章节定位

上一章解决的是“LLM 应用是什么”。这一章开始回答“LangChain 到底在帮你组织什么”。

如果说上一章是在建立心智模型，这一章就是正式进入工具层：你会开始接触 LangChain 的几个核心抽象，并理解为什么它们能把模型调用变成可维护的工程结构。

## 配套示例

- 目录：`examples/chapter-02`
- 入口：`examples/chapter-02/main.py`
- 依赖：`examples/chapter-02/requirements.txt`
- 运行：`cd examples/chapter-02 && python3 main.py`

## 示例层级与边界

- 层级：`Toy`
- 本章重点：理解 LangChain 核心抽象为什么值得拆分，而不是学习某个真实模型供应商的完整接法。
- 不要误判：示例只保留最小 LCEL 思维模型，不覆盖真实回调、配置管理或复杂链路。

## 本章目标

学完这一章，你应该能够：

- 说清楚 LangChain 在工程里的位置
- 理解 `PromptTemplate`、`Chat Model`、`Output Parser` 的作用
- 理解 `Runnable` 和 `LCEL` 的基本思想
- 写出一个可组合、可扩展的最小链式程序
- 给 `AI 学习助手` 的后续章节打下结构基础

## 前置知识

建议你已经理解：

- 第 1 章中关于 `prompt`、`message`、`context` 的概念
- Python 函数和字典的基本使用
- 最简单的模型调用流程

如果你对这些还不熟，建议先回到第 1 章再看一遍。

## 2.1 LangChain 在工程中的位置

LangChain 不是模型，不是数据库，也不是 UI 框架。它的角色更像一个“LLM 应用编排层”。

它主要帮你处理这些事：

- 组织 Prompt
- 封装模型调用
- 统一输出解析
- 把多个步骤串成链
- 为后续 RAG、Agent、工作流提供共同接口

它不负责这些事：

- 训练模型
- 提供自己的大模型
- 替你设计业务目标
- 自动解决所有工程问题

这个边界很重要。很多初学者会把框架当成“万能答案”，结果学习时只会照抄例子，不知道每一层为什么存在。

## 2.2 `PromptTemplate`

`PromptTemplate` 的作用是把提示词从硬编码字符串里抽出来，变成可复用模板。

它解决的不是“写 prompt”，而是“管理 prompt”。

为什么要这么做：

- 业务参数会变
- 同一个模板会被不同章节复用
- 你需要把任务描述、输入变量和格式要求分开

例如，你可以把“主题”变成一个变量：

```python
template = """
你是一个中文技术导师。
请用 3 点解释 {topic}，每点都要短、清晰、适合初学者。
"""
```

这样就可以反复用于不同主题，而不需要每次手写整段 prompt。

## 2.3 `Chat Model`

`Chat Model` 是对聊天式模型接口的封装。

它的价值不只是“能调用模型”，而是让你把调用参数也纳入工程管理：

- 模型名称
- 温度
- 最大输出长度
- 流式输出
- 消息格式

在真实项目里，这些参数不会一直固定。不同场景会有不同需求：

- 学习建议需要更稳定的输出
- 创意写作可以更高温度
- 结构化结果通常要更低随机性

所以模型本身也需要像配置一样被管理，而不是散落在代码各处。

## 2.4 `Output Parser`

模型输出默认是自然语言，但程序通常更喜欢结构化结果。

`Output Parser` 的作用，就是把模型输出转成程序可处理的数据。

为什么这一步关键：

- UI 可以直接消费结构化字段
- 后续逻辑可以按字段分支处理
- 调试时更容易知道哪里出错

例如，`AI 学习助手` 可能希望拿到这样的结构：

```json
{
  "title": "LangChain 入门建议",
  "steps": [
    "先理解 LLM 应用基础",
    "再学习 LangChain 核心抽象",
    "最后做第一个链式应用"
  ],
  "difficulty": "beginner"
}
```

如果没有 parser，你就只能手工从一段自然语言里猜字段含义，这会让后续工程越来越脆弱。

## 2.5 `Runnable` 与 `LCEL`

`Runnable` 是 LangChain 里非常核心的抽象之一。你可以把它理解成“一个可组合的执行单元”。

`LCEL` 是 LangChain 的表达式语言，它允许你用类似管道的方式把步骤串起来：

```python
prompt | model | parser
```

这种写法的价值在于：

- 每一步职责清晰
- 组合方式统一
- 更容易读懂和维护
- 后续扩展时不需要重写整段流程

你可以把它理解成：

- `prompt` 负责准备输入
- `model` 负责推理
- `parser` 负责整理输出

这比把所有逻辑塞进一个函数里要稳得多。

## 2.6 最小示例：文本总结器

下面给出一个“概念上的最小链式程序”。这里的重点不是某个具体模型供应商，而是理解组件如何连接。

```python
from dataclasses import dataclass


@dataclass
class PromptTemplate:
    template: str

    def format(self, **kwargs) -> str:
        return self.template.format(**kwargs)


class ChatModel:
    def invoke(self, prompt: str) -> str:
        return f"模拟模型输出：{prompt}"


class OutputParser:
    def invoke(self, text: str) -> dict:
        return {
            "summary": text,
            "length_hint": len(text)
        }


def main() -> None:
    prompt = PromptTemplate(
        template="请把下面内容总结成 3 点：{content}"
    )
    model = ChatModel()
    parser = OutputParser()

    formatted = prompt.format(content="LangChain 用于组织 LLM 应用流程")
    raw = model.invoke(formatted)
    result = parser.invoke(raw)

    print(result)


if __name__ == "__main__":
    main()
```

这个例子还不是完整 LangChain 代码，但它准确表达了核心思想：

1. 模板化输入
2. 模型执行
3. 输出整理

第 3 章会在这个思路上继续往前走，写出真正意义上的 `AI 学习助手 V1`。

## 2.7 `AI 学习助手` 的结构化第一版

在这一章里，`AI 学习助手` 可以先升级成这样：

- 输入一个学习主题
- 输出一个摘要
- 输出一个难度级别
- 输出一个推荐学习步骤列表

这意味着你开始把“回答问题”变成“回答并可程序化处理”。

这一步非常重要，因为后面的 RAG 和 Agent，都需要结构化能力作为基础。

## 2.8 本章实践

请你完成以下任务：

1. 为 `PromptTemplate` 写一个自己的模板
2. 用一个固定主题测试模板格式化结果
3. 设计一个你希望模型输出的结构化 JSON
4. 思考这个 JSON 为什么比自然语言更适合程序处理

如果你愿意继续推进，可以把你设计的结构直接当成 `AI 学习助手 V1` 的输出格式。

## 2.9 常见坑

- 把 LangChain 当成模型提供商
- 认为 `PromptTemplate` 只是把字符串拼起来
- 忽略输出解析的必要性
- 把多个职责塞进一个长函数里
- 过早追求复杂链路，导致最小可运行版本都没有

## 2.10 练习题

1. LangChain 在工程中的位置是什么？
2. `PromptTemplate` 解决的核心问题是什么？
3. 为什么输出解析在真实项目里很重要？
4. `prompt | model | parser` 这种结构相比单函数方案有什么优势？

## 本章总结

这一章的核心收获是：你开始从“调用模型”走向“组织模型能力”。

你已经接触到 LangChain 最重要的三个基础层：

- `PromptTemplate` 负责输入可复用
- `Chat Model` 负责模型执行
- `Output Parser` 负责输出可处理

再加上 `Runnable` 和 `LCEL`，你就已经拥有了构建简单但可维护的 LLM 应用骨架。

下一章我们会基于这些基础，正式构建 `AI 学习助手 V1`，把零散组件真正串成一个最小链式应用。

## 学完本章，你现在应该会

- 解释 `PromptTemplate`、`Chat Model`、`Output Parser` 各自负责什么
- 说清 `Runnable` 和 `LCEL` 为什么让链路更容易组合
- 把一个自然语言需求拆成输入模板、模型执行和输出解析三个步骤
- 说明为什么结构化输出对 `AI 学习助手` 后续章节很关键

## 最小验收 checklist

- [ ] 我能写出一个最小的 `prompt | model | parser` 结构
- [ ] 我能解释模板化输入相比直接拼字符串的工程价值
- [ ] 我能设计一个简单的结构化输出字段集合
- [ ] 我知道 Parser 的职责不是“美化文本”，而是让结果可继续处理

## 建议你动手改一版

- 把本章示例的输出改成固定字段，例如 `summary`、`difficulty`、`steps`
- 给 `AI 学习助手 V1` 增加一个“学习时长建议”字段，看看 Prompt 和 Parser 要怎么一起调整
- 尝试把输出改成 Markdown 列表，再比较它和 JSON 各自适合什么场景

## 卡住时先回看这里

- 如果你混淆了 LangChain 和模型提供商，回看 [chapter-02-langchain-core.md](/home/litianwei/langchain-learning-path/docs/chapters/chapter-02-langchain-core.md) 里的 `## 2.1 LangChain 在工程中的位置`
- 如果你不清楚模板和解析器为什么要分开，回看 [chapter-02-langchain-core.md](/home/litianwei/langchain-learning-path/docs/chapters/chapter-02-langchain-core.md) 里的 `## 2.2 PromptTemplate` 到 `## 2.4 Output Parser`
- 如果你不知道这些抽象最终要服务什么项目形态，回看 [chapter-02-langchain-core.md](/home/litianwei/langchain-learning-path/docs/chapters/chapter-02-langchain-core.md) 里的 `## 2.7 AI 学习助手 的结构化第一版`

## 下一章预告

下一章会把本章的抽象组合起来，完成第一个可运行的链式应用，并开始处理“输入主题、生成学习建议、输出结构化结果”这类更接近真实项目的任务。
