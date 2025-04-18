import os
from requests import Response

dirName = 'data'

class DataSaver():
    def saveFromResponse(resp: Response, fileName: str, extension: str):
        os.makedirs(dirName, exist_ok=True)
        with open(f'{dirName}/{fileName}.{extension}', 'wb') as file:  # Corrigido para f-string
            file.write(resp.content)