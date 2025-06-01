from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from crawler_x.aplication.logger.use_cases.listarLogs import ListarLogs

router = APIRouter()

@router.get("/")
def list_data_folder():
    use_case = ListarLogs()
    try:
        return use_case.execute()
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": str(e)}
        )
