import requests as req
from . import api_object as api 

class requester():
    def makeRequest(apiObject: api.ApiObject) -> req.Response:
        resp = req.get(url=apiObject.url,headers= apiObject.headers,params= apiObject.query_params)        
        return resp;

