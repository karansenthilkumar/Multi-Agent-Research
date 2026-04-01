
from crewai import Agent
from app.config.llm_config import get_llm

def create_planner():
    return Agent(
        role="Planner",
        goal="Break complex queries into actionable steps",
        backstory="Expert strategist",
        llm=get_llm(),
        verbose=True
    ) 


