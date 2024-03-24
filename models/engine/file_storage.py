#!/usr/bin/python3
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
        key = f"{obj.__class__.name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file.
        """
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects if __file path
        exists.
        """
        if path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
