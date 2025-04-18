import requests as req
from . import api_object as api

class requester():
    def makeRequest(self,apiObject: api.ApiObject) -> req.Response:
        if apiObject.method.upper() == "GET":
            return self.get(apiObject)
        elif apiObject.method.upper() == "POST":
            return self.post(apiObject)
        elif apiObject.method.upper() == "PUT":
            return self.put(apiObject)
        else:
            raise ValueError(f"Unsupported HTTP method: {apiObject.method}")

    def get(self, apiObject: api.ApiObject):
        return req.get(url=apiObject.url, headers=apiObject.headers, params=apiObject.params)

    def post(self, apiObject: api.ApiObject):
        return req.post(url=apiObject.url, headers=apiObject.headers, params=apiObject.params)

    def put(self, apiObject: api.ApiObject):
        return req.put(url=apiObject.url, headers=apiObject.headers, params=apiObject.params)