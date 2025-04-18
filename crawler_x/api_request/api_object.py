from dataclasses import dataclass, asdict

@dataclass
class ApiObject():
    id: int = None
    url: str = ''
    name: str = ''
    params: dict = None
    headers: dict = None
    method: str = ''