#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey

class City(BaseModel):
    """ The city class, contains state ID and name """
     __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete', backref='state')
    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """Cities getter"""
            from models.city import City
            from models import storage
            list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    list.append(city)
            return list