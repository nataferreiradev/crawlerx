from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from crawler_x.aplication.api_request.use_cases import (
    ListarApi, ProcurarApi, CadastrarApi, DeletarApi, AtualizarApi
)
from sqlalchemy.orm import Session
from crawler_x.infrastructure.dataBase.sqlalchemy_session import get_db
from crawler_x.modules.api_request.model import ApiOrmObject, ApiJsonObject

router = APIRouter()

def validate_id(id: int):
    if id <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="ID deve ser maior que zero"
        )

@router.get("/{id}")
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

@router.delete("/{id}")
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

@router.get("/")
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

@router.post("/")
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

@router.put("/{id}")
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
