from crawler_x.integration.dataBase.interface.db import DatabaseInterface
from dataclasses import asdict,fields,is_dataclass
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
        if not is_dataclass(cls):
            raise ValueError("The provided class must be a dataclass.")

        query = f"SELECT * FROM {cls().table_name}"
        results = self.db.execute(query)

        cls_fields = [field.name for field in fields(cls)]

        objects = []
        for row in results:
            obj_data = {key: value for key, value in zip(cls_fields, row)}

            for field in fields(cls):
                if field.metadata.get("json", False):  # Verifica se o campo tem a flag "json" na implementação da dataclass
                    key = field.name
                    value = obj_data.get(key)
                    if isinstance(value, str):
                        try:
                            obj_data[key] = json.loads(value)
                        except json.JSONDecodeError:
                            obj_data[key] = {}

            obj_data = {key: (value if value is not None else '') for key, value in obj_data.items()}
            objects.append(cls(**obj_data))

        return objects