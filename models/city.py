#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship
from models.base_model import Base
import os


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        state = relationship('State', back_populates='cities')
        places = relationship('Place', backref='cities',
                              cascade='all, delete, delete-orphan')
    else:
        name = ""
        state_id = ""

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Returns an empty list for non-DB storage."""
            return []
# #!/usr/bin/python3
# """ City Module for HBNB project """
# from models.base_model import BaseModel
# from sqlalchemy.orm import relationship
# from sqlalchemy import Column, String, ForeignKey

# class City(BaseModel):
#     """ The city class, contains state ID and name """
#     __tablename__ = 'cities'
#     name = Column(String(128), nullable=False)
#     state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
