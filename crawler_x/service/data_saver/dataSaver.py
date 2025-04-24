import os
from crawler_x.modules.api_request.model.apiObject import ApiObject
from requests import Response
from datetime import datetime


class DataSaver():
    dirName = 'data'

    def save_from_response(self,resp: Response,ApiObject: ApiObject):
        os.makedirs(self.dirName, exist_ok=True)
        extension = 'json' if resp.headers.get('Content-Type') == 'application/json' else 'txt'
        print(ApiObject.name)
        with open(f'{self.dirName}/{ApiObject.name}-{datetime.now().time()}.{extension}', 'wb') as file:  
            file.write(resp.content)