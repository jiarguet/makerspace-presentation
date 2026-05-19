from langgraph.graph import END, StateGraph

from relevant.pipeline import steps
from relevant.pipeline.state import StoryState


def build_graph(checkpointer):
    graph = StateGraph(StoryState)  # Typed state shared by every DAG node

    # AI work nodes — each node transforms StoryState and hands it to the next step.
    graph.add_node("prompt_gen", steps.run_prompt_gen)      # DAG node: draft the implementation prompt
    graph.add_node("plan_gen", steps.run_plan_gen)          # DAG node: turn prompt into a coding plan
    graph.add_node("execute", steps.run_execute)            # DAG node: implement the feature
    graph.add_node("commit", steps.run_commit)              # DAG node: persist work to Git
    graph.add_node("test_gen", steps.run_test_gen)          # DAG node: generate / run tests
    graph.add_node("review_queue", steps.run_review_queue)  # DAG node: prepare review context
    graph.add_node("close", steps.run_close)                # DAG node: mark story complete

    # Human gates — LangGraph pauses before these nodes so a person can review the output.
    graph.add_node("prompt_approval", steps.human_gate)     # human gate — pipeline pauses here
    graph.add_node("plan_approval", steps.human_gate)       # human gate — approve the plan
    graph.add_node("review_gate", steps.human_gate)         # human gate — close or loop for fixes

    graph.set_entry_point("prompt_gen")
    graph.add_edge("prompt_gen", "prompt_approval")
    graph.add_edge("prompt_approval", "plan_gen")
    graph.add_edge("plan_gen", "plan_approval")
    graph.add_edge("plan_approval", "execute")

    graph.add_conditional_edges(
        "execute",
        lambda state: "end" if state["stage"] == "error" else "commit",  # short-circuit on failure
        {"end": END, "commit": "commit"},
    )
    graph.add_edge("commit", "test_gen")
    graph.add_edge("test_gen", "review_queue")
    graph.add_edge("review_queue", "review_gate")
    graph.add_conditional_edges("review_gate", steps.after_review_gate, {"close": "close", "execute": "execute"})
    graph.add_edge("close", END)

    return graph.compile(
        checkpointer=checkpointer,  # durable checkpoint — resume after restart or manual approval
        interrupt_before=["prompt_approval", "plan_approval", "review_gate"],
    )
