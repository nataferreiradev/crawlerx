from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from crawler_x.infrastructure.dataBase.sqlalchemy_session import get_db
from crawler_x.aplication.logger.use_cases.listarLogs import ListarLogs

router = APIRouter()

@router.get("/")
def list_data_folder(db: Session = Depends(get_db)):
    try:
        use_case = ListarLogs(db)
        return use_case.execute()
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": str(e)}
        )
