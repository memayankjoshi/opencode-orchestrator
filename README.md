# OpenCode Orchestrator

A lightweight, deterministic, and fiercely token-efficient Multi-Agent Orchestration Framework for [OpenCode](https://github.com/opencode-ai/opencode).

This repository isn't just a collection of dotfiles; it is a **Framework Generator**. By passing the included `BOOTSTRAP.md` to your OpenCode assistant, it will autonomously inspect your available AI models and build a completely custom, agentic software factory tailored exactly to your local environment.

## 🌟 Core Features

1. **Zero Token Wastage**: Context slicing guarantees subagents only see the files they need.
2. **Deterministic State Machine**: Execution state is stored in machine-readable `tasks.yaml` and `progress.json`, preventing infinite "AI doom loops".
3. **Google OKF Native**: Integrated with the [Open Knowledge Format (OKF)](https://okf.md/) to store research, APIs, and rules in an agent-friendly, Git-versioned knowledge graph.
4. **Fast vs. Pro Routing**: Automatically delegates easy tasks (CRUD, CSS) to cheap/fast models and complex tasks (Auth, AI, Architecture) to advanced Pro models.
5. **Auto-Escalation**: If a Fast model fails twice, the Orchestrator automatically upgrades the task to a Pro model for the third attempt.

---

## 🚀 Installation

Because you probably have different models configured than I do (e.g. OpenAI vs Anthropic vs Ollama vs Gemini), this repository uses a "Bootstrap" prompt to build the framework dynamically.

1. Clone this repository:
   ```bash
   git clone https://github.com/memayankjoshi/opencode-orchestrator.git
   cd opencode-orchestrator
   ```

2. Open OpenCode in the directory and run the Bootstrap prompt:
   ```text
   @opencode Read BOOTSTRAP.md and execute the 5 setup steps to build my orchestration framework.
   ```

OpenCode will analyze your configured models, ask you which ones to use for "Fast" vs "Pro" tasks, and build the entire `plan`, `build`, and subagent architecture directly into your global `~/.config/opencode/` directory!

---

## 🛠️ Usage

### 1. Start a Project (Plan Mode)
Navigate to a fresh directory and open OpenCode. Talk to the `plan` agent:
> *"I want to build a Python CLI tool that fetches weather data."*

The Plan agent will copy the boilerplate `.opencode/` templates into your workspace, ask clarifying questions, and generate a robust `tasks.yaml` execution queue.

### 2. Execute the Plan (Build Mode)
Once the plan is finalized, switch to the `build` agent:
> *"Start building."*

The Build agent will autonomously read the queue, spawn specialized subagents in the background, run verification commands (tests), and update `progress.json` until the project is complete.
