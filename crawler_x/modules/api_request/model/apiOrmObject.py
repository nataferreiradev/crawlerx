## objetos com sqlalchmy são declarados com a classe Base para o uso do orm

from sqlalchemy import Column, Integer, String, JSON
from crawler_x.infrastructure.dataBase.sqlalchemy_session import Base

class ApiOrmObject(Base):
    __tablename__ = 'apiTable'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    url = Column(String(255))
    method = Column(String(10))
    headers = Column(JSON)
    body = Column(String)
    params = Column(JSON)
    return_type = Column(String(10))
