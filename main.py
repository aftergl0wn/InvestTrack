from fastapi import FastAPI

from routing.health import router_health

app = FastAPI()
app.include_router(router_health)
