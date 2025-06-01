from crawler_x.modules.log_saver.integration.logDao import LogDao
from crawler_x.modules.log_saver.model.logOrmObject import LogOrmObject

class LogRepository():
    def __init__(self, dao: LogDao):
        self.dao = dao

    def save(self, log: LogOrmObject) -> LogOrmObject: 
        self.dao.add(log)
        return log
    
    def get(self, id: int) -> LogOrmObject:
        return self.dao.get(id)
    
    def delete(self, id: int) -> None:
        self.dao.delete(id)
    
    def update(self, log: LogOrmObject) -> None:
        self.dao.update(log)
    
    def get_all(self) -> list[LogOrmObject]:
        return self.dao.list_all()