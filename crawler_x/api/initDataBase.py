from crawler_x.modules.api_request.model.apiOrmObject import ApiOrmObject
from crawler_x.modules.log_saver.model.logOrmObject import LogOrmObject 
from crawler_x.modules.script_runner.model.scriptOrmObject import ScriptOrmObject
from crawler_x.infrastructure.dataBase.sqlalchemy_session import Base,engine

def init():
    Base.metadata.create_all(bind=engine);