from crawler_x.modules.script_runner.integration.scriptDao import ScriptDAO
from crawler_x.modules.script_runner.model.scriptOrmObject import ScriptOrmObject

class ScriptRepository():
    def __init__(self, dao: ScriptDAO):
        self.dao = dao

    def save(self, api_object: ScriptOrmObject) -> ScriptOrmObject: 
        self.dao.add(api_object)
        return api_object
    
    def get(self, api_object_id: int) -> ScriptOrmObject:
        return self.dao.get(api_object_id)
    
    def delete(self, api_object_id: int) -> None:
        self.dao.delete(api_object_id)
    
    def update(self, api_object: ScriptOrmObject) -> None:
        self.dao.update(api_object)
    
    def get_all(self) -> list[ScriptOrmObject]:
        return self.dao.list_all()