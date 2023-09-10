#!/usr/bin/python3
"""Contains the class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class that defines a user"""
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""     