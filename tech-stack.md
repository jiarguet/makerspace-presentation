# Relevant — Tech Stack Reference

> Single-pane-of-glass agentic workflow suite for Godot game development.

Versions below are the minimum versions declared in `pyproject.toml` where applicable. GitHub star counts use the supplied May 2026 research numbers; companion packages inherit the parent ecosystem's repo count where that is the meaningful public project.

## Stack Table

| Layer | Tool | Version | GitHub stars | Purpose in Relevant | Why it was chosen |
|---|---|---:|---:|---|---|
| Pipeline orchestration | LangGraph | `>=0.2` | 31.6k | Runs the story workflow graph, human approval gates, retries, and resume logic. | It is the cleanest fit for explicit DAG orchestration plus durable agent workflows. |
| Pipeline orchestration | langgraph-checkpoint-sqlite | `>=1.0` | 31.6k (LangGraph ecosystem) | Persists graph checkpoints so interrupted runs can resume exactly where they stopped. | It gives Relevant durable execution with SQLite and no extra service to operate. |
| AI personas | PydanticAI | `>=0.0.20` | 16.9k | Defines the prompt-writer, planner, executor, and tester personas with typed interfaces. | It combines strong typing, model flexibility, and clean tool/MCP integration. |
| LLM abstraction | LiteLLM | `>=1.0` | ~17k | Normalizes calls across Claude, OpenAI-compatible endpoints, and local runtimes. | It keeps model/provider switching cheap so the suite stays vendor-flexible. |
| Hosted model option | Anthropic Claude | External | N/A | Provides high-quality cloud reasoning for planning, implementation, and review. | It is the high-accuracy option when a task needs more reasoning depth than a local model. |
| Local model runtime | Ollama | External | 171k | Runs local chat and embedding models behind an OpenAI-compatible local API. | It enables private, offline-friendly, low-friction local inference. |
| Document/RAG core | llama-index-core | `>=0.11` | ~40k | Ingests design docs, epics, and repo knowledge into queryable indexes. | It is strong at document-centric retrieval workflows and fits markdown-heavy projects. |
| Document/RAG retrieval | llama-index-retrievers-bm25 | `>=0.7` | ~40k (LlamaIndex ecosystem) | Adds lexical BM25 retrieval for local-first document search. | It improves precision on exact terms, symbols, and Godot-specific vocabulary without embeddings. |
| Document ingestion | llama-index-readers-file | `>=0.2` | ~40k (LlamaIndex ecosystem) | Loads markdown and file-based sources into the document pipeline. | It is the simplest path to ingesting local design docs and repo content. |
| Ranking | rank-bm25 | `>=0.2` | N/A | Supplies the BM25 scoring implementation used for classic lexical retrieval. | It keeps retrieval fast, transparent, local, and model-free. |
| Vector + hybrid storage | LanceDB | External | ~5k | Stores vectors and hybrid-search indexes for richer RAG when needed. | It is embedded, serverless, and aligned with Relevant's local-first philosophy. |
| App state models | SQLModel | `>=0.0.21` | ~15k | Defines typed models for stories, runs, checkpoints, and project state. | It gives a Pythonic ORM/data-model layer with low ceremony on top of SQLite. |
| Local database | SQLite | External | N/A | Holds project state, workflow checkpoints, and portable local data. | It delivers durable state in a single file with zero infrastructure. |
| Terminal UI | Textual | `>=1.0` | 35.8k | Powers the operator dashboard, pipeline status views, tables, logs, and markdown panels. | It is the fastest path to a polished Python-native TUI with async support. |
| Version control | GitPython | `>=3.1` | ~4.5k | Stages, commits, and inspects repo state as part of the story workflow. | It gives first-class Git automation without shelling out for every operation. |
| File watching | Watchdog | `>=4.0` | ~6.5k | Detects changes in docs, configs, and repos so indexes and views stay fresh. | It is the standard Python choice for reliable cross-platform file events. |
| Desktop notifications | plyer | `>=2.1` | ~1.8k | Sends native desktop notifications for approvals, completions, and GTG events. | It keeps alerting local and cross-platform without standing up a notification service. |
| Config serialization | PyYAML | `>=6.0` | N/A | Parses persona files and human-editable configuration documents. | YAML is easy for humans to author and review, especially for persona specs. |
| HTTP transport | httpx | `>=0.27` | N/A | Talks to MCP servers, local model runtimes, and other HTTP endpoints. | It provides a modern sync/async HTTP client that matches the app's async architecture. |
| Async runtime | anyio | `>=4.0` | N/A | Provides async compatibility primitives used across the orchestration stack. | It keeps concurrency portable and clean across the Python async ecosystem. |
| Game-engine bridge | Godot MCP Pro | Custom/commercial | N/A | Gives agents structured access to the Godot editor, scene tree, scripts, tests, and runtime. | It turns Godot into a tool-usable environment instead of a black-box external app. |
| AI harness | GitHub Copilot CLI | External/commercial | N/A | Serves as the current harness that invokes coding agents and toolchains from Relevant workflows. | It is a practical operator-facing AI execution surface today, and it remains swappable later. |

## Layered List View

### 1. Pipeline orchestration
- **LangGraph** (`>=0.2`, 31.6k) — the workflow backbone. It maps naturally to Relevant's stage-based story DAG, human checkpoints, and restart-safe execution.
- **langgraph-checkpoint-sqlite** (`>=1.0`, LangGraph ecosystem) — the checkpoint layer. It keeps runs resumable with a local SQLite file instead of a hosted workflow backend.

### 2. AI personas and model routing
- **PydanticAI** (`>=0.0.20`, 16.9k) — the persona layer for prompt-writer, planner, executor, and tester. It was chosen for typed agent outputs, tool/MCP friendliness, and clean composition with LangGraph.
- **LiteLLM** (`>=1.0`, ~17k) — the model abstraction layer. It was chosen so Relevant can switch providers with config changes instead of code rewrites.
- **Anthropic Claude** (external, N/A) — the premium hosted model path. It was chosen for strong reasoning quality on higher-stakes planning and coding tasks.
- **Ollama** (external, 171k) — the local model path. It was chosen because it makes private local inference easy and standardizes access through a familiar API.

### 3. RAG and document layer
- **llama-index-core** (`>=0.11`, ~40k) — the document indexing/query foundation for design docs, epics, and repo knowledge. It was chosen because it is especially good at document-heavy RAG flows.
- **llama-index-retrievers-bm25** (`>=0.7`, LlamaIndex ecosystem) — lexical retrieval on top of the RAG layer. It was chosen for exact-term and symbol-sensitive search.
- **llama-index-readers-file** (`>=0.2`, LlamaIndex ecosystem) — local file ingestion. It was chosen because Relevant's source of truth is mostly markdown and repo files.
- **rank-bm25** (`>=0.2`, N/A) — the BM25 ranking primitive. It was chosen to keep retrieval local, cheap, and interpretable.
- **LanceDB** (external, ~5k) — the embedded vector/hybrid store. It was chosen because it brings richer retrieval without introducing a separate server tier.

### 4. State and storage
- **SQLModel** (`>=0.0.21`, ~15k) — typed persistence models for stories, runs, and workflow metadata. It was chosen for the balance of Pydantic ergonomics and SQLAlchemy power.
- **SQLite** (external, N/A) — the single-file local database. It was chosen because local durability and portability are central to the product.

### 5. Operator interface
- **Textual** (`>=1.0`, 35.8k) — the TUI shell for operators. It was chosen because it gives a polished Python-native dashboard without splitting the stack across languages.

### 6. Repo, file, and notification integration
- **GitPython** (`>=3.1`, ~4.5k) — repo automation. It was chosen so Relevant can enforce commit-aware workflows as stories move forward.
- **Watchdog** (`>=4.0`, ~6.5k) — file event monitoring. It was chosen to keep local docs and indexes in sync automatically.
- **plyer** (`>=2.1`, ~1.8k) — native notifications. It was chosen because it keeps GTG and review notifications local and cross-platform.
- **PyYAML** (`>=6.0`, N/A) — config and persona parsing. It was chosen because YAML is easy for humans to read and edit.

### 7. Transport and concurrency
- **httpx** (`>=0.27`, N/A) — the HTTP client layer. It was chosen for modern sync/async ergonomics when talking to MCP servers and model endpoints.
- **anyio** (`>=4.0`, N/A) — async portability primitives. It was chosen because the stack is async-heavy and benefits from a clean concurrency foundation.

### 8. Game-engine and harness layer
- **Godot MCP Pro** (custom/commercial, N/A) — the bridge into Godot editor/runtime operations. It was chosen because it gives agents deep, structured control over the game project.
- **GitHub Copilot CLI** (external/commercial, N/A) — the current AI harness. It was chosen because it provides a usable agent-execution shell today while still being replaceable through configuration.

## Why local-first?

Relevant is intentionally designed to be **local-first**:

- **Single-file state** — SQLite keeps workflow state, checkpoints, and project metadata portable and easy to back up.
- **Embedded retrieval** — BM25 and LanceDB avoid the cost and operational drag of a separate search cluster.
- **Optional local models** — Ollama allows private inference for design docs, code context, and testing workflows.
- **Repo-native workflow** — GitPython, Watchdog, and local file readers operate directly on the developer's real workspace.
- **Fewer moving parts** — no mandatory always-on backend, queue, or vector service means less failure surface for solo and small-team development.
- **Swappable cloud assist** — cloud models like Claude can be added where quality matters, but they are not required for the architecture to function.

That combination makes Relevant faster to adopt, cheaper to run, easier to reason about, and more privacy-friendly for game teams working with in-progress design and code assets.
