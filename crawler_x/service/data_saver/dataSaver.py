import os
from crawler_x.modules.api_request.model.apiOrmObject import ApiOrmObject
from requests import Response
from datetime import datetime
import json


class DataSaver():
    dirName = 'data'

    def save_from_response(self, resp: Response, ApiObject: ApiOrmObject):
        extension = 'json' if resp.headers.get('Content-Type') == 'application/json' else ApiObject.return_type
        self.save(ApiObject.name, resp.content, extension)
    
    def save(self, name: str, content, extension: str):
        file_path = self.getFilePath(name, extension)

        if isinstance(content, str) or isinstance(content, bytes):
            to_write = content
        else:
            to_write = json.dumps(content, ensure_ascii=False, indent=2)

        # se for bytes o modo de escrita é diferente
        mode = 'wb' if isinstance(to_write, bytes) else 'w'

        with open(file_path, mode, encoding='utf-8' if mode == 'w' else None) as file:
            file.write(to_write)
    

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