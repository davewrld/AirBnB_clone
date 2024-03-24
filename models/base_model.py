#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:

    """
    Base class that defines all commnon attributes/methods for other classes
    Goal is to have unique id for each BaseModel

    Public instance attribute:
        id: string - unqique identifier - uuid.uuid4()
        created_at - datetime when instance was created.
        updated_at - datetime when instance eas last updated.
    Public insance methods:
        save(self) - updates public instance attribute.
        to_dict(self) - Returns a dictionary of  __dict__ instance.
        __str__() - Returns string representation of the object.
    """
    def __init__(self):
        """
        Initializes BaseModel instance and assigns attributes.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """
        Updates the update_at attribute with current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns:
            A dictionary containning all instance attributes and their values.
        """
        dict_output = self.__dict__.copy()
        dict_output["__class__"] = self.__class__.__name__
        dict_output["created_at"] = self.created_at.isoformat()
        dict_output["updated_at"] = self.updated_at.isoformat()
        return dict_output

    def __str__(self):
        """
        Returns:
            A string representation of the object.
            Containing class name, id and attrubute dictionary.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
