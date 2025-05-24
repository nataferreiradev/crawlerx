from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from sqlalchemy.orm import Session
from crawler_x.aplication.api_request.use_cases import (
    ListarApi, ProcurarApi, CadastrarApi, DeletarApi, AtualizarApi
)
from crawler_x.aplication.script_runner.use_cases import ( 
    ProcurarScript, ListarScripts, GetScriptFile, DeleteScript, AlterarScript, SalvarScript
)
from crawler_x.aplication.data_recover.use_cases import PegarDiretorioZippado
from crawler_x.infrastructure.dataBase.sqlalchemy_session import get_db
from crawler_x.modules.api_request.model import ApiOrmObject, ApiJsonObject
from crawler_x.modules.script_runner.model import ScriptJsonObject, ScriptOrmObject
from pathlib import Path

router = APIRouter()

def validate_id(id: int):
    if id <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="ID deve ser maior que zero"
        )

@router.get("/api/{id}")
def get_api_por_id(id: int, db: Session = Depends(get_db)):
    validate_id(id)
    try:
        use_case = ProcurarApi(db)
        result = use_case.execute(id)
        if not result:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={"detail": "API não encontrada"}
            )
        return result
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": str(e)}
        )

@router.delete("/api/{id}")
def delete_api_por_id(id: int, db: Session = Depends(get_db)):
    validate_id(id)
    try:
        use_case = DeletarApi(db)
        use_case.execute(id)
        return {"message": "API deletada com sucesso"} 
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": str(e)}
        )

@router.get("/api")
def listar_apis(db: Session = Depends(get_db)):
    try:
        use_case = ListarApi(db)
        result = use_case.execute()
        return result
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": str(e)}
        )

@router.post("/api")
def criar_api(api_data: ApiJsonObject, db: Session = Depends(get_db)):
    if not api_data:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"detail": "Dados da API não podem ser nulos"}
        )
    new_api = ApiOrmObject(
        name=api_data.name,
        url=api_data.url,
        method=api_data.method,
        headers=api_data.headers,
        body=api_data.body,
        params=api_data.params,
        return_type=api_data.return_type
    )
    use_case = CadastrarApi(db)
    try:
        new_api = use_case.execute(new_api)
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={"message": "API criada com sucesso", "id": new_api.id}
        )
    except ValueError as e:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"detail": str(e)}
        )
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": str(e)}
        )

@router.put("/api/{id}")
def update_api(id: int, api_data: ApiJsonObject, db: Session = Depends(get_db)):
    validate_id(id)
    if not api_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Dados da API não podem ser nulos"
        )
    api = ApiOrmObject(
        id=api_data.id,
        name=api_data.name,
        url=api_data.url,
        method=api_data.method,
        headers=api_data.headers,
        body=api_data.body,
        params=api_data.params,
        return_type=api_data.return_type
    )
    if id != api.id:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"detail": "ID na URL não corresponde ao ID do objeto enviado"}
        )
    use_case = AtualizarApi(db)
    try:
        use_case.execute(api)
        return {"message": "API atualizada com sucesso"}
    except ValueError as e:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"detail": str(e)}
        )
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": str(e)}
        )

@router.get("/dataRecover/zip/{folder_name}")
def download_zip(folder_name: str):
    if not folder_name:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"detail": "Nome da pasta não pode ser vazio"}
        )
    dr = PegarDiretorioZippado()
    try:
        zip_path_str = dr.execute(folder_name)
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

@router.get("/script/{id}")
def get_script_por_id(id: int, db: Session = Depends(get_db)):
    validate_id(id)
    try:
        use_case = ProcurarScript(db)
        result = use_case.execute(id)
        if not result:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={"detail": "Script não encontrado"}
            )
        return result
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": str(e)}
        )

@router.get("/script")
def get_listar_scripts(db: Session = Depends(get_db)):
    try:
        use_case = ListarScripts(db)
        return use_case.execute()
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": str(e)}
        )

@router.put("/script/{id}")
def update_script(id: int, script_data: ScriptJsonObject, db: Session = Depends(get_db)):
    validate_id(id)
    if not script_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Dados do Script não podem ser nulos"
        )
    script = ScriptOrmObject(
        id=script_data.id,
        name=script_data.name,
        return_type=script_data.return_type
    )
    if id != script_data.id:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"detail": "ID na URL não corresponde ao ID do objeto enviado"}
        )
    use_case = AlterarScript(db)
    try:
        use_case.execute(script)
        return {"message": "Script atualizada com sucesso"}
    except ValueError as e:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"detail": str(e)}
        )
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": str(e)}
        )

@router.post("/script")
def criar_script(script_data: ScriptJsonObject, db: Session = Depends(get_db)):
    if not script_data:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"detail": "Dados do Script não podem ser nulos"}
        )
    new_script = ApiOrmObject(
        name=script_data.name,
        return_type=script_data.return_type
    )
    use_case = SalvarScript(db)
    try:
        new_script = use_case.execute(new_script)
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={"message": "Script criada com sucesso", "id": new_script.id}
        )
    except ValueError as e:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"detail": str(e)}
        )
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": str(e)}
        )

@router.delete("/script/{id}")
def delete_script(id: int, db: Session = Depends(get_db)):
    validate_id(id)
    try:
        use_case = DeleteScript(db)
        use_case.execute(id) 
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"message": "Script deletado com sucesso"}
        )
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": str(e)}
        )

@router.get("/script/file/{id}")
def get_script_file(id: int, db: Session = Depends(get_db)):
    validate_id(id)
    try:
        use_case = GetScriptFile(db)
        result = use_case.execute(id)
        if not result:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={"detail": "Arquivo não encontrado"}
            )

        file_path = Path(result)
        if not file_path.exists():
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={"detail": "Falha ao localizar o arquivo no sistema de arquivos"}
            )

        return FileResponse(
            path=file_path,
            media_type="text/x-python",
            filename=file_path.name
        )
    except FileNotFoundError as e:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": str(e)}
        )
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": str(e)}
        )