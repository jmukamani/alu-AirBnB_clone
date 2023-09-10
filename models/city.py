#!/usr/bin/python
""" holds class City"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime
import time


class City(BaseModel, Base):
    """Represents a city"""
    if models.storage_t == "db":
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", backref="cities")
    else:
        name = ""
        state_id = ""

    def __init__(self, *args, **kwargs):
        """Initializes a new city"""
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
