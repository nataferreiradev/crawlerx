from crawler_x.modules.api_request.repository.api_repository import ApiRepository
from crawler_x.modules.api_request.model.apiOrmObject import ApiOrmObject
from crawler_x.modules.api_request.integration.api_dao import ApiDAO
from sqlalchemy.orm import Session

class AtualizarApi():
    def __init__(self,session: Session):
        self.repository = ApiRepository(ApiDAO(session))

    def execute(self, api: ApiOrmObject) -> ApiOrmObject:
        if not api:
            raise ValueError("objeto api não pode ser nulo")
        if api.name is None or api.name == "":
            raise ValueError("Nome da API não pode ser nulo ou vazio")
        if api.url is None or api.url == "":
            raise ValueError("URL da API não pode ser nulo ou vazio")
        if api.method is None or api.method == "":
            raise ValueError("Método da API não pode ser nulo ou vazio")
        api.method = api.method.upper()
        if api.method not in ["GET", "POST", "PUT"]:
            ValueError("Método da API deve ser 'GET', 'POST' ou 'PUT'")
        if api.return_type is None or api.return_type == "":
            raise ValueError("Tipo de retorno da API não pode ser nulo ou vazio")
        api.return_type = api.return_type.lower()
        try:
            return self.repository.update(api)
        except Exception as e:
            raise Exception(f"Erro ao atualizar a API: {str(e)}")