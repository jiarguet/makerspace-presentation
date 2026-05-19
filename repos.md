# Relevant — Repos and External Tools Reference

This page lists both core open-source dependencies and optional operational integrations used around Relevant. GitHub star counts reflect the supplied May 2026 research where available; items without a public OSS repo or without a supplied count are marked `N/A`.

## Pipeline Orchestration

| Repo name | GitHub URL | License | Stars | Role in Relevant | What it does |
|---|---|---|---:|---|---|
| LangGraph | https://github.com/langchain-ai/langgraph | MIT | 31.6k | Orchestrates the end-to-end story pipeline, approval gates, loops, and resumable execution. | Framework for stateful agent graphs with durable checkpoints and human-in-the-loop control. |

## AI Personas & LLM

| Repo name | GitHub URL | License | Stars | Role in Relevant | What it does |
|---|---|---|---:|---|---|
| PydanticAI | https://github.com/pydantic/pydantic-ai | MIT | 16.9k | Defines typed AI personas such as planner, executor, and tester. | Agent framework for structured outputs, tools, and multi-provider model usage. |
| LiteLLM | https://github.com/BerriAI/litellm | MIT | ~17k | Normalizes model access so Relevant can switch between hosted and local providers. | OpenAI-style abstraction layer across many LLM vendors and runtimes. |
| Anthropic Claude | N/A (commercial service) | Proprietary service | N/A | Optional hosted reasoning model for planning, coding, and review when cloud quality is preferred. | Claude is Anthropic's family of frontier LLMs used when maximum reasoning quality is desired. |
| Ollama | https://github.com/ollama/ollama | MIT | 171k | Local model runtime for private inference and embeddings. | Runs local LLMs behind a simple OpenAI-compatible HTTP API. |

## RAG & Document Layer

| Repo name | GitHub URL | License | Stars | Role in Relevant | What it does |
|---|---|---|---:|---|---|
| LlamaIndex | https://github.com/run-llama/llama_index | MIT | ~40k | Ingests and retrieves design docs, epics, and repo knowledge for agent context. | Data framework for loaders, indexes, retrievers, and agent-oriented query flows. |
| rank-bm25 | https://github.com/dorianbrown/rank_bm25 | Apache-2.0 | N/A | Supplies lexical ranking for local-first search over markdown and repo text. | Lightweight Python implementation of the BM25 ranking algorithm. |
| LanceDB | https://github.com/lancedb/lancedb | Apache-2.0 | ~5k | Stores vectors and hybrid-search indexes without a separate service. | Embedded vector database optimized for local development workflows. |

## TUI / UI

| Repo name | GitHub URL | License | Stars | Role in Relevant | What it does |
|---|---|---|---:|---|---|
| Textual | https://github.com/Textualize/textual | MIT | 35.8k | Powers the single-pane-of-glass operator dashboard in the terminal. | Python TUI framework for rich, async terminal applications with modern widgets. |

## Storage & State

| Repo name | GitHub URL | License | Stars | Role in Relevant | What it does |
|---|---|---|---:|---|---|
| SQLModel | https://github.com/fastapi/sqlmodel | MIT | ~15k | Defines typed models for stories, runs, checkpoints, and project metadata. | ORM/data-model layer that blends Pydantic-style models with SQLAlchemy. |
| SQLite | https://github.com/sqlite/sqlite | Public domain | N/A | Stores local application state and durable workflow data in a single file. | Embedded relational database designed to run without a separate server process. |
| langgraph-checkpoint-sqlite | https://github.com/langchain-ai/langgraph | MIT | 31.6k (LangGraph ecosystem) | Persists LangGraph checkpoints so workflows can pause and resume safely. | SQLite-backed checkpoint adapter for LangGraph durable execution. |

## Version Control

| Repo name | GitHub URL | License | Stars | Role in Relevant | What it does |
|---|---|---|---:|---|---|
| GitPython | https://github.com/gitpython-developers/GitPython | BSD | ~4.5k | Automates repo inspection, staging, and commit-aware workflow steps. | Python library for interacting with Git repositories programmatically. |

## Tooling

| Repo name | GitHub URL | License | Stars | Role in Relevant | What it does |
|---|---|---|---:|---|---|
| Watchdog | https://github.com/gorakhargosh/watchdog | Apache-2.0 | ~6.5k | Watches files and folders so Relevant can react to doc and repo changes. | Cross-platform filesystem event library for Python. |
| plyer | https://github.com/kivy/plyer | MIT | ~1.8k | Sends native desktop notifications for approvals, GTG events, and completed runs. | Cross-platform wrapper around native device and desktop features. |
| httpx | https://github.com/encode/httpx | BSD-3-Clause | N/A | Handles HTTP communication with MCP servers, model endpoints, and related services. | Modern Python HTTP client with both sync and async APIs. |
| anyio | https://github.com/agronholm/anyio | MIT | N/A | Provides concurrency primitives across the async-heavy workflow stack. | High-level compatibility layer for asynchronous I/O in Python. |
| PyYAML | https://github.com/yaml/pyyaml | MIT | N/A | Parses persona specs and human-authored configuration files. | YAML parser and emitter for Python applications. |

## Game Engine Integration

| Repo name | GitHub URL | License | Stars | Role in Relevant | What it does |
|---|---|---|---:|---|---|
| Godot 4 | https://github.com/godotengine/godot | MIT | N/A | The target engine that Relevant plans, edits, tests, and reviews against. | Open-source game engine used to build the actual project under automation. |
| Godot MCP Pro | N/A (custom/commercial MCP server) | Commercial / custom | N/A | Optional engine integration that gives agents structured access to the Godot editor and running game. | MCP server that exposes Godot scenes, scripts, tests, and runtime state as callable tools. |

## AI Harness

| Repo name | GitHub URL | License | Stars | Role in Relevant | What it does |
|---|---|---|---:|---|---|
| GitHub Copilot CLI | https://github.com/features/copilot | Closed source | N/A | Current execution harness for invoking AI coding agents from the workflow suite. | GitHub's CLI-facing Copilot product used here as the operator-accessible agent harness. |

> All core dependencies are open source. The only closed-source component is GitHub Copilot (the AI harness) — this is swappable via the `harness` config field.
