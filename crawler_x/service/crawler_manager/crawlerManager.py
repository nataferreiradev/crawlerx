from crawler_x.modules.api_request.services.requester import Requester
from crawler_x.modules.script_runner.service.script_runner import PythonScriptRunner


class CrawlerManager:
    def __init__(self):
        self.script_runner = PythonScriptRunner()
        self.requester = Requester()

    def execute(self,scripts: list,apis: list, registerCallback: callable):

        total_executions = len(apis) + len(scripts)
        total_executatos = 0


        for api in apis:
            total_executatos += 1
            try:
                self.requester.make_request(api)
                registerCallback(self.get_json_massage(total_executions, total_executatos, f"api {api.name} executada com sucesso"))
            except Exception as e:
                registerCallback(self.get_json_massage(total_executions, total_executatos, f"Erro ao executar a api {api.name}: {str(e)}"))

        
        for script in scripts:
            total_executatos += 1
            print(f"Executando script: {script.name}")
            print(f"Script path: {script.path}")
            if not script.path or script.path == "":
                registerCallback(self.get_json_massage(total_executions, total_executatos, f"Script {script.name} não possui um arquivo associado"))
                continue

            try:
                self.script_runner.run(script)
                registerCallback(self.get_json_massage(total_executions, total_executatos, f"script {script.name} executado com sucesso"))
            except Exception as e:
                registerCallback(self.get_json_massage(total_executions, total_executatos, f"Erro ao executar o script {script.name}: {str(e)}"))

        registerCallback(self.get_json_massage(total_executions, total_executatos, "Execução finalizada"))


    def get_execution_percentage(self, total_executions: int, total_executados: int) -> float:
        if total_executions == 0:
            return 0.0
        return (total_executados / total_executions) * 100

    def get_json_massage(self,total_executions: int, total_executados: int,message: str) -> dict:
        return {
            "total_executions": total_executions,
            "total_executados": total_executados,
            "percentage": int(self.get_execution_percentage(total_executions, total_executados)),
            "message": message,
        }