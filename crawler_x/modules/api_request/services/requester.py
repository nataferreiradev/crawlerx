import requests as req
from ..model.apiObject import ApiObject
from crawler_x.service.data_saver.dataSaver import DataSaver

class Requester():
    def __init__(self):
        self.data_saver = DataSaver()

    def make_request(self,api_object: ApiObject) -> req.Response:
        resp: req.Response;
        method = api_object.method.upper().strip()
        if method == "":
            raise ValueError("HTTP method cannot be empty")
        if method == "GET":
            resp = self.get(api_object)
        elif method == "POST":
            resp = self.post(api_object)
        elif method == "PUT":
            resp = self.put(api_object)
        else:
            raise ValueError(f"Unsupported HTTP method: {api_object.method}")

        self.data_saver.save_from_response(resp, api_object)
        return resp



    def get(self, api_object: ApiObject):
        return req.get(url=api_object.url, headers=api_object.headers, params=api_object.params)

    def post(self, api_object: ApiObject):
        return req.post(url=api_object.url, headers=api_object.headers, params=api_object.params)

    def put(self, api_object: ApiObject):
        return req.put(url=api_object.url, headers=api_object.headers, params=api_object.params)