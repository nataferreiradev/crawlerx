from crawler_x.modules.script_runner.integration.scriptDao import ScriptDAO
from crawler_x.modules.script_runner.model.script import Script

class ApiRepository():
    def __init__(self, dao: ScriptDAO):
        self.dao = dao

    def save(self, api_object: Script) -> Script: 
        self.dao.add(api_object)
        return api_object
    
    def get(self, api_object_id: int) -> Script:
        return self.dao.get(api_object_id)
    
    def delete(self, api_object_id: int) -> None:
        self.dao.delete(api_object_id)
    
    def update(self, api_object: Script) -> None:
        self.dao.update(api_object)
    
    def get_all(self) -> list[Script]:
        return self.dao.list_all()