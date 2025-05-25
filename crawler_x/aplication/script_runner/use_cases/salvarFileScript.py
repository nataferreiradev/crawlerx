from crawler_x.modules.script_runner.service.script_manager import ScriptManager
from .procurarScript import ProcurarScript
from .alterarScript import AlterarScript
from sqlalchemy.orm import Session
from fastapi import File

class SalvarFileScript:
    def __init__(self, session: Session):
        self.procurar_script = ProcurarScript(session)
        self.script_manager = ScriptManager()
        self.alterar_script = AlterarScript(session)

    def execute(self, file: File, id: int):
        script = self.procurar_script.execute(id)
        if not script:
            raise ValueError("Script não encontrado")
        
        if self.script_manager.get_file_path(script.path):
            raise Exception("script já possui um arquivo associado")
        
        new_path = self.script_manager.save_file(script.path, file.file.read())

        script.path = new_path

        self.alterar_script.execute(script)
        