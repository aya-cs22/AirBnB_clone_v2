#!/usr/bin/python3
"""a script for DB Storage Engine"""
import os
from models.base_model import Base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User


class DBStorage():
    """create the engine to be linked to the MySQL
    database
    """

    __engine = None
    __session = None

    def __init__(self):
        """Instantiation of engine"""

        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv("HBNB_ENV")

        db_url = "mysql+mysqldb://{}:{}@{}/{}".format(
            user, password, host, database)

        engine = create_engine(db_url, pool_pre_ping=True)

        self.__engine = engine
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session
        (self.__session) all objects depending of the class
        name (cls)"""
        obj_list = ['User', 'State', 'City', 'Amenity', 'Place', 'Review']
        objects = []

        if cls is not None:
            objects.extend(self.__session.query(cls).all())  # objects
        else:
            for item in obj_list:
                objects.extend(self.__session.query(item).all())

        dict = {}
        for obj in objects:
            k = f"{obj.__class__.__name__}.{obj.id}"
            dict[k] = obj

        return dict

    def new(self, obj):
        """add the object to the current database session (self.__session)"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the current database session."""
        self.__session.close()
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