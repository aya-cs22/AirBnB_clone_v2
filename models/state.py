#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
import os
import models
from models.city import City  # Import the City class
import shlex


from models.base_model import Base


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade='all, delete, delete-orphan',
                              back_populates="state")

    else:
        @property
        def cities(self):
            var = models.storage.all()
            lista = []
            result = []
            for key in var:
                city = key.replace('.', ' ')
                city = shlex.split(city)
                if (city[0] == 'City'):
                    lista.append(var[key])
            for elem in lista:
                if (elem.state_id == self.id):
                    result.append(elem)
            return result
# #!/usr/bin/python3
# """ State Module for HBNB project """
# from os import getenv
# from models.base_model import BaseModel
# from sqlalchemy.orm import relationship
# from sqlalchemy import Column, String, ForeignKey

# class State(BaseModel):
#     """ State class """
#     __tablename__ = 'states'
#     name = Column(String(128), nullable=False)
#     cities = relationship('City', cascade='all, delete', backref='state')
#     if getenv('HBNB_TYPE_STORAGE') != 'db':
#         @property
#         def cities(self):
#             """Cities getter"""
#             from models.city import City
#             from models import storage
#             list = []
#             for city in storage.all(City).values():
#                 if city.state_id == self.id:
#                     list.append(city)
#             return list
