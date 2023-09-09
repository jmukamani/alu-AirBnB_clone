#!/usr/bin/python3
"""defines the class attributes"""
import models
from models.base_model import BaseModel, Base
from models.user import User
from models.city import City
import sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
from os import getenv
import uuid
from datetime import datetime
import time

class State(BaseModel, Base):
    """Class that defines states"""
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        name = ""
        cities = []
    def __init__(self, *args, **kwargs):
        """Instantiates a new state"""
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

    if models.storage_t != "db":
        @property
        def cities(self):
            """getter for cities"""
            list_cities = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    list_cities.append(city)
            return list_cities