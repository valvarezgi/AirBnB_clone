#!/usr/bin/python3
"""Module FileStorage"""

import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """Class FileStorage"""

    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        """init"""
        pass

    def all(self):
        """all -  returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """new - sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects["{}.{}".format(
            obj.__class__.__name__, obj.id)] = obj
        """__objects[class.id] = obj → debug"""

    def save(self):
        """save - serializes __objects to the JSON file"""
        json_file = {}
        with open(FileStorage.__file_path, "w", encoding='utf-8') as jfile:
            for key, value in self.__objects.items():
                json_file[key] = value.to_dict()
            json.dump(json_file, jfile)

    def reload(self):
        """reload - deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as jfile:
                jdict = json.load(jfile)
            for key, value in jdict.items():
                classes = key.split(".")
                FileStorage.__objects[key] = globals()[classes[0]](**value)

        except:
            pass
