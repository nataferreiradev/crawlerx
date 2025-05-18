from crawler_x.modules.api_request.model.apiObject import ApiObject 
from crawler_x.modules.api_request.services.requester import Requester
from requests import Response 
from crawler_x.integration.DAO.DAO import GenericORM as ORM
from crawler_x.integration.dataBase.sqlite.sqlite import SQLiteDatabase as sqlite
from crawler_x.modules.script_runner.model.script import Script
from crawler_x.modules.script_runner.service.script_runner import PythonScriptRunner  
import crawler_x.integration.dataBase.dataBaseScript as dbScript
import crawler_x.miscelaneos as miscelaneos

#          █▀▀ █▀█ ▄▀█ █░█░█ █░░ █▀▀ █▀█ ▀▄▀
#          █▄▄ █▀▄ █▀█ ▀▄▀▄▀ █▄▄ ██▄ █▀▄ █░█


def initDataBase():
    db_connection = sqlite(dbScript.data_base_path + dbScript.data_base_name)
    db_connection.execute(dbScript.api_table_script)
    db_connection.execute(dbScript.script_table_script)
    db_connection.execute(f'delete from {ApiObject().table_name}')
    db_connection.execute(f'delete from {Script().table_name}')
    return db_connection

def main():
    miscelaneos.print_logo()
    db = initDataBase();
    dao = ORM(db)

    api = ApiObject();
    api.name = "API"
    api.url = "https://jsonplaceholder.typicode.com/posts"
    api.params = {"userId": 1}
    api.headers = {"Content-Type": "application/json"}
    api.method = "GET"

    api2 = ApiObject();
    api2.name = "API2"
    api2.url = "https://jsonplaceholder.typicode.com/comments"
    api2.params = {"postId": 1}
    api2.headers = {"Content-Type": "application/json"}
    api2.method = "GET"

    api3 = ApiObject();
    api3.name = "API3"
    api3.url = "https://jsonplaceholder.typicode.com/albums"
    api3.params = {"userId": 1}
    api3.headers = {"Content-Type": "application/json"}
    api3.method = "GET"

    api4 = ApiObject();
    api4.name = "API4"
    api4.url = "https://jsonplaceholder.typicode.com/photos"
    api4.params = {"albumId": 1}
    api4.headers = {"Content-Type": "application/json"}
    api4.method = "GET"

    dao.insert(api);
    dao.insert(api2);
    dao.insert(api3);
    dao.insert(api4);

    script = Script();
    script.name = "script"
    script.path = "scripts/teste.py"
    dao.insert(script)

    script_runner = PythonScriptRunner()
    script_runner.run(script)

    requester = Requester()

    saved_apis: list = dao.list_all(ApiObject);

    print('--'* 20);

    for saved_api in saved_apis:
        resp: Response = requester.make_request(saved_api)
        print('\n')
        print(resp.json());

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
