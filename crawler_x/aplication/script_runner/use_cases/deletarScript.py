from crawler_x.modules.script_runner.repository.scriptRepository import ScriptRepository 
from crawler_x.modules.script_runner.integration.scriptDao import ScriptDAO 
from crawler_x.aplication.script_runner.use_cases.procurarScript import ProcurarScript
from crawler_x.modules.script_runner.service.script_manager import ScriptManager
from sqlalchemy.orm import Session

class DeleteScript():
    def __init__(self, session: Session):
        self.procurar_script = ProcurarScript(session)
        self.directory = ScriptRepository(ScriptDAO(session))

    def execute(self, id: int):
        script = self.procurar_script.execute(id)
        if not script:
            raise Exception("Script não encontrado")
        script_recover = ScriptManager()
        self.directory.delete(script.id)

        if script.path:
            try:
                script_recover.delete_file(script.path)
            except Exception as e:
                return;
        
        
