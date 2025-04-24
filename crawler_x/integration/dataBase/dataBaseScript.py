data_base_name = "crawler.db"
data_base_path = "dataBase/"

api_table_script = """
    create table if not exists apiTable(
        id integer primary key autoincrement,
        name text not null,
        url text not null,
        method text not null,
        headers text,
        body text,
        params text
    )
"""

script_table_script = """
    create table if not exists scriptTable(
        id integer primary key autoincrement,
        name text not null,
        path text not null
    )
"""