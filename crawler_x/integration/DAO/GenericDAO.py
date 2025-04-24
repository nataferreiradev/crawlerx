from crawler_x.integration.dataBase.interface.db import DatabaseInterface
from dataclasses import asdict,fields
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

    def insert(self, obj):
        data = asdict(obj)
        data = {k: (json.dumps(v) if isinstance(v, dict) else v) for k, v in data.items() if v is not None}
        self.db.insert(obj.table_name, data)

    def update(self, obj, condition: str, params: tuple = ()):
        data = asdict(obj)
        data = {k: v for k, v in data.items() if k != 'id' and v is not None}
        self.db.update(obj.table_name, data, condition, params)

    def delete_by_id(self, table: str, id_value):
        self.db.delete(table, 'id = ?', (id_value,))

    def list_all(self, cls):
        query = f"SELECT * FROM {cls().table_name}"
        results = self.db.execute(query)

        cls_fields = [field.name for field in fields(cls)]

        objects = []
        for row in results:
            obj_data = {key: value for key, value in zip(cls_fields, row)}

            for key, value in obj_data.items():
                if isinstance(value, str) and (key == "headers" or key == "params"):
                    try:
                        obj_data[key] = json.loads(value)
                    except json.JSONDecodeError:
                        obj_data[key] = {}

            obj_data = {key: (value if value is not None else '') for key, value in obj_data.items()}
            objects.append(cls(**obj_data))

        return objects 