import os
import zipfile
from pathlib import Path
from typing import List, Optional


class DataRecover:
    def __init__(self):
        self.data_dir = Path.cwd() / 'data'

    def recover_directories(self) -> List[str]:
        if not self.data_dir.exists():
            return []

        return [dir.name for dir in self.data_dir.iterdir() if dir.is_dir()]

    def get_directory_path_by_name(self, name: str) -> Optional[Path]:
        directory_path = self.data_dir / name
        return directory_path if directory_path.is_dir() else None

    def zip_directory(self, directory_path: Path) -> Path:
        zip_path = directory_path.with_suffix('.zip')

        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(directory_path):
                for file in files:
                    file_path = Path(root) / file
                    arcname = file_path.relative_to(directory_path)
                    zipf.write(file_path, arcname)

        return zip_path

    def zip_directory_by_name(self, name: str) -> Optional[str]:
        directory_path = self.get_directory_path_by_name(name)
        if not directory_path:
            return None

        zip_path = self.zip_directory(directory_path)
        return str(zip_path)

    def delete_zip_files(self):
        for zip_file in self.data_dir.glob('*.zip'):
            zip_file.unlink()