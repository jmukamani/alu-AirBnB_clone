#!/usr/bin/python3
"""defines the class attributes"""
from models.base_model import BaseModel


class State(BaseModel):
    """Class that defines states"""
    name = ""
    cities = []
