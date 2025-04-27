from crawler_x.modules.api_request.model.apiObject import ApiObject
from crawler_x.modules.script_runner.model.script import Script

data_base_name = "crawler.db"
data_base_path = "dataBase/"

api_table_script = f"""
    create table if not exists {ApiObject.table_name} (
        id integer primary key autoincrement,
        name text not null,
        url text not null,
        method text not null,
        headers text,
        body text,
        params text,
        return_type text not null
    )
"""

script_table_script = f"""
    create table if not exists {Script.table_name}(
        id integer primary key autoincrement,
        name text not null,
        path text not null,
        return_type text not null
    )
"""