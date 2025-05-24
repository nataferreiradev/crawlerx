from sqlalchemy.orm import Session
from typing import Optional, List
from crawler_x.infrastructure.DAO.DAO import DAO 
from crawler_x.modules.script_runner.model.scriptOrmObject import ScriptOrmObject

class ScriptDAO(DAO):
    def __init__(self, session: Session):
        self.session = session

    def get(self, id: int) -> Optional[ScriptOrmObject]:
        return self.session.query(ScriptOrmObject).filter(ScriptOrmObject.id == id).first()

    def add(self, api_obj: ScriptOrmObject) -> None:
        self.session.add(api_obj)
        self.session.commit()

    def update(self, api_obj: ScriptOrmObject) -> None:
        self.session.merge(api_obj)
        self.session.commit()

    def delete(self, id: int) -> None:
        obj = self.get(id)
        if obj:
            self.session.delete(obj)
            self.session.commit()

    def list_all(self) -> List[ScriptOrmObject]:
        return self.session.query(ScriptOrmObject).all()
