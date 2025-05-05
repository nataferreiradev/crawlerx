from dataclasses import dataclass,field

@dataclass
class ApiObject:
    table_name = 'apiTable'

    id: int = None
    name: str = ''
    url: str = ''
    method: str = ''
    headers: dict = field(default_factory=dict, metadata={"json": True})
    body: str = ''
    params: dict = field(default_factory=dict, metadata={"json": True})
    return_type: str = 'txt'