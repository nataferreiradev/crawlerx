from crawler_x.api_request import api_object as obj
from crawler_x.api_request import requester as req
from requests import Response 

#          █▀▀ █▀█ ▄▀█ █░█░█ █░░ █▀▀ █▀█ ▀▄▀
#          █▄▄ █▀▄ █▀█ ▀▄▀▄▀ █▄▄ ██▄ █▀▄ █░█

def printLogo():
    print('\n')
    print('█▀▀ █▀█ ▄▀█ █░█░█ █░░ █▀▀ █▀█ ▀▄▀')
    print('█▄▄ █▀▄ █▀█ ▀▄▀▄▀ █▄▄ ██▄ █▀▄ █░█')
    print('\n')
    print('█▀ ▀█▀ █░█ █▀▄ █ █▀█   █▀▀ █▀█ █▀█ ▀█▀ █▀▀ ▀▄▀')
    print('▄█ ░█░ █▄█ █▄▀ █ █▄█   █▄▄ █▄█ █▀▄ ░█░ ██▄ █░█')


def main():
    api = obj.ApiObject(name='teste', url='https://jsonplaceholder.typicode.com/posts',headers=None,query_params=None)
    resp: Response = req.requester.makeRequest(api)
    printLogo()
    print(resp.json())
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
