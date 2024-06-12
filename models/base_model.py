#!/usr/bin/python3
"""
Contains class BaseModel
"""

from datetime import datetime
import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid

time = "%Y-%m-%dT%H:%M:%S.%f"

if models.storage_t == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """The BaseModel class from which future classes will be derived"""
    if models.storage_t == "db":
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self, save_fs=None):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        if save_fs is None:
            if "password" in new_dict:
                del new_dict["password"]
        return new_dict

    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)
# #!/usr/bin/python3
# """This module defines a base class for all models in our hbnb clone"""
# import uuid
# from sqlalchemy.ext.declarative import declarative_base
# from datetime import datetime
# from sqlalchemy import Column, String, DateTime
# Base = declarative_base()

# class BaseModel:
#     """A base class for all hbnb models"""
#     id = Column(String(60), unique=True,
#                 nullable=False, primary_key=True)
#     created_at = Column(
#         DateTime, nullable=False, default=datetime.utcnow())
#     updated_at = Column(
#         DateTime, nullable=False, default=datetime.utcnow())

#     # def __init__(self, *args, **kwargs):
#     #     """Instantiates a new model"""
#     #     if not kwargs:
#     #         from models import storage
#     #         self.id = str(uuid.uuid4())
#     #         self.created_at = datetime.now()
#     #         self.updated_at = datetime.now()
#     #     else:
#     #         if 'updated_at' in kwargs:
#     #             kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
#     #         if 'created_at' in kwargs:
#     #             kwargs['created_at'] = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
#     #         if '__class__' in kwargs:
#     #             del kwargs['__class__']
#     #         for key, value in kwargs.items():
#     #             if not hasattr(self, key):
#     #                 setattr(self, key, value)

#     def __init__(self, *args, **kwargs):
#         """Instatntiates a new model"""
#         if not kwargs:
#             self.id = str(uuid.uuid4())
#             self.created_at = datetime.now()
#             self.updated_at = self.created_at
#         elif 'id' not in kwargs:
#             self.id = str(uuid.uuid4())
#             self.created_at = datetime.now()
#             self.updated_at = self.created_at
#             self.__dict__.update(kwargs)
#         else:
#             kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
#                                                      '%Y-%m-%dT%H:%M:%S.%f')
#             kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
#                                                      '%Y-%m-%dT%H:%M:%S.%f')
#             del kwargs['__class__']
#             self.__dict__.update(kwargs)

#     def __str__(self):
#         """Returns a string representation of the instance"""
#         cls = (str(type(self)).split('.')[-1]).split('\'')[0]
#         return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

#     def save(self):
#         """Updates updated_at with current time when instance is changed"""
#         from models import storage
#         self.updated_at = datetime.now()
#         storage.new(self)
#         storage.save()

#     def to_dict(self):
#         """Convert instance into dict format"""
#         dictionary = {}
#         dictionary.update(self.__dict__.copy())
#         if '_sa_instance_state' in dictionary:
#             del dictionary['_sa_instance_state']
#         dictionary.update({'__class__':
#                           (str(type(self)).split('.')[-1]).split('\'')[0]})
#         dictionary['created_at'] = self.created_at.isoformat()
#         dictionary['updated_at'] = self.updated_at.isoformat()
#         return dictionary

#     def delete(self):
#         """delete the current instance from the storage"""
#         from models import storage
#         storage.delete(self)