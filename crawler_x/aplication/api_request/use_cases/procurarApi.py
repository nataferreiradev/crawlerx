from crawler_x.modules.api_request.repository.api_repository import ApiRepository
from crawler_x.modules.api_request.integration.api_dao import ApiDAO
from sqlalchemy.orm import Session

class ProcurarApi():
    def __init__(self,session: Session):
        self.api_repository = ApiRepository(ApiDAO(session))

    def execute(self, id):
        return self.api_repository.get(id)