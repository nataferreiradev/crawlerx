from fastapi import FastAPI
from crawler_x.api.routes.routes import router as api_router

app = FastAPI(
    title="Projeto X API",
    description="APIs para orquestração de serviços do Projeto X",
    version="0.1.0"
)

app.include_router(api_router, prefix="/v1")
