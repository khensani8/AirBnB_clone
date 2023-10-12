#!/usr/bin/python3
"""defines the FileStorage class"""
import json
from models.base_model import BaseModel


class FileStorage:
	"""Respresents an abstract storage engine"""
	
	Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
	"""
	__file_path = file.json
	__objects = {}
	
	def all(self):
		"""returns the dictionary __objects"""
		return self.__ojects

	def new(self, obj):
	"""sets in __objects the obj with key <obj class name>.id"""
		key = "{}.{}".format(obj.__class__.__name__, obj.id)
		self.__objects[key] = obj

	def save(self):
		"""Serialize __objects to the JSON file __file_path."""
		objdict = {k: v.to_dict() for k, v in self.__objects.items()}
		with open(self.__file_path, 'w') as file:
            		json.dump(objdict, file)

	def reload(self):
	"""deserialises JSON file to __objects"""
		if os.path.exists(self.__file_path):
			with open(self.__file_path, 'r', encoding='utf-8') as file:
			new_dict = json.load(file)
				for key, value in new_dict.items():
					class_name, obj_id = key.split('.')
					class_ = globals()[class_name]
					obj = class_(**value)
					self.new(obj)
