# OpenCode Solo Orchestrator

A lightweight, deterministic, and fiercely token-efficient Multi-Agent Orchestration Framework for [OpenCode](https://github.com/opencode-ai/opencode).

This framework transforms OpenCode from a standard coding assistant into a fully autonomous software factory tailored for **solo developers**. It separates the "thinking" (Planning) from the "doing" (Building) and uses specialized subagents to execute tasks efficiently without bloating the LLM context window.

## 🌟 Core Features

1. **Zero Token Wastage**: Context slicing guarantees subagents only see the files they need.
2. **Deterministic State Machine**: Execution state is stored in machine-readable `tasks.yaml` and `progress.json`, preventing infinite "AI doom loops".
3. **Google OKF Native**: Integrated with the [Open Knowledge Format (OKF)](https://okf.md/) to store research, APIs, and rules in an agent-friendly, Git-versioned knowledge graph.
4. **Fast vs. Pro Routing**: Automatically delegates easy tasks (CRUD, CSS) to cheap/fast models and complex tasks (Auth, AI, Architecture) to advanced Pro models.
5. **Auto-Escalation**: If a Fast model fails twice, the Orchestrator automatically upgrades the task to a Pro model for the third attempt.

## 🏗️ Architecture

### 1. Primary Agents (The Managers)
* **`plan`**: The Architect. Locks down requirements, researches unknown APIs (saving them as OKF files), designs the architecture, and breaks the project down into a YAML execution plan with Test-Driven Development (TDD) mandates.
* **`build`**: The Orchestrator. Reads the YAML queue, spawns the correct subagent, verifies the output, escalates failures, and updates local state. **It never writes production code itself.**

### 2. Specialized Subagents (The Workers)
* **`research`**: The Scout. Uses MCPs (Context7, DuckDuckGo) to fetch documentation and writes OKF-compliant markdown.
* **`backend-pro` / `frontend-pro`**: Heavy-duty engineers for complex logic, state management, and architecture.
* **`backend-fast` / `frontend-fast`**: Lightning-fast engineers for basic components, tests, CRUD, and styling.

---

## 🚀 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/opencode-solo-orchestrator.git
   ```
2. Copy the framework into your global OpenCode config directory:
   ```bash
   cp -r opencode-solo-orchestrator/agents ~/.config/opencode/
   cp -r opencode-solo-orchestrator/templates ~/.config/opencode/
   ```
3. Update your `~/.config/opencode/opencode.json` to enable context injection and compaction:
   ```json
   {
     "compaction": { "auto": true, "tail_turns": 10 },
     "instructions": [
       ".opencode/tasks.yaml",
       ".opencode/progress.json",
       ".opencode/session.json"
     ]
   }
   ```

## 🛠️ Usage

### 1. Start a Project (Plan Mode)
Navigate to a fresh directory and open OpenCode. Talk to the `plan` agent:
> *"I want to build a Python CLI tool that fetches weather data."*

The Plan agent will copy the boilerplate `.opencode/` templates into your workspace, ask clarifying questions, and generate a robust `tasks.yaml` execution queue.

### 2. Execute the Plan (Build Mode)
Once the plan is finalized, switch to the `build` agent:
> *"Start building."*

The Build agent will autonomously read the queue, spawn specialized subagents in the background, run verification commands (tests), and update `progress.json` until the project is complete.

## 🎛️ Customization

You can swap out the AI models by editing the frontmatter in the `~/.config/opencode/agents/*.md` files.

By default, this framework is tuned for:
* **Primary / Research Agents**: `google/antigravity-gemini-3.1-pro`
* **Pro Subagents**: `opencode-go/deepseek-v4-pro`
* **Fast Subagents**: `opencode-go/deepseek-v4-flash`
