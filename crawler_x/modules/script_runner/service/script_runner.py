from crawler_x.modules.script_runner.model.scriptOrmObject import ScriptOrmObject
from crawler_x.service.data_saver.dataSaver import DataSaver

scripts_dir = 'scripts'
    
class PythonScriptRunner:

    def run(self,script: ScriptOrmObject):
        context = {}

        with open(script.path, 'r', encoding='utf-8') as file:
            script_code = file.read()

        # aqui pode ser definido oque o script pode acessar
        # Exemplo: __builtins__ é o módulo builtins, que contém funções e exceções padrão
        # assim ele poderá assesar as funções principais mas em caso de mais segurança poderá ser alterado
        safe_globals = {
            "__builtins__": __builtins__,  
        }

        # o script será executado e deve comter uma variacel chamada "result" que será um dicionário
        # onde o script poderá armazenar os dados

        exec(script_code, safe_globals, context)

        data = self.getResult(context)
        if data is not None:
            self.saveResult(data,script)
    
    def saveResult(self,data,script: ScriptOrmObject):
        dataSaver = DataSaver()

        dataSaver.save(script.name, data, 'json')

    def getResult(self,context: dict):
        return context.get('result')

    def get(self, name: str):
        return self.context.get(name)