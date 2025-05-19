from sqlalchemy.orm import Session
from typing import Optional, List
from crawler_x.integration.DAO.DAO import DAO 
from crawler_x.modules.script_runner.model.script import Script

class ScriptDAO(DAO):
    def __init__(self, session: Session):
        self.session = session

    def get(self, id: int) -> Optional[Script]:
        return self.session.query(Script).filter(Script.id == id).first()

    def add(self, api_obj: Script) -> None:
        self.session.add(api_obj)
        self.session.commit()

    def update(self, api_obj: Script) -> None:
        self.session.merge(api_obj)
        self.session.commit()

    def delete(self, id: int) -> None:
        obj = self.get(id)
        if obj:
            self.session.delete(obj)
            self.session.commit()

    def list_all(self) -> List[Script]:
        return self.session.query(Script).all()
