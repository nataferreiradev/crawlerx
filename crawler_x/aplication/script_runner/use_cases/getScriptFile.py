from crawler_x.modules.script_runner.repository.scriptRepository import ScriptRepository 
from crawler_x.modules.script_runner.integration.scriptDao import ScriptDAO 
from crawler_x.aplication.script_runner.use_cases.procurarScript import ProcurarScript
from crawler_x.modules.script_runner.service.script_recover import ScriptRecover
from sqlalchemy.orm import Session

class GetScriptFile():
    def __init__(self, session: Session):
        self.procurar_script = ProcurarScript(session)

    def execute(self, id: int):
        script = self.procurar_script.execute(id)
        if not script:
            return None
        script_recover = ScriptRecover()
        return script_recover.get_file_path(script.path);