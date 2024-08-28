# Williams Villalba _ January,19th 2022
import os
import json

class config:

    __config_filename = ['assets','config','config.json']

    __instance = None

    @staticmethod
    def  get_instance():
        if config.__instance is None:
            config()
        return config.__instance
        

    def __init__(self):
        if config.__instance is None:
            config.__instance = self

            with open(os.path.join(*config.__config_filename)) as file:
                self.data = json.load(file)


        else:
            raise Exception("Configuration can not have multiple instances")