from colorama import Fore

import requests
import yaml


class Config:
    def read(self):
        try:
            file = open("./config/config.yaml", 'r', encoding='utf8')
        except FileNotFoundError:
            print(Fore.RED + 'Error: config.yaml file not found, rename EXAMPLE-config.yaml to config.yaml inside /config folder' + Fore.RESET)
            exit()

        with file as s:
            stream = s.read()
        return yaml.safe_load(stream)

    def readGitHubExample(self):
        data = requests.get(
            url='https://raw.githubusercontent.com/newerton/sunflower-land-bot/main/config/EXAMPLE-config.yaml', timeout=2)
        try:
            configExample = yaml.safe_load(data.text)
        except FileNotFoundError:
            self.log.console(
                'Config example file not found in GitHub', emoji='💥', color='red')
            configExample = None

        return configExample
