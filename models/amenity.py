#!/usr/bin/python
""" holds class Amenity"""
from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """Amenity class"""

    name = ""
