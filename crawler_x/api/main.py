from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from crawler_x.api.routes.router import router

app = FastAPI(
    title="Projeto X API",
    description="APIs para orquestração de serviços do Projeto X",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/v1")


# a estrutura ficou da seguinte forma:
# o handler valida os dados da requisição principalmente os parametros da requisição 
# o handler da rota instancia um caso de uso e injeta a sessão do banco definida em infrasctructure/database/sqlalchemy_session.py
# o metodo get_db faz a injeção da sessão do banco
# o caso de uso intancia o repository concreto para o tipo de dado que ele vai manipular e injeta um DAO com a sessão do banco
# o handler chama o entry point do caso de uso passando os dados nescessarios
# o caso de uso valida os dados passados retornando exceções caso os dados estejam incorretos
# o caso de uso chama o repository que por sua vez chama o DAO para persistir os dados no banco
# o DAO chama o banco e persiste os dados
# o DAO retorna os dados persistidos para o repository
# o repository retorna os dados para o caso de uso
# o caso de uso retorna os dados para o handler
# o handler retorna os dados para o cliente