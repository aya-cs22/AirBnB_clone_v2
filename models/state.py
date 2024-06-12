#!/usr/bin/python3
""" holds class State"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Representation of state """
    if models.storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City",
                              backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if models.storage_t != "db":
        @property
        def cities(self):
            """getter for list of city instances related to the state"""
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
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
