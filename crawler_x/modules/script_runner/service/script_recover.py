import os
from pathlib import Path

class ScriptRecover():
    def __init__(self):
        self.data_dir = Path.cwd()


    def get_file_path(self, script_path: str) -> Path | None:
        full_path = self.data_dir / script_path

        if full_path.exists() and full_path.is_file():
            return full_path
        return None
