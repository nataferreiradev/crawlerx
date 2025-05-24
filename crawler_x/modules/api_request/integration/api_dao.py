from sqlalchemy.orm import Session
from typing import Optional, List
from crawler_x.infrastructure.DAO.DAO import DAO 
from crawler_x.modules.api_request.model.apiOrmObject import ApiOrmObject

class ApiDAO(DAO):
    def __init__(self, session: Session):
        self.session = session

    def get(self, id: int) -> Optional[ApiOrmObject]:
        return self.session.query(ApiOrmObject).filter(ApiOrmObject.id == id).first()

    def add(self, api_obj: ApiOrmObject) -> None:
        self.session.add(api_obj)
        self.session.commit()

    def update(self, api_obj: ApiOrmObject) -> None:
        self.session.merge(api_obj)
        self.session.commit()

    def delete(self, id: int) -> None:
        obj = self.get(id)
        if obj:
            self.session.delete(obj)
            self.session.commit()

    def list_all(self) -> List[ApiOrmObject]:
        return self.session.query(ApiOrmObject).all()
