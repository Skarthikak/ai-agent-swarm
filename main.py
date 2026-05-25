from fastapi import FastAPI
from pydantic import BaseModel
from agents import run_swarm

app = FastAPI()

class AgentRequest(BaseModel):
    prompt: str

@app.post("/trigger")
async def trigger_agent(request: AgentRequest):
    # This runs the swarm in the cloud!
    result = run_swarm(request.prompt)
    return {"status": "success", "response": str(result)}
