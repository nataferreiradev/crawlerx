from sqlalchemy.orm import Session
from typing import Optional, List
from crawler_x.integration.DAO.DAO import DAO 
from crawler_x.modules.api_request.model.apiObject import ApiObject

class ApiDAO(DAO):
    def __init__(self, session: Session):
        self.session = session

    def get(self, id: int) -> Optional[ApiObject]:
        return self.session.query(ApiObject).filter(ApiObject.id == id).first()

    def add(self, api_obj: ApiObject) -> None:
        self.session.add(api_obj)
        self.session.commit()

    def update(self, api_obj: ApiObject) -> None:
        self.session.merge(api_obj)
        self.session.commit()

    def delete(self, id: int) -> None:
        obj = self.get(id)
        if obj:
            self.session.delete(obj)
            self.session.commit()

    def list_all(self) -> List[ApiObject]:
        return self.session.query(ApiObject).all()
