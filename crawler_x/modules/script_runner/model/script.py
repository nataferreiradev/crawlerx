from dataclasses import dataclass

@dataclass
class Script:
    table_name = 'scriptTable'

    id: int = None
    name: str = ''
    path: str = ''
    return_type: str = 'txt'
