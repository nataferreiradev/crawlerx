from crawler_x.modules.api_request.repository.api_repository import ApiRepository
from crawler_x.modules.api_request.model.apiOrmObject import ApiOrmObject
from crawler_x.modules.api_request.integration.api_dao import ApiDAO
from sqlalchemy.orm import Session

class DeletarApi():
    def __init__(self,session: Session):
        self.repository = ApiRepository(ApiDAO(session))

    def execute(self, id: int) -> ApiOrmObject:
        try:
            return self.repository.delete(id)
        except Exception as e:
            raise Exception(f"Erro ao deletar a API: {str(e)}")