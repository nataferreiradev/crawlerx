from crawler_x.aplication.api_request.use_cases.listarApi import ListarApi
from crawler_x.aplication.script_runner.use_cases.listarScripts import ListarScripts
from crawler_x.service.crawler_manager.crawlerManager import CrawlerManager
from sqlalchemy.orm import Session

class CrawlerRun():
    def __init__(self, session: Session):
        self.listar_api = ListarApi(session)
        self.listar_scripts = ListarScripts(session)
        self.crawler_manager = CrawlerManager()

    def execute(self,callback: callable):
        apis = self.listar_api.execute()
        scripts = self.listar_scripts.execute()

        self.crawler_manager.execute(scripts, apis, callback)
