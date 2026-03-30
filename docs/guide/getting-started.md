# 快速开始

这一页解决三个问题：

1. 你应该按什么顺序学习  
2. 本地怎么把文档站和示例代码跑起来  
3. 什么叫“学完一章”

如果你是第一次接触这个仓库，先看 [新手 Setup](./setup.md) 再回来读这一页，路径会更稳。

## 推荐学习顺序

如果你是第一次系统学习 LangChain，建议严格按章节顺序来：

1. 先完成第 1、2 章，建立基础抽象
2. 再做第 3、4 章，真正写出链式应用
3. 再进入第 5、6 章，理解 RAG 与优化
4. 再做第 7、8 章，进入 Agent 和 LangGraph
5. 最后完成第 9、10 章，补工程化与公开部署

不要一上来就跳到 Agent 或 LangGraph。那样通常只会背名词，不会做项目。

## 运行文档站

前置条件：

- Node.js 18+
- npm 9+

安装依赖：

```bash
npm install
```

启动 VitePress 本地站点：

```bash
npm run docs:dev
```

构建静态站点：

```bash
npm run docs:build
```

本地预览构建结果：

```bash
npm run docs:preview
```

## 运行章节示例

前置条件：

- Python 3.11+
- 能创建虚拟环境

如果你准备连续跑多个 LangChain 章节，先在仓库根目录安装共享依赖最省事：

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

以某一章示例为例：

```bash
cd examples/chapter-01
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

`chapter-03` 到 `chapter-06` 的 `requirements.txt` 会自动继承仓库根目录的版本边界，所以单章安装和根目录统一安装不会出现版本分叉。

如果章节示例需要模型 API Key，会在该章节目录下提供 `.env.example`，并在 `README.md` 写清楚变量名和用途。

所有章节目录和运行入口可以在 [示例代码总览](../examples/README.md) 里直接查看。

## 每章应该怎么学

建议每章按这个顺序走：

1. 先读章节正文，理解这一章在主项目里的位置
2. 再看最小示例，确认输入、输出、依赖和数据流
3. 自己运行一次代码
4. 改一个小地方，例如改 Prompt、改字段、改输入
5. 再回到正文看“常见坑”和“练习题”

## 学完一章的标准

不是“看懂了就算会”，而是至少做到下面三件事：

- 能说清楚这一章解决了什么问题
- 能自己把示例跑通
- 能做一个小改动而不把整个链路弄乱

## 建议的学习节奏

- 工作日晚间：一晚读一章正文，第二晚跑一章示例
- 周末：回顾前面两章，补练习题和自己的笔记

这样比“连续看 6 章不动手”有效得多。
