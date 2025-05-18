from crawler_x.modules.api_request.integration.api_dao import ApiDAO
from crawler_x.modules.api_request.model.apiObject import ApiObject

class ApiRepository():
    def __init__(self, dao: ApiDAO):
        self.dao = dao

    def save(self, api_object: ApiObject) -> ApiObject: 
        return self.dao.save(api_object)
    
    def get(self, api_object_id: int) -> ApiObject:
        return self.dao.get(api_object_id)
    
    def delete(self, api_object_id: int) -> None:
        self.dao.delete(api_object_id)
    
    def udpate(self, api_object: ApiObject) -> None:
        self.dao.update(api_object)
    
    def get_all(self) -> list[ApiObject]:
        return self.dao.list_all()