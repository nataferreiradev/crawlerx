from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse, FileResponse
from pathlib import Path
from crawler_x.aplication.data_recover.use_cases import PegarDiretorioZippado, ListarDiretorios

router = APIRouter()

@router.get("/")
def list_data_folder():
    use_case = ListarDiretorios()
    try:
        return use_case.execute()
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": str(e)}
        )

@router.get("/zip/{folder_name}")
def download_zip(folder_name: str):
    if not folder_name:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"detail": "Nome da pasta não pode ser vazio"}
        )
    use_case = PegarDiretorioZippado()
    try:
        zip_path_str = use_case.execute(folder_name)
        if zip_path_str is None:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={"detail": f"Zip para '{folder_name}' não foi gerado."}
            )
        zip_path = Path(zip_path_str)
    except FileNotFoundError as e:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": str(e)}
        )

    if not zip_path.exists():
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": "Falha ao localizar o arquivo ZIP."}
        )

    return FileResponse(
        path=zip_path,
        media_type="application/zip",
        filename=zip_path.name
    )