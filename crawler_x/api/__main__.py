from crawler_x.api.main import app
import asyncio
from fastapi import Request
from starlette.responses import PlainTextResponse
from starlette.routing import Route
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
import uvicorn

if __name__ == "__main__":
    uvicorn.run("crawler_x.api.main:app", host="127.0.0.1", port=8000, reload=True)
