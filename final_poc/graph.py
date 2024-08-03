from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated, List
from nodes import *
from tools import *
from langgraph.checkpoint.sqlite import SqliteSaver
from dotenv import load_dotenv

load_dotenv()

memory = SqliteSaver.from_conn_string(":memory:")

# graph instance
builder = StateGraph(AgentState)

builder.add_node("planner", plan_node)
builder.add_node("generate", generation_node)
builder.add_node("reflect", reflection_node)
builder.add_node("research_plan", research_plan_node)
builder.add_node("research_critique", research_critique_node)

builder.set_entry_point("planner")

builder.add_conditional_edges(
    "generate", 
    should_continue, 
    {END: END, "reflect": "reflect"}
)

builder.add_edge("planner", "research_plan")
builder.add_edge("research_plan", "generate")

builder.add_edge("reflect", "research_critique")
builder.add_edge("research_critique", "generate")

graph = builder.compile(checkpointer=memory)

thread = {"configurable": {"thread_id": "1"}}
for s in graph.stream({
    'task': "Describe the men's singles competition in tennis at the 2024 Paris Olympic games, in a total of 50 words.",
    "max_revisions": 2,
    "revision_number": 1,
}, thread):
    for key, value in s.items():
        print(f"{key}:")
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                print(f"  {sub_key}:")
                print(f"    {sub_value}")
                print()  # Add a blank line between sub-fields
        else:
            print(value)
        print()  # Add a blank line between main fields for better readability

# print(graph.get_graph().draw_mermaid())
