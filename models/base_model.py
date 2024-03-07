#!/usr/bin/python3

import uuid
import datetime
from models import storage


class BaseModel:

    def __init__(self, *arg, **kwargs):
        if kwargs is not None and kwargs != {}:
            for attr, value in kwargs.items():
                if attr == "created_at" or attr == "updated_at":
                    date_string = "%Y-%m-%dT%H:%M:%S.%f"
                    self.__dict__[attr] = datetime.datetime.strptime(value, date_string)
                else:
                    self.__dict__[attr] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def save(self):
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        dict_class = self.__dict__.copy()
        dict_class["__class__"] = type(self).__name__
        dict_class["created_at"] = dict_class["created_at"].isoformat()
        dict_class["updated_at"] = dict_class["updated_at"].isoformat()
        return dict_class

    def __str__(self):
        cl_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cl_name, self.id, self.__dict__)
