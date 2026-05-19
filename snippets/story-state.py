# StoryState is the durable state envelope that flows through Relevant's LangGraph pipeline.
# Each node reads and updates this shared dict, and checkpointing lets the workflow pause
# for human approval and resume later without losing context.

from typing_extensions import TypedDict

from relevant.pipeline.state import PipelineStage


class StoryState(TypedDict):
    stage: PipelineStage         # Current pipeline node (prompt_gen, execute, review_gate, ...)
    gtg: bool                    # "Green to go": human approved and all dependencies are closed
    human_interrupted: bool      # True when the graph is paused at a human approval gate

    generated_prompt: str | None # AI-generated implementation prompt for the coding workflow
    generated_plan: str | None   # AI-generated coding plan derived from the approved prompt

    commit_sha: str | None       # Git commit produced by the executor step
