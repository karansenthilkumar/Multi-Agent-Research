
from crewai import Agent
from app.config.llm_config import get_llm

def create_summarizer():
    return Agent(
        role="Summarizer",
        goal="Summarize research into concise insights",
        backstory="Expert writer",
        llm=get_llm(),
        verbose=True
    ) 

