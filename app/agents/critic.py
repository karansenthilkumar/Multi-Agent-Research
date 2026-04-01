
from crewai import Agent
from app.config.llm_config import get_llm

def create_critic():
    return Agent(
        role="Critic",
        goal="Improve answer quality and correctness",
        backstory="Strict reviewer",
        llm=get_llm(),
        verbose=True
    ) 

