from pathlib import Path


class FileScanner:
    def __init__(self, source_dir):
        self.source_dir = Path(source_dir)

    def scan_files(self):
        files = []

        for file in self.source_dir.rglob("*"):
            if file.is_file():
                files.append(file)

        return files
