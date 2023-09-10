#!/usr/bin/python
""" holds class Amenity"""
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """Amenity class"""
    if models.storage_t == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
    else:
        name = ""

        def __init__(self, *args, **kwargs):
            """initializes Amenity"""
            super().__init__(*args, **kwargs)
