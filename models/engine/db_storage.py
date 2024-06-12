#!/usr/bin/python3
""" creating a database using sql with python"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session , sessionmaker , scoped_session
from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import BaseModel , Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from datetime import datetime


# script that prints the State object with the name
# passed as argument from the database hbtn_0e_6_usa
class DBStorage ():
    """ the new engine"""
    __engine=None
    __session=None
    def __init__(self):
        """constructor of engine"""
        user = os.getenv('HBNB_MYSQL_USER')
        paswd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine("mysql+mysqldb://"+user+':'+paswd+'@'+host+'/'+database, pool_pre_ping=True,)
        if os.getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)
        # Base.metadata.create_all(self.__engine)
        # session = sessionmaker(self.__engine)
        # self.__session = scoped_session(session)

            
    def all(self, cls=None):
        """get all data on the current session"""
        dict_ins = {}
        name = cls.__name__
        
        if cls:
            data = self.__session.query(cls).all()
            for i in data:
                key = name + '.'+ i.id
                dict[key] = i
            return dict_ins
        else:
            dict_ins = {}
            classes = {
                    'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
            for cls_name ,value in classes.items():
                data = self.__session.query(value).all()
                name = cls_name
                key = name + '.'+ value.id
                for i in data:
                    key = name + '.'+ i.id
                    dict[key] = i
            return dict_ins


    def new(self, obj):
        """ add the object to the current database session (self.__session) """
        # cls_name = obj.__class__.__name__
        self.__session.add(obj)


    def save(self):
        """commit all changes of the current database session (self.__session)"""
        self.__session.commit()


    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)
            # self.__session.commit()


    def reload(self):
        """import the data back"""
        Base.metadata.create_all(self.__engine)
        session_maker = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_maker)
        self.__session = Session()
# #!/usr/bin/python3
# """ DBStorage"""

# import models
# from models.amenity import Amenity
# from models.base_model import BaseModel, Base
# from models.city import City
# from models.place import Place
# from models.review import Review
# from models.state import State
# from models.user import User
# from os import getenv
# import sqlalchemy
# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker

# class DBStorage:
#     """interaacts with the MySQL database"""
#     __engine = None
#     __session = None
#     classes = {"Amenity": Amenity, "City": City,
#                "Place": Place, "Review": Review, "State": State, "User": User}
    
#     def __init__(self):
#         """Instantiate a DBStorage"""
#         HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
#         HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
#         HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
#         HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
#         HBNB_ENV = getenv('HBNB_ENV')
#         self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
#                                       format(HBNB_MYSQL_USER,
#                                              HBNB_MYSQL_PWD,
#                                              HBNB_MYSQL_HOST,
#                                              HBNB_MYSQL_DB),
#                                       pool_pre_ping=True
#                                       )
#         if HBNB_ENV == "test":
#             Base.metadata.drop_all(self.__engine)

#     def all(self, cls=None):
#         """query on the current database session"""
#         new_dict = {}
#         for clss in self.classes:
#             if cls is None or cls is self.classes[clss] or cls is clss:
#                 objs = self.__session.query(self.classes[clss]).all()
#                 for obj in objs:
#                     key = obj.__class__.__name__ + '.' + obj.id
#                     new_dict[key] = obj
#         return (new_dict)

#     def new(self, obj):
#         """add the object to the current database session"""
#         self.__session.add(obj)

#     def save(self):
#         """commit all changes of the current database session"""
#         self.__session.commit()

#     def delete(self, obj=None):
#         """delete from the current database session obj if not None"""
#         if obj is not None:
#             self.__session.delete(obj)

#     def reload(self):
#         """reloads data from the database"""
#         Base.metadata.create_all(self.__engine)
#         sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
#         Session = scoped_session(sess_factory)
#         self.__session = Session

#     def close(self):
#         """call remove() method on the private session attribute"""
#         self.__session.close()