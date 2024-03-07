#!/usr/bin/python3

from os import path
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__class__, obj.id)
        self.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            object_dict = {}
            for key, value in FileStorage.__objects.items():
                object_dict[key] = (
                    value.to_dict() if hasattr(value, "to_dict") else value
                )
                json.dump(object_dict, f)

    def reload(self):
        if path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                dict_obj = json.load(f)
        return None
