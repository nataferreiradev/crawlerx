from sqlalchemy.orm import Session
from typing import Optional, List
from crawler_x.infrastructure.DAO.DAO import DAO 
from crawler_x.modules.log_saver.model.logOrmObject import LogOrmObject

class LogDao(DAO):
    def __init__(self, session: Session):
        self.session = session

    def get(self, id: int) -> Optional[LogOrmObject]:
        return self.session.query(LogOrmObject).filter(LogOrmObject.id == id).first()

    def add(self, log: LogOrmObject) -> None:
        self.session.add(log)
        self.session.commit()

    def update(self, log: LogOrmObject) -> None:
        self.session.merge(log)
        self.session.commit()

    def delete(self, id: int) -> None:
        obj = self.get(id)
        if obj:
            self.session.delete(obj)
            self.session.commit()

    def list_all(self) -> List[LogOrmObject]:
        return self.session.query(LogOrmObject).all()
