#!/usr/bin/python3
'''
    This module contains the definition of the BaseModel class
'''

import uuid
import datetime
from models import storage

class BaseModel:
    '''
    Class BaseModel that defines all common attributes/methods
    for other classes

    Attributes:
        id (str): A unique identifier for the instance.
        created_at (datetime): The datetime when the instance is created.
        updated_at (datetime): The datetime when the instance is updated.

    Methods:
        __init__: Initializes a new instance of the BaseModel class.
        __str__: Returns a string representation of the BaseModel instance.
        save: Updates the updated_at attribute and saves the instance.
        to_dict: Returns a dictionary representation of the instance.
    '''
    def __init__(self, *args, **kwargs):
        '''Public instance attributes'''
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)
        else:
            kwargs['created_at'] = datetime.datetime.strptime(
                kwargs['created_at'],
                "%Y-%m-%dT%H:%M:%S.%f"
            )
            kwargs['updated_at'] = datetime.datetime.strptime(
                kwargs['updated_at'],
                "%Y-%m-%dT%H:%M:%S.%f"
            )
            for key, val in kwargs.items():
                if key != '__class__':
                    setattr(self, key, val)

    def __str__(self):
        '''
        Return a string representation of BaseModel class
        '''
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__
        )
    
    def save(self):
        '''
        Update the public instance attribute updated_at
        with the current datetime and save the instance
        '''
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        '''
        Return a dictionary containing all keys/values
        of __dict__ of the instance
        '''
        dct_instance = self.__dict__.copy()
        dct_instance['__class__'] = self.__class__.__name__
        dct_instance['created_at'] = self.created_at.isoformat()
        dct_instance['updated_at'] = self.updated_at.isoformat()
        return dct_instance
