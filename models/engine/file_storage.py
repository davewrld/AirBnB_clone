#!/usr/bin/python3
"""
file storage Engine
"""
import json
from os import path
from models.base_model import BaseModel


class FileStorage:
    """
    Serializes instances to JSON file and
    deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns:
            The dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file.
        """
        with open(self.__file_path, "w") as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects if __file path
        exists.
        """
        try:
            with open(self.__file_path, "r") as f:
                obj_dict = json.loads(f)
                for key, val in obj_dict.items():
                    class_name = val['__class__']
                    obj = eval(class_name)(**val)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
