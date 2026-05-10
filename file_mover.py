from pathlib import Path
import shutil


class FileMover:
    def __init__(self, destination_path):
        self.root = Path(destination_path)

    def move_file(self, file_path, category):
        destination_folder = self.root / category

        destination_folder.mkdir(parents=True, exist_ok=True)

        destination_path = destination_folder / file_path.name

        shutil.move(str(file_path), str(destination_path))

        return destination_path
