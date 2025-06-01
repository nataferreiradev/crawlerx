from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
from crawler_x.infrastructure.dataBase.sqlalchemy_session import Base


class LogOrmObject(Base):
    __tablename__ = "request_logs"

    id = Column(Integer, primary_key=True, index=True)
    method = Column(String(10), nullable=False)
    path = Column(String(255), nullable=False)
    status_code = Column(Integer, nullable=False)
    ip = Column(String(45))
    user_agent = Column(Text)
    timestamp = Column(DateTime, default=datetime.now())