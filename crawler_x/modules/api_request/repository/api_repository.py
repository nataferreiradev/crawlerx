from crawler_x.modules.api_request.integration.api_dao import ApiDAO
from crawler_x.modules.api_request.model.apiOrmObject import ApiOrmObject

class ApiRepository():
    def __init__(self, dao: ApiDAO):
        self.dao = dao

    def save(self, api_object: ApiOrmObject) -> ApiOrmObject: 
        self.dao.add(api_object)
        return api_object
    
    def get(self, api_object_id: int) -> ApiOrmObject:
        return self.dao.get(api_object_id)
    
    def delete(self, api_object_id: int) -> None:
        self.dao.delete(api_object_id)
    
    def update(self, api_object: ApiOrmObject) -> None:
        self.dao.update(api_object)
    
    def get_all(self) -> list[ApiOrmObject]:
        return self.dao.list_all()