from pathlib import Path

class Categorizer():
    def __init__(self, category_mapping):
        self.category_mapping = category_mapping

    def get_category(self, file):
        extention = Path(file).suffix.lower()

        for category, extentions in self.category_mapping.items():
            if extention in extentions:
                return category
        
        return "Other"