from dataclasses import dataclass

@dataclass
class ApiObject:
    table_name = 'apiTable'

    id: int = None
    name: str = ''
    url: str = ''
    method: str = ''
    headers: dict = None
    body: str = ''  
    params: dict = None
