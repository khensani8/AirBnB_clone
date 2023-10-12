#!/usr/bin/python3
"""BaseModel that defines all common attributes/methods for other classes"""


import uuid
from datetime import datetime
improt models

class BaseModel:
	"""class BaseModel"""
     def __init__(self, *args, **kwargs):
		""" class consturctor for class BaseModel"""
		if kwargs:
			kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
			kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
			
			for key, value in kwargs.items():
                		if key != '__class__':
                    			setattr(self, key, value)
		else:
			self.id = str(uuid.uuid4())
        		self.created_at = datetime.now()
        		self.updated_at = self.created_at

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
