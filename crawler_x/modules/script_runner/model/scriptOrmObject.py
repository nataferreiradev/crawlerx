from sqlalchemy import Column, Integer, String
from crawler_x.infrastructure.dataBase.sqlalchemy_session import Base

class ScriptOrmObject(Base):
    __tablename__ = 'scriptTable'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    path = Column(String, nullable=True)
    return_type = Column(String, default='txt')