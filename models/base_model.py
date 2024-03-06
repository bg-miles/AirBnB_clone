import uuid
import datetime


class BaseModel:

    def __init__(self, *arg, **kwargs):
        if kwargs is not None and kwargs != {}:
            for attr in kwargs:
                if attr == "created_at":
                    self.__dict__["created_at"] = datetime.datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
                    )
                elif attr == "updated_at":
                    self.__dict__["updated_at"] = datetime.datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"
                    )
                else:
                    self.__dict__[attr] = kwargs[attr]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        dict_class = self.__dict__
        dict_class["__class__"] = self.__class__.__name__
        dict_class["created_at"] = dict_class["created_at"].isoformat()
        dict_class["updated_at"] = dict_class["updated_at"].isoformat()
        return dict_class

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
