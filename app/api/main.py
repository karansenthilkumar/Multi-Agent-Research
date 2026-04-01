
from fastapi import FastAPI
from pydantic import BaseModel
from app.workflows.langgraph_workflow import run_langgraph
from app.utils.logger import logger

app = FastAPI(title="Multi-Agent Research API")

class Query(BaseModel):
    question: str

@app.get("/")
def health():
    return {"status": "running"}

@app.post("/research")
def research(q: Query):
    logger.info(f"Query: {q.question}")

    result = run_langgraph(q.question)

    logger.info("Response generated")

    return {"result": result["final"]} 

