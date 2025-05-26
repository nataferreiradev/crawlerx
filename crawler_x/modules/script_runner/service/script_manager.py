import os
from pathlib import Path

class ScriptManager():
    def __init__(self):
        self.data_dir = Path.cwd()

    def get_file_path(self, script_path: str) -> Path | None:
        full_path = self.data_dir / script_path

        if full_path.exists() and full_path.is_file():
            return full_path
        return None

    def delete_file(self, script_path: str) -> bool:
        full_path = self.data_dir / script_path

        if full_path.exists() and full_path.is_file():
            os.remove(full_path)
            return True
        else:
            raise FileNotFoundError("File not found")
    
    def save_file(self, file_name: str, file_content: bytes) -> str:
        full_path = self.data_dir / "scripts" / (file_name + ".py")
        if not full_path.parent.exists():
            full_path.parent.mkdir(parents=True, exist_ok=True)

        with open(full_path, 'wb') as file:
            file.write(file_content)
        
        return str(Path("scripts") / (file_name + ".py"))

    def recreate_file(self, script_path: str, file_content: bytes) -> bool:
        full_path = self.data_dir / script_path

        if full_path.exists() and full_path.is_file():
            with open(full_path, 'wb') as file:
                file.write(file_content)
            return True
        else:
            raise FileNotFoundError("File not found")