#!/usr/bin/python3
"""Contains the class User"""
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """Class that defines a user"""
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""     