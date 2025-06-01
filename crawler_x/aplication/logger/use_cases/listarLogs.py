from sqlalchemy.orm import Session
from crawler_x.modules.log_saver.repository.logRepository import LogRepository
from crawler_x.modules.log_saver.integration.logDao import LogDao

class ListarLogs():
    def __init__(self, session: Session):
        self.repository = LogRepository(LogDao(session))
        
    def execute(self) :
        return self.repository.get_all()