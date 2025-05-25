from fastapi import APIRouter, Depends, HTTPException, status,File, UploadFile
from fastapi.responses import JSONResponse, FileResponse
from sqlalchemy.orm import Session
from pathlib import Path
from crawler_x.aplication.script_runner.use_cases import (
    ProcurarScript, ListarScripts, GetScriptFile, DeleteScript, AlterarScript, SalvarScript,
    SalvarFileScript,
)
from crawler_x.infrastructure.dataBase.sqlalchemy_session import get_db
from crawler_x.modules.script_runner.model import ScriptJsonObject, ScriptOrmObject

router = APIRouter()

def validate_id(id: int):
    if id <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="ID deve ser maior que zero"
        )

@router.get("/{id}")
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

@router.get("/")
def listar_scripts(db: Session = Depends(get_db)):
    try:
        use_case = ListarScripts(db)
        return use_case.execute()
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": str(e)}
        )

@router.post("/")
def criar_script(script_data: ScriptJsonObject, db: Session = Depends(get_db)):
    if not script_data:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"detail": "Dados do Script não podem ser nulos"}
        )
    new_script = ScriptOrmObject(
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

@router.put("/{id}")
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

@router.delete("/{id}")
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

@router.get("/file/{id}")
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

@router.post("/file/{id}")
def post_script_file(id: int,file: UploadFile = File(...), db: Session = Depends(get_db)):
    validate_id(id)
    if not file.filename.endswith(".py"):
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST , detail="Apenas arquivos .py são permitidos.")
    
    try:
        use_case = SalvarFileScript(db)
        use_case.execute(file, id)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"message": "Arquivo salvo com sucesso"}
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


