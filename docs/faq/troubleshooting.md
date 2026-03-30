# 故障排查

这页只解决一件事：当你第一次跑这个仓库时，如果环境、依赖或文档构建报错，先按这里排查，不用先翻 issue。

## 先判断你卡在哪一层

先不要一上来就同时重装所有东西。先看报错属于哪一类：

- `python` / `python3` 命令本身不可用
- `ModuleNotFoundError` 或 `ImportError`
- `node` / `npm` 版本过低，或安装依赖失败
- `npm run docs:build` 构建失败

建议先执行：

```bash
python3 --version
node --version
npm --version
```

如果你的系统没有 `python3`，再试一次：

```bash
python --version
```

本仓库当前推荐基线：

- `Python 3.11`
- `Node.js 20 LTS`
- 与 `Node.js 20 LTS` 配套的默认 `npm`

## ModuleNotFoundError: No module named 'xxx'

这类错误大多数不是“代码坏了”，而是你没有在正确的 Python 环境里安装依赖。

常见表现：

- `ModuleNotFoundError: No module named 'langchain_core'`
- `ModuleNotFoundError: No module named 'langchain_text_splitters'`
- 你明明装过依赖，但换一个终端又找不到模块

优先按这个顺序排查：

1. 确认你当前使用的 Python 和 pip 指向同一套环境
2. 确认虚拟环境已经激活
3. 确认依赖装在仓库根目录或当前章节目录对应的环境里

可以直接执行：

```bash
python3 -c "import sys; print(sys.executable)"
python3 -m pip --version
```

如果两条命令显示的路径不在你的虚拟环境里，先重新激活环境：

```bash
source .venv/bin/activate
```

推荐修复方式：

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

如果你只想运行单章，也可以在章节目录单独安装：

```bash
cd examples/chapter-03
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 main.py
```

额外注意：

- 不要混用系统 `pip` 和虚拟环境里的 `python`
- 优先使用 `python3 -m pip install ...`，不要直接猜 `pip` 指向哪里
- 切换终端后，虚拟环境需要重新激活

## Python 版本不兼容

如果你使用的是过低或过新的 Python，常见现象包括：

- `SyntaxError`，但代码本身看起来没问题
- 某些依赖安装时报版本不支持
- `pip install -r requirements.txt` 过程中提示当前 Python 版本不满足要求

先确认版本：

```bash
python3 --version
```

本仓库推荐直接使用 `Python 3.11`。如果你现在是 `3.9`、`3.10` 或更高的未验证版本，先不要继续猜依赖问题，先把解释器对齐。

更稳的做法是：

1. 安装 `Python 3.11`
2. 删除旧虚拟环境
3. 用新解释器重建 `.venv`
4. 重新安装依赖

典型流程：

```bash
rm -rf .venv
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

如果你的机器上 `python3.11` 不存在，先安装它，再继续。不要在错误的 Python 版本上反复重试 `pip install`。

## Node.js / npm 版本问题

文档站使用 `VitePress`。如果 Node 版本太旧，常见表现是：

- `npm install` 失败
- `npm run docs:dev` 或 `npm run docs:build` 直接退出
- 报错里出现 `Unsupported engine`、语法不支持或依赖解析失败

先确认版本：

```bash
node --version
npm --version
```

这套仓库当前推荐：

- `Node.js 20 LTS`
- 与之配套的默认 `npm`

如果你本地还是 `Node 16` 或更早版本，先升级 Node，再重新安装前端依赖。

升级后建议执行一次干净安装：

```bash
rm -rf node_modules
rm -f package-lock.json
npm install
```

只有在你明确知道自己要重新生成锁文件时，才删除 `package-lock.json`。如果你只是普通读者，本仓库默认应该优先保留提交里的锁文件，再执行：

```bash
rm -rf node_modules
npm install
```

## docs build 失败时先看什么

先执行：

```bash
npm run docs:build
```

常见原因通常只有几类。

### 1. 前端依赖没有装完整

表现：

- `vitepress: command not found`
- 构建一开始就失败

修复：

```bash
npm install
npm run docs:build
```

### 2. Node 版本不符合当前基线

表现：

- 安装过依赖，但构建时仍然报运行时语法错误
- 某些依赖加载失败

修复：

1. 升级到 `Node.js 20 LTS`
2. 删除 `node_modules`
3. 重新执行 `npm install`
4. 再跑 `npm run docs:build`

### 3. 文档链接或页面路径写错

表现：

- 构建日志里出现页面路径找不到
- 你刚新增或改名了某个 Markdown 文件后开始报错

修复思路：

1. 检查链接路径是否和真实文件名一致
2. 检查目录页是否引用了不存在的页面
3. 检查 `docs/.vitepress/config.mts` 里的导航或 sidebar 链接是否仍然有效

如果你刚改过文件名，最容易漏的是：

- Markdown 内部链接还指向旧路径
- sidebar 仍然引用旧页面
- 目录页新增了入口，但文件还没创建

### 4. 构建缓存或旧依赖残留

表现：

- 你没有改构建相关文件，但本地突然开始失败
- 同事能构建，你本地不行

可以先做一次最小清理：

```bash
rm -rf node_modules docs/.vitepress/dist
npm install
npm run docs:build
```

如果还是失败，再回头看 Node 版本和最近改动的文档链接。

## 最稳的重新开始方式

如果你已经试了很多轮，环境越来越乱，直接按下面的顺序重置通常更快：

```bash
rm -rf .venv node_modules docs/.vitepress/dist
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
npm install
npm run docs:build
python3 examples/chapter-01/main.py
```

这套流程的目标不是“一次跑通所有章节”，而是先确认三件事：

- Python 环境能正常导入依赖
- 文档站能成功构建
- 最小示例能正常运行

只要这三件事成立，后面再进入具体章节排查会容易很多。

## 还是卡住时，优先提供什么信息

如果你准备继续提 issue 或找人协助，至少先整理下面这些信息，不然别人只能继续猜：

- 你执行的完整命令
- 完整报错文本
- `python3 --version`
- `node --version`
- `npm --version`
- 你是在仓库根目录，还是某个 `examples/chapter-*` 目录执行命令

信息越完整，越容易判断问题到底是环境、依赖、路径，还是文档本身。
