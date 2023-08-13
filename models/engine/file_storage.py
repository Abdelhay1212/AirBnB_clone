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
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize and save the data to the JSON file."""
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """Deserialize and reload data from the JSON file, if it exists."""

        current_classes = {'BaseModel': BaseModel}

        if not os.path.exists(self.__file_path):
            return

        with open(self.__file_path, 'r') as f:
            deserialized = None

            try:
                deserialized = json.load(f)
            except Exception:
                pass

            if deserialized is None:
                return

            FileStorage.__objects = {
                k: current_classes[k.split('.')[0]](**v)
                for k, v in deserialized.items()}
