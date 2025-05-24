from crawler_x.modules.api_request.repository.api_repository import ApiRepository
from crawler_x.modules.api_request.model.apiOrmObject import ApiOrmObject
from crawler_x.modules.api_request.integration.api_dao import ApiDAO
from sqlalchemy.orm import Session

class CadastrarApi():
    def __init__(self,session: Session):
        self.repository = ApiRepository(ApiDAO(session))

    def execute(self, api_object: ApiOrmObject) -> ApiOrmObject:
        if not api_object:
            raise ValueError("objeto api não pode ser nulo")
        if api_object.name is None or api_object.name == "":
            raise ValueError("Nome da API não pode ser nulo ou vazio")
        if api_object.url is None or api_object.url == "":
            raise ValueError("URL da API não pode ser nulo ou vazio")
        if api_object.method is None or api_object.method == "":
            raise ValueError("Método da API não pode ser nulo ou vazio")
        try:
             return self.repository.save(api_object) 
        except Exception as e:
            raise Exception(f"Erro ao cadastrar a API: {str(e)}")