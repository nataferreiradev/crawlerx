dataBaseName = "crawler.db"
dataBasePath = "crawler_x/dataBase/"

apiTableScript = """
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

scriptTableScript = """
    create table if not exists scriptTable(
        id integer primary key autoincrement,
        name text not null,
        path text not null
    )
"""