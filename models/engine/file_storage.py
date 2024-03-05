#from command import BaseModel
import json
class FileStorage:
    def __init__(self, file_path, objects):
        self.__file_path = file_path
        self.__objects = objects


    def all(self):
        return self.__objects
    def new(self, obj):
        pass
    def save(self):
        pass
    def reload(self):
        pass