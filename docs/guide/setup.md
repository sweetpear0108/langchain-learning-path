# 新手 Setup

这页只解决一件事：第一次接触这个仓库时，如何在 30 分钟内把文档站和至少一个示例跑起来。

如果你还不确定先看什么，直接照着这页做，不用先研究全仓库。

## 你要先准备什么

建议本地环境直接对齐仓库当前基线：

- `Python 3.11`
- `Node.js 20 LTS`
- 与 `Node.js 20 LTS` 配套的默认 `npm`

先确认版本：

```bash
python3 --version
node --version
npm --version
```

如果你的机器上 `python3` 不存在，也可以试：

```bash
python --version
```

后面的命令默认使用 `python3`。如果你的系统只有 `python`，把命令里的 `python3` 替换掉即可。

## 第一步：克隆仓库并进入目录

```bash
git clone <your-repo-url>
cd langchain-learning-path
```

如果你已经拿到仓库压缩包或已有本地副本，直接进入仓库根目录即可。

## 第二步：先把文档站跑起来

先安装前端依赖：

```bash
npm install
```

启动文档站：

```bash
npm run docs:dev
```

正常情况下，你会看到 VitePress 启动日志，并能在浏览器里打开本地地址。

常用命令还有两个：

```bash
npm run docs:build
npm run docs:preview
```

- `docs:build` 用来确认文档站可以成功构建
- `docs:preview` 用来本地预览构建后的静态站

如果你只是第一次体验仓库，先跑通 `npm run docs:dev` 就够了。

## 第三步：创建 Python 虚拟环境

如果你准备连续跑多个章节，建议直接在仓库根目录创建一套共享虚拟环境。

创建虚拟环境：

```bash
python3 -m venv .venv
```

激活方式：

```bash
source .venv/bin/activate
```

安装根目录依赖：

```bash
python3 -m pip install -r requirements.txt
```

执行完后，`chapter-03` 到 `chapter-06` 这类依赖 LangChain 的章节就能直接复用这套环境，不需要每章重新猜版本。

## 第四步：先跑一个最容易成功的示例

第一次建议从 `chapter-01` 开始。它只用 Python 标准库，不需要 API Key，也不依赖第三方模型服务。

如果你已经在仓库根目录激活了 `.venv`，直接运行：

```bash
python3 examples/chapter-01/main.py
```

你也可以进入章节目录再执行：

```bash
cd examples/chapter-01
python3 main.py
```

预期结果：

- 终端会打印组装后的 Prompt
- 终端会打印 `ToyLLM` 返回的示例学习摘要

跑通这一章，就说明你的 Python 运行环境没有问题，仓库最小教学链路也已经打通。

## 如果你只想运行单章示例

有些读者不想先装整仓库依赖，只想临时试一个章节。这种情况下，可以在章节目录里单独建虚拟环境。

典型流程：

```bash
cd examples/chapter-03
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 main.py
```

适用场景：

- 你只打算试单章，不准备连续学习
- 你想把某一章和其他实验环境隔离开

如果某一章不需要第三方依赖，对应章节的 `README.md` 会直接说明。

## 文档站和示例分别怎么用

建议把两类入口分开理解：

- 文档站：负责解释这一章学什么、为什么这样设计、有哪些常见坑
- `examples/`：负责让你把最小代码亲手跑起来

第一次上手最稳的节奏是：

1. 先启动文档站，确认能浏览课程结构
2. 再跑 `chapter-01` 示例，确认 Python 运行没问题
3. 然后边看章节正文边改动示例代码

不要一开始就直冲 `chapter-07` 或 `chapter-08`。那样通常会跳过前面的抽象基础，后面只剩下背术语。

## 第一次学习顺序

如果你是第一次系统接触 LangChain，建议按下面的顺序走：

1. 先看 [快速开始](./getting-started.md)，知道整个仓库怎么组织
2. 再看 [学习路线图](./roadmap.md)，理解为什么章节顺序不能乱
3. 启动文档站：`npm run docs:dev`
4. 跑通 `chapter-01`：`python3 examples/chapter-01/main.py`
5. 继续读第 1 章和第 2 章，再进入第 3 章开始接触真正的 LangChain 抽象

更具体一点：

- 第 1、2 章：先建立应用视角和核心抽象
- 第 3、4 章：开始写链式应用和可控输出
- 第 5、6 章：进入 RAG
- 第 7、8 章：进入 Agent 和 LangGraph
- 第 9、10 章：补评估、观测、调试和部署

## 30 分钟自检清单

如果你想确认自己是否已经完成最小 setup，可以按这份清单自检：

- `node --version` 和 `python3 --version` 都可用
- `npm install` 成功
- `npm run docs:dev` 能启动文档站
- 虚拟环境 `.venv` 已创建并激活
- `python3 examples/chapter-01/main.py` 能成功输出内容

完成这 5 件事，你就已经具备继续学习这个仓库的最小环境。
