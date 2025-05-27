import os
from pathlib import Path
from .script_runner import scripts_dir

class ScriptManager():
    def __init__(self):
        self.data_dir = Path.cwd()

    def get_file_path(self, script_path: str) -> Path | None:

        full_path = self.data_dir / script_path

        if full_path.exists() and full_path.is_file():
            return full_path
        raise FileNotFoundError(f"Arquivo '{script_path}' não encontrado.")


    def delete_file(self, script_path: str) -> bool:
        full_path = self.data_dir / script_path

        if full_path.exists() and full_path.is_file():
            os.remove(full_path)
            return True
        else:
            raise FileNotFoundError("File not found")
    
    def save_file(self,file_name:str, file_content: bytes):
        if not file_name:
            raise ValueError("O nome do arquivo não pode ser vazio ou None.")

        full_path = self.data_dir / scripts_dir / f"{file_name}.py"
        print("Saving file to:", full_path)
        

        if not full_path.parent.exists():
            print("Creating directory:", full_path.parent)
            full_path.parent.mkdir(parents=True, exist_ok=True)

        with open(full_path, 'wb') as file:
            print("Writing content to file")
            if not isinstance(file_content, bytes):
                raise TypeError("file_content must be of type bytes")
            file.write(file_content)
        return Path(scripts_dir) / f"{file_name}.py"

    def recreate_file(self, script_path: str, file_content: bytes) -> bool:
        full_path = self.data_dir / script_path
        print(full_path)

        if full_path.exists() and full_path.is_file():
            print("Recreating file at:", full_path)
            with open(full_path, 'wb') as file:
                print("Writing content to file")
                file.write(file_content)
            return True
        else:
            raise FileNotFoundError("File not found")
    
    def search_in_file_for_result_var(self, file_content: str) -> bool:
        result = "result" in file_content
        return result
