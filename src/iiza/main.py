from fastapi import FastAPI

from iiza.router import agent, liveness_probe

api = FastAPI()

api.include_router(liveness_probe.router)
api.include_router(agent.router)
