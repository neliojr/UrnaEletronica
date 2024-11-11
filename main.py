import json
from TUI.main import TUI

class Config:
    def __init__(self, section, enable_gui, admin_pass):
        self.section = section
        self.enable_gui = enable_gui
        self.admin_pass = admin_pass

class ConfigManager:
    def __init__(self):
        self.config = []
        self.database = './data/config.json'
        self.load()

    # carregar as configurações para a RAM.
    def load(self):
        try:
            with open(self.database, 'r') as file:
                data = json.load(file)

                for item in data['config']:
                    config = Config(item['section'], item['enable_gui'], item['admin_pass'])
                    self.config.append(config)
        except: # criando arquio JSON caso não exista.
            data = {
                "config": [
                    {
                        "section": 1,
                        "enable_gui": False,
                        "admin_pass": "1234"
                    }
                ]
            }

            with open(self.database, 'w') as file:
                json.dump(data, file, indent=4)

    
    def get(self):
        for config in self.config:
            return {
                'section': config.section,
                'enable_gui': config.enable_gui,
                'admin_pass': config.admin_pass
            }
        return None

config = ConfigManager()

def select_ui(enable_gui):
    if enable_gui:
        pass
    else:
        TUI().menu()

try:
    select_ui(config.get()['enable_gui'])
except:
    config = ConfigManager()
    select_ui(config.get()['enable_gui'])