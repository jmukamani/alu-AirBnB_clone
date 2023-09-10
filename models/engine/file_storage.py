#!/usr/bin/python3
"""Contains the class FileStorage"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os.path
import json


class FileStorage:
    """serializes instances to a JSON file and deserializes JSON file to instances"""
    # __file_path = "file.json"
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj
    
    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        obdict = FileStorage.__objects
        objdict = {}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(objdict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = jo[key]
        except FileNotFoundError:
            pass