from sqlalchemy.orm import Session
from crawler_x.modules.log_saver.model.logOrmObject import LogOrmObject
from crawler_x.modules.log_saver.repository.logRepository import LogRepository
from crawler_x.modules.log_saver.integration.logDao import LogDao

class InsertLog():
    def __init__(self, session: Session):
        self.repository = LogRepository(LogDao(session))
        
    def execute(self, log: LogOrmObject) :
        if log.id:
            raise ValueError("id deve ser vazio")
        return self.repository.save(log)