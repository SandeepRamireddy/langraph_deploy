# src/langgraph_deployment/agent.py

from langgraph.graph import StateGraph, START
from langgraph.prebuilt import tools_condition
from .state import State
from .nodes import chatbot, tool_node


def get_agent():
    """Build and return the compiled LangGraph agent."""
    graph_builder = StateGraph(State)

    # Add nodes
    graph_builder.add_node("chatbot", chatbot)
    graph_builder.add_node("tools", tool_node)

    # Add conditional edges
    graph_builder.add_conditional_edges("chatbot", tools_condition)

    # Add normal edges
    graph_builder.add_edge("tools", "chatbot")
    graph_builder.add_edge(START, "chatbot")

    return graph_builder.compile()
