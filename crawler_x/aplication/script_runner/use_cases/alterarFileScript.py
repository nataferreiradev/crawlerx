from crawler_x.modules.script_runner.service.script_manager import ScriptManager
from .procurarScript import ProcurarScript
from .alterarScript import AlterarScript
from sqlalchemy.orm import Session
from fastapi import UploadFile

class AlterarFileScript:
    def __init__(self, session: Session):
        self.procurar_script = ProcurarScript(session)
        self.script_manager = ScriptManager()
        self.alterar_script = AlterarScript(session)

    def execute(self, file: UploadFile, id: int):
        script = self.procurar_script.execute(id)
        file_bytes = file.file.read()
        file_content = file_bytes.decode('utf-8')
        
        if not script:
            raise ValueError("Script não encontrado")
        
        if not self.script_manager.get_file_path(script.path):
            raise Exception("script não possui um arquivo associado crie um novo arquivo")
        
        if not self.script_manager.search_in_file_for_result_var(file_content):
            raise ValueError("O arquivo deve conter a variável 'result'.")
        
        new_path = self.script_manager.save_file(script.nam, file_bytes)
        if not new_path:
            raise ValueError("Erro ao salvar o arquivo.")

        script.path = new_path

        return self.alterar_script.execute(script)
        