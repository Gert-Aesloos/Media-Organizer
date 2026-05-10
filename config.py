import json


class ConfigManager:
    def __init__(self, config_path):
        self.config_path = config_path

    def load_config(self):
        with open(self.config_path, "r") as file:
            return json.load(file)
