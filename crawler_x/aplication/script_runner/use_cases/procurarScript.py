from crawler_x.modules.script_runner.repository.scriptRepository import ScriptRepository 
from crawler_x.modules.script_runner.integration.scriptDao import ScriptDAO 
from sqlalchemy.orm import Session

class ProcurarScript():
    def __init__(self, session: Session):
        self.script_repository = ScriptRepository(ScriptDAO(session)) 

    def execute(self, id: int):
        return self.script_repository.get(id);
