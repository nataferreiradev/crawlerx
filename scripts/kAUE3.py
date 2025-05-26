from sqlalchemy.orm import Session
from crawler_x.modules.script_runner.model.scriptOrmObject import ScriptOrmObject
from crawler_x.modules.script_runner.repository.scriptRepository import ScriptRepository
from crawler_x.modules.script_runner.integration.scriptDao import ScriptDAO

class SalvarScript():
    def __init__(self, session: Session):
        self.script_repository = ScriptRepository(ScriptDAO(session))
        
    def execute(self, script: ScriptOrmObject) -> ScriptOrmObject:
        if not script:
            raise ValueError("Script não encontrado")
        if script.return_type == "" or script.return_type is None:
            raise ValueError("Tipo de retorno não encontrado")
        if script.name == "" or script.name is None:
            raise ValueError("Nome do script não encontrado")
        return self.script_repository.save(script)