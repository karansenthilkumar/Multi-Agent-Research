
from langgraph.graph import StateGraph
from typing import TypedDict
from app.agents.planner import create_planner
from app.agents.researcher import create_researcher
from app.agents.summarizer import create_summarizer
from app.agents.critic import create_critic
from app.memory.memory import ConversationMemory

memory = ConversationMemory()

class AgentState(TypedDict):
    query: str
    plan: str
    research: str
    summary: str
    final: str


def planner_node(state: AgentState):
    agent = create_planner()
    result = agent.run(state["query"])
    return {"plan": result}


def researcher_node(state: AgentState):
    agent = create_researcher()
    result = agent.run(state["plan"])
    return {"research": result}


def summarizer_node(state: AgentState):
    agent = create_summarizer()
    result = agent.run(state["research"])
    return {"summary": result}


def critic_node(state: AgentState):
    agent = create_critic()
    result = agent.run(state["summary"])

    memory.add(state["query"], result)

    return {"final": result}


def build_graph():

    builder = StateGraph(AgentState)

    builder.add_node("planner", planner_node)
    builder.add_node("researcher", researcher_node)
    builder.add_node("summarizer", summarizer_node)
    builder.add_node("critic", critic_node)

    builder.set_entry_point("planner")

    builder.add_edge("planner", "researcher")
    builder.add_edge("researcher", "summarizer")
    builder.add_edge("summarizer", "critic")

    return builder.compile()


graph = build_graph()


def run_langgraph(query: str):
    return graph.invoke({"query": query}) 

