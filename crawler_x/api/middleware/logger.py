from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from typing import Callable

from crawler_x.modules.log_saver.model.logOrmObject import LogOrmObject
from crawler_x.aplication.logger.use_cases.insertLog import InsertLog
from sqlalchemy.orm import Session

def get_client_ip(request: Request) -> str:
    forwarded = request.headers.get("x-forwarded-for")
    if forwarded:
        return forwarded.split(",")[0].strip()
    return request.client.host

class LoggingMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, db_sessionmaker):
        super().__init__(app)
        self.db_sessionmaker = db_sessionmaker

    async def dispatch(self, request: Request, call_next: Callable):
        response: Response = await call_next(request)

        def save_log():
            with self.db_sessionmaker() as db:
                use_case = InsertLog(db)

                log = LogOrmObject(
                    method=request.method,
                    path=str(request.url.path),
                    status_code=response.status_code,
                    ip=get_client_ip(request),
                    user_agent=request.headers.get("User-Agent")
                )

                use_case.execute(log)

        import asyncio
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, save_log)

        return response
