#!/usr/bin/python
""" holds class Review"""

from models.base_model import BaseModel


class Review(BaseModel, Base):
    """Review class"""
    place_id = ""
    user_id = ""
    text = ""