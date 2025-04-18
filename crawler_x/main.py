from crawler_x.api_request import api_object as obj
from crawler_x.api_request import requesterBO as req
from requests import Response 
from crawler_x.DAO.dao import GenericDAO as DAO
from crawler_x.dataBase.sqlite.sqlite import SQLiteDatabase as sqlite
from crawler_x.dataSaver.dataSaver import DataSaver  as ds
import crawler_x.dataBase.dataBaseScript as dbScript
import crawler_x.miscelaneos as miscelaneos

#          █▀▀ █▀█ ▄▀█ █░█░█ █░░ █▀▀ █▀█ ▀▄▀
#          █▄▄ █▀▄ █▀█ ▀▄▀▄▀ █▄▄ ██▄ █▀▄ █░█


def initDataBase():
    dbPath = f"dataBase/{dbScript.dataBaseName}"
    dbConnection = sqlite(dbPath)
    dbConnection.execute(dbScript.apiTableScript)
    dbConnection.execute(dbScript.scriptTableScript)
    return dbConnection

def main():
    miscelaneos.printLogo()
    db = initDataBase();
    dao = DAO(db)

    api = obj.ApiObject();
    api.name = "API"
    api.url = "https://jsonplaceholder.typicode.com/posts"
    api.params = {"userId": 1}
    api.headers = {"Content-Type": "application/json"}
    api.method = "GET"

    dao.insert("apiTable", api);

    requester = req.requester()

    resp: Response = requester.makeRequest(api)

    ds.saveFromResponse(resp, "response", "json");
    
    return

if __name__ == "__main__":
    main()

# !por favor não apagar! 
# uma lembrança dos alunos do ricardo 2025 5ºsemestre
# créditos do projeto
#
# Julia Zuim
# Diogo
# Natã Nogueira Ferreira github: https://github.com/nataferreiradev
# Rafael de Camargo Neves
# Kauê Sobreira github: https://github.com/KaueSobreira 


# █▀ ▀█▀ █░█ █▀▄ █ █▀█   █▀▀ █▀█ █▀█ ▀█▀ █▀▀ ▀▄▀
# ▄█ ░█░ █▄█ █▄▀ █ █▄█   █▄▄ █▄█ █▀▄ ░█░ ██▄ █░█
