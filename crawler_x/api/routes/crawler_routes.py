from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from sqlalchemy.orm import Session
from crawler_x.infrastructure.dataBase.sqlalchemy_session import get_db
from crawler_x.aplication.crawler.use_cases.crawlerRun import CrawlerRun
import asyncio

router = APIRouter()

# end point para documentação do websocket
@router.get("/ws-info")
def get_ws_info():
    return {"info": "o endpoint /ws/execute é um websocket que executa o crawler e retorna o progresso da execução."}

@router.websocket("/ws/execute")
async def websocket_crawler_run(websocket: WebSocket, db: Session = Depends(get_db)):
    await websocket.accept()
    crawler_run = CrawlerRun(db)
    loop = asyncio.get_event_loop()

    async def send_callback(message: str):
        await websocket.send_json(message)

    def callback_sync(msg):
        asyncio.run_coroutine_threadsafe(send_callback(msg), loop)

    try:
        await loop.run_in_executor(None, crawler_run.execute, callback_sync)
    except Exception as e:
        await send_callback(f"Erro inesperado: {str(e)}")
    finally:
        await websocket.close()
