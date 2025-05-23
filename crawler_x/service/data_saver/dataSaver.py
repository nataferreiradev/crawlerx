import os
from crawler_x.modules.api_request.model.apiOrmObject import ApiOrmObject
from requests import Response
from datetime import datetime


class DataSaver():
    dirName = 'data'

    def save_from_response(self, resp: Response, ApiObject: ApiOrmObject):
        extension = 'json' if resp.headers.get('Content-Type') == 'application/json' else ApiObject.return_type
        self.save(ApiObject.name, resp.content, extension)
    
    def save(self, name: str, content: str, extension: str):
        file_path = self.getFilePath(name, extension)
        with open(file_path, 'wb') as file:  
            if isinstance(content, str):
                content = content.encode('utf-8')  
            file.write(content) 
    
    def getDir(self):
        dir_path = os.path.join(self.dirName, datetime.now().strftime('%Y-%m-%d'))
        os.makedirs(dir_path, exist_ok=True) 
        return dir_path

    def getFilePath(self, name: str, extension: str):
        dir_path = self.getDir()
        date = datetime.now().time()
        
        date_str = date.strftime('%H-%M-%S')  # Formato seguro para nomes de arquivos
        
        file_path = os.path.join(dir_path, f'{name}-{date_str}.{extension}')
        return file_path