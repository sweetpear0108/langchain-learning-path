# 示例代码总览

每一章都对应一个最小可运行示例，统一放在仓库根目录的 `examples/` 下。

<div class="landing-hero">
  <div class="landing-hero-copy">
    <p class="landing-kicker">Example Index</p>
    <h2>先看示例怎么跑，再回章节里理解为什么这样写。</h2>
    <p class="landing-lead">
      这里的示例不是独立 Demo 集合，而是对应章节的最小可运行版本。它们和正文一起组成“先读，再跑，再改”的学习回路。
    </p>
    <div class="landing-metrics">
      <div>
        <span>组织方式</span>
        <strong>按章节一一对应</strong>
      </div>
      <div>
        <span>目标</span>
        <strong>最小可运行</strong>
      </div>
      <div>
        <span>默认入口</span>
        <strong>`python3 main.py`</strong>
      </div>
    </div>
    <div class="landing-summary">
      <div class="landing-summary-item">先确认章节对应的目录。</div>
      <div class="landing-summary-item">再看是否需要安装独立依赖。</div>
      <div class="landing-summary-item">最后动手改一处再重跑一次。</div>
    </div>
  </div>
</div>

## 通用运行方式

<div class="landing-grid">
  <section class="landing-panel">
    <span class="landing-card-kicker">纯标准库</span>
    <h3>第 1 章示例</h3>
    <p>直接进入章节目录运行即可，不需要额外安装依赖。</p>
    <pre><code>cd examples/chapter-01
python3 main.py</code></pre>
  </section>
  <section class="landing-panel">
    <span class="landing-card-kicker">共享环境</span>
    <h3>连续跑多个章节</h3>
    <p>如果你想连续跑 LangChain 章节，先准备一个统一的虚拟环境。</p>
    <pre><code>python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt</code></pre>
  </section>
  <section class="landing-panel">
    <span class="landing-card-kicker">单章依赖</span>
    <h3>按章节安装</h3>
    <p>如果只跑单章，就使用章节目录里的 `requirements.txt`。</p>
    <pre><code>cd examples/chapter-03
pip install -r requirements.txt
python3 main.py</code></pre>
  </section>
</div>

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

<div class="landing-stack">
  <div class="landing-step">
    <span class="landing-step-index">01</span>
    <div>
      <h3>先读正文</h3>
      <p>先看对应章节，再跑示例，不然只会记住表面 API。</p>
    </div>
  </div>
  <div class="landing-step">
    <span class="landing-step-index">02</span>
    <div>
      <h3>再改一处</h3>
      <p>不要只跑通一次，改一个小地方再运行一次，才能看出边界。</p>
    </div>
  </div>
  <div class="landing-step">
    <span class="landing-step-index">03</span>
    <div>
      <h3>最后回主线</h3>
      <p>如果示例带依赖或链路变复杂，优先回到主项目页和章节页定位上下文。</p>
    </div>
  </div>
</div>

<div class="landing-chip-list">
  <a href="../chapters/">章节目录</a>
  <a href="../project/">主项目</a>
  <a href="../guide/roadmap">学习路线图</a>
  <a href="../faq/troubleshooting">故障排查</a>
</div>

<p class="landing-note">
  移动端下，代码块会自动横向滚动，示例页的主要信息仍然先放在上方的块结构里，避免用户在表格和长命令之间来回扫视。
</p>
