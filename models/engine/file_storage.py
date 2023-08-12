# /usr/bin/python3
"""This module provides a FileStorage class for serializing instances to a JSON file and deserializing JSON files to instances."""

import os
import json
from models.base_model import BaseModel


class FileStorage:
    """A class that handles serialization and deserialization of data using JSON."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of objects.

        Returns:
            dict: A dictionary containing the stored objects.
        """
        return self.__objects

    def new(self, obj):
        """sets in __objects the object with the key
        <object class name>.id

        Args:
            object(obj): object to write

        """
        self.__objects[obj.__class__.__name__ + '.' + str(obj)] = obj

    def save(self):
        """Serialize and save the data to the JSON file."""
        with open(self.__file_path, 'w+') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """Deserialize and reload data from the JSON file, if it exists."""
        try:
            with open(self.__file_path, 'r') as f:
                dict = json.loads(f.read())
                for value in dict.values():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
        except Exception:
            pass
