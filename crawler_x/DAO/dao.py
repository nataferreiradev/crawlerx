from crawler_x.dataBase.interface.db import DatabaseInterface
from dataclasses import asdict
import json

## para o dao funcionar a classe deve ser serializavel!

## exemplo:

##from dataclasses import dataclass, asdict

##@dataclass
##class User:
##    id: int = None
##    name: str = ''
##    age: int = 0

class GenericDAO:
    def __init__(self, db: DatabaseInterface):
        self.db = db

    def insert(self, table: str, obj):
        data = asdict(obj)
        # Serializar dicionários para JSON
        data = {k: (json.dumps(v) if isinstance(v, dict) else v) for k, v in data.items() if v is not None}
        self.db.insert(table, data)

    def update(self, table: str, obj, condition: str, params: tuple = ()):
        data = asdict(obj)
        data = {k: v for k, v in data.items() if k != 'id' and v is not None}
        self.db.update(table, data, condition, params)

    def delete_by_id(self, table: str, id_value):
        self.db.delete(table, 'id = ?', (id_value,))
