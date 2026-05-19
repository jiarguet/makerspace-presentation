## 1. Title — Relevant — Agentic Workflow Suite

- Godot game development, automated.
- Relevant is a single-pane-of-glass workflow suite for story-driven game development.
- It connects design docs, planning, coding, testing, and review into one pipeline.
- The goal is less coordination work and more shipped stories.

**Visual:** Text-only title slide with product name, subtitle, and a small workflow tagline: "Design doc → story → prompt → plan → execute → test → review."

**Speaker note:** Built by @jiarguet. In one sentence: Relevant is a local-first agentic workflow system that turns approved Godot stories into code, tests, and review-ready work with minimal manual coordination.

## 2. The Problem

- Today the workflow is a chain of manual handoffs: design doc → coding task → implementation → tests → review.
- Every handoff forces context switching between tools, files, and mental models.
- The human keeps retranslating the same story for different steps.
- Review often starts with: "Wait, what did this story actually want again?"
- Coordination overhead grows faster than the actual coding work.

**Visual:** Simple pain-point text layout with five boxes in sequence: design doc, task, code, tests, review; add red callouts for "manual translation," "context switching," and "forgotten intent."

**Speaker note:** Emphasize that the pain is not just writing code — it is repeatedly reloading context and rewriting intent at every stage.

## 3. The Vision

- Relevant follows a "fire and return" philosophy.
- The human writes a story YAML once, approves the generated prompt, and leaves the pipeline to run.
- When they return, they see a review queue instead of a blank slate.
- Human time shifts from orchestration to decision-making.
- The system is designed to make progress while the developer is away.

**Visual:** Before/after comparison. Left: human spends time on planning, translating, checking, and re-explaining. Right: human spends time on story authoring, prompt approval, and review queue.

**Speaker note:** The value proposition is not "AI writes code." It is "the workflow keeps moving without me babysitting every step."

## 4. System Architecture

- Four layers: UI → Pipeline Engine → Personas → Data/Resources.
- The UI is replaceable; the workflow logic lives below it.
- LangGraph orchestrates the pipeline, personas do the work, and the resource layer supplies context.
- Data stays local-first: local config, local repo, local SQLite, local file watching.
- This makes the system portable, inspectable, and practical for solo or small-team development.

**Visual:** Use `diagrams/exported/system-architecture.png`. Add a small caption: "UI on top, pipeline in the middle, personas as workers, local resources underneath."

**Speaker note:** The key architectural point is separation of concerns: presentation can change, but the workflow engine and local data model stay stable.

## 5. The Pipeline

- Each story moves through a named sequence of stages.
- The stages are: prompt_gen → prompt_approval → plan_gen → plan_approval → execute → commit → test_gen → review_queue → close.
- Every stage has a concrete artifact or decision attached to it.
- The pipeline turns vague work into durable outputs: prompt.md, plan.md, code, commit, tests, review items.
- Because the stages are explicit, the workflow is resumable and debuggable.

**Visual:** Use `diagrams/exported/pipeline-flow.png`. Label each node with its main artifact: prompt, approved prompt, plan, code, commit, tests, review.

**Speaker note:** Walk left to right. Stress that the pipeline is not magic — it is a visible sequence with checkpoints, outputs, and status at every step.

## 6. Human-in-the-Loop Gates

- The system is intentionally human-guided, not human-free.
- GTG means two things: a human approved the story, and all story dependencies are closed.
- The key required gate is prompt approval: verify the system understood the story before it spends time coding.
- After that, the pipeline is meant to run autonomously until it produces reviewable output.
- Review happens at the end as a queue, not as constant synchronous interruption.

**Visual:** Use `diagrams/exported/gtg-logic.png`. Highlight the rule: "GTG = human approved AND deps closed." Add a bold callout: "One mandatory gate: prompt approval."

**Speaker note:** This is the trust boundary. Approve intent once, then let the system execute. The whole product depends on getting this boundary right.

## 7. The Four Roles / Personas

- PromptWriter: design docs + epics + skills → `prompt.md`.
- Planner: repo context + skills → `plan.md` aligned to the real codebase.
- Executor: approved plan → code changes and commit using Godot MCP tools.
- Tester: acceptance criteria → test files → pass/fail signal and review checklist.
- Each role is YAML-defined, model-specific, and replaceable without changing the whole system.

**Visual:** Use `diagrams/exported/rag-context.png` or a four-column persona card layout showing input, output, and tools for each role.

**Speaker note:** Present these as specialized workers, not one giant general-purpose agent. The win is role clarity and configurable responsibility boundaries.

## 8. Godot MCP Integration

- The Executor role works directly inside the Godot editor through Godot MCP Pro.
- That means scene edits, script creation, verification, and screenshots can all happen without human clicking.
- Relevant is not only generating text plans; it can drive concrete editor actions.
- Example MCP capabilities include node creation, script creation, scene running, and screenshot capture.
- This is what makes the workflow feel like a build system for game features, not just a chat wrapper.

**Visual:** Show a code snippet from `snippets/executor-persona.yaml`, plus a short side list of MCP actions such as `add_node`, `create_script`, `play_scene`, and `get_game_screenshot`.

**Speaker note:** This is the slide where the audience should realize the executor is acting on the actual Godot project, not merely proposing changes in abstract.

## 9. RAG & Context Layer

- Relevant uses LlamaIndex with BM25 retrieval for local, explainable context lookup.
- Obsidian docs, skill markdown, and the game repo are registered in one resource store.
- Personas query only the context they need instead of loading the whole world every time.
- Watchdog monitors file changes and re-indexes automatically.
- The result is fresher context, smaller prompts, and better story fidelity.

**Visual:** Reference `diagrams/exported/rag-context.png` and pair it with a resource store config snippet from `project.toml` showing design docs, epics, skills, and game repo entries.

**Speaker note:** The important idea is scoped retrieval. Good workflow automation depends on giving each stage the right context, not the most context.

## 10. Technology Stack

- Orchestration: LangGraph.
- Personas: PydanticAI + LiteLLM.
- RAG: LlamaIndex + BM25.
- Storage and workflow state: SQLite + SQLModel.
- UI and operations: Textual, GitPython, plyer, and Watchdog.

**Visual:** Table sourced from `tech-stack.md` with columns: layer, tool, and why it fits a local-first workflow suite.

**Speaker note:** Keep this practical. Every tool exists to support one workflow property: durable execution, swappable models, local context, portable state, or low-friction operator UX.

## 11. Key Repos Used

- LangGraph (31.6k ⭐): pipeline graph and durable execution.
- PydanticAI (16.9k ⭐): persona framework and model abstraction.
- Textual (35.8k ⭐): fast Python-native dashboard.
- Godot MCP Pro (custom): direct editor automation.
- The stack is intentionally MIT-heavy, Python-heavy, and local-first.

**Visual:** Repository summary table sourced from `repos.md` with columns for repo, stars, license, language, and why it matters to Relevant.

**Speaker note:** This slide reassures developers that the system is assembled from understandable building blocks, not opaque proprietary infrastructure.

## 12. Configuration

- Everything is file-based: TOML for project wiring, YAML for personas and work items.
- Each role configures its own persona, model, harness command, and MCP servers.
- Changing providers is low-friction: swap Claude, GPT, or Ollama with one line.
- The configuration is portable with the project, not hidden in a remote service.
- This keeps the suite scriptable, reviewable, and versionable.

**Visual:** Show `snippets/project-config.toml` with highlighted sections for `[project]`, resource store entries, and role-specific config.

**Speaker note:** Configuration is part of the product design here. If the workflow is not easy to inspect and edit, developers will not trust it.

## 13. Pipeline in Code

- The pipeline is implemented as a LangGraph `StateGraph`.
- Nodes map directly to workflow stages, which keeps the code legible.
- `interrupt_before` marks human gate points.
- `SqliteSaver` provides durable checkpointing so runs survive restarts.
- The shared story state carries artifacts, flags, and review data across the graph.

**Visual:** Show short snippets from `snippets/pipeline-graph.py` and `snippets/story-state.py`, with callouts on nodes, edges, interrupts, and checkpointing.

**Speaker note:** This is the "under the hood" slide for technical audiences. Show that the workflow is encoded as an explicit graph, not buried in ad hoc control flow.

## 14. TUI Dashboard (Bonus)

- The TUI gives one place to monitor the board, pipeline runs, and review queue.
- Dashboard, Pipeline, and Review tabs are the most demo-friendly surfaces.
- The visual style is Marathon-inspired: retro-futurist military terminal.
- But the TUI is the smallest part of the system.
- The pipeline still matters even without any dashboard at all.

**Visual:** Use `screenshots/dashboard.png`, `screenshots/pipeline.png`, and `screenshots/review.png`. Add a caption: "Operator console, not the core product." Optionally include `screenshots/agents.png` for the agent role config panel.

**Speaker note:** Frame this as a bonus demo. The audience should leave remembering the workflow engine and toolchain, not just the terminal aesthetic.

## 15. What's Next

- Phase 0 Scaffold ✅.
- Next: Phase 1 Core Pipeline, Phase 2 RAG, Phase 3 Personas, Phase 4 TUI, Phase 5 Polish, and Phase 6 Tauri Desktop App.
- The roadmap moves from workflow correctness first to UI polish second.
- The long-term direction is the same pipeline with a richer desktop shell.
- The near-term goal is proving that story-in, review-out can run reliably end to end.

**Visual:** Simple roadmap timeline with the seven phases, showing the first as complete and later phases as progressive capability layers.

**Speaker note:** End on momentum. The headline is that the workflow architecture comes first; the UI can evolve once the pipeline is dependable.