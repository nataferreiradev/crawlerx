from crawler_x.modules.script_runner.repository.scriptRepository import ScriptRepository 
from crawler_x.modules.script_runner.integration.scriptDao import ScriptDAO 
from sqlalchemy.orm import Session

class ListarScripts():
    def __init__(self, session: Session):
        self.script_repository = ScriptRepository(ScriptDAO(session)) 

    def execute(self):
        return self.script_repository.get_all();
