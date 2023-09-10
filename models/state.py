#!/usr/bin/python3
"""defines the class attributes"""
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """Class that defines states"""
    name = ""
    cities = []