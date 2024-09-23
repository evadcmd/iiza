from fastapi import FastAPI

from iiza.router import agent, liveness_probe

api = FastAPI(title="a chatbot API using mrkl algorithm")

api.include_router(liveness_probe.router)
api.include_router(agent.router)
