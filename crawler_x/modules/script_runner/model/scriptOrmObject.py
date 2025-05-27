from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ScriptOrmObject(Base):
    __tablename__ = 'scriptTable'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    path = Column(String, nullable=True)
    return_type = Column(String, default='txt')