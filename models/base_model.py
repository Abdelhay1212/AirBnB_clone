#!/usr/bin/python3
"""This module defines a base class for all models in our HBNB clone."""

import uuid
import models
from datetime import datetime


class BaseModel:
    """BaseModel class defines common attributes and methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initialize the BaseModel instance.

        Args:
            *args: Variable-length argument list (not used in this implementation).
            **kwargs: Keyword arguments used for object initialization, if provided.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key in ("updated_at", "created_at"):
                    self.__dict__[key] = datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key[0] == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """Update the updated_at attribute with the current datetime and save changes."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance.

        Returns:
            dict: A dictionary containing the instance's attributes and values.
        """
        dictionary = {**self.__dict__}
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = dictionary['created_at'].isoformat()
        dictionary['updated_at'] = dictionary['updated_at'].isoformat()

        return dictionary

    def __str__(self):
        """Return a string representation of the instance.

        Returns:
            str: A formatted string with class name, instance ID, and attribute dictionary.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
