# Contributing

本仓库当前先约束最小的一致性检查，目标是让文档、示例和 CI 保持同一套风格基线。

## 推荐本地流程

1. 创建并激活 Python 虚拟环境。
2. 安装 Python 依赖：`python -m pip install -r requirements-dev.txt`
3. 安装 Node 依赖：`npm install`
4. 提交前运行：`npm run lint`

如果你修改了示例代码或文档构建相关内容，再补一轮：

- `npm run ci:docs`
- `npm run ci:examples`

## 当前最小规范

- Python 使用 `ruff check` 做静态检查，使用 `ruff format` 保持统一格式。
- Markdown 使用 `markdownlint-cli2` 做基础格式检查。
- 新增 Python 文件时，默认兼容 `Python 3.11`。
- 新增文档时，保持标题层级清晰，列表和代码块尽量采用一致写法。

## 常用命令

- `npm run lint`：同时检查 Markdown 和 Python。
- `npm run format`：自动修复 Python import 顺序和格式问题。
- `npm run ci:check`：执行 lint、文档构建和示例 smoke test。
