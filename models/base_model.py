#!usr/bin/python3
"""Defines all common attributes/methods for other classes."""

from datetime import datetime
import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid

time = "%Y-%m-%dT%H:%M:%S.%f"

if models.storage_t == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """Class from which the future classes will be derived"""
    if models.storage_t == "db":
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime, default=datetime.utcnow())
        updated_at = Column(DateTime, default=datetime.utcnow())

        def __init__(self, *args, **kwargs):
            """Instantiates a new model"""
            if kwargs:
                for key, value in kwargs.items():
                    if key != "__class__":
                        setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
            else:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.utcnow()
                self.updated_at = self.created_at

        def __str__(self):
            """Returns a string representation of the instance"""
            return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

        def save(self):
            """Updates updated_at with current time when instance is changed"""
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
            models.storage.save()

        def to_dict(self):
            """Convert instance into dict format"""
            new_dict = self.__dict__.copy()
            if "created_at" in new_dict:
                new_dict["created_at"] = new_dict["created_at"].strftime(time)
            if "updated_at" in new_dict:
                new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
            new_dict["__class__"] = self.__class__.__name__
            if "_sa_instance_state" in new_dict:
                del new_dict["_sa_instance_state"]
            return new_dict

        def delete(self):
            """Delete the current instance from the storage"""
            models.storage.delete(self)
