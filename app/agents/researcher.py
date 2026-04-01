
from crewai import Agent
from app.tools.web_search import search_web
from app.config.llm_config import get_llm

def create_researcher():
    return Agent(
        role="Researcher",
        goal="Find relevant information from web",
        backstory="Expert researcher",
        tools=[search_web],
        llm=get_llm(),
        verbose=True
    ) 

