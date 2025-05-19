from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from crawler_x.api.routes.routes import router as api_router

app = FastAPI(
    title="Projeto X API",
    description="APIs para orquestração de serviços do Projeto X",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/v1")
