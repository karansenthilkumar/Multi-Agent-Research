
from crewai import Task, Crew
from app.agents.planner import create_planner
from app.agents.researcher import create_researcher
from app.agents.summarizer import create_summarizer
from app.agents.critic import create_critic

def run_crew(query):

    planner = create_planner()
    researcher = create_researcher()
    summarizer = create_summarizer()
    critic = create_critic()

    plan_task = Task(
        description=f"Break down: {query}",
        agent=planner
    )

    research_task = Task(
        description="Search and gather info",
        agent=researcher
    )

    summary_task = Task(
        description="Summarize findings",
        agent=summarizer
    )

    critique_task = Task(
        description="Improve final output",
        agent=critic
    )

    crew = Crew(
        agents=[planner, researcher, summarizer, critic],
        tasks=[plan_task, research_task, summary_task, critique_task],
        verbose=True
    )

    return crew.kickoff() 

