class MediaOrganizer:
    def __init__(self, scanner, categorizer, mover):
        self.scanner = scanner
        self.categorizer = categorizer
        self.file_mover = mover

    def organize(self):
        files = self.scanner.scan_files()

        for file in files:
            category = self.categorizer.get_category(file)
            self.file_mover.move_file(file, category)
