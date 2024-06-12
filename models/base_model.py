#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from datetime import datetime
import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()

class BaseModel:
    """A base class"""
    id = Column(String(60), unique=True,
                nullable=False, primary_key=True)
    created_at = Column(
        DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(
        DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
        elif 'id' not in kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            self.__dict__.update(kwargs)
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation"""
        _dict = self.__dict__.copy()
        if '_sa_instance_state' in _dict:
            del _dict['_sa_instance_state']
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return (f'[{cls}] ({self.id}) {_dict}')

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        _dict = {}
        _dict.update(self.__dict__.copy())
        if '_sa_instance_state' in _dict:
            del _dict['_sa_instance_state']
        _dict.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        _dict['created_at'] = self.created_at.isoformat()
        _dict['updated_at'] = self.updated_at.isoformat()
        return _dict

    def delete(self):
        """del"""
        from models import storage
        storage.delete(self)
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