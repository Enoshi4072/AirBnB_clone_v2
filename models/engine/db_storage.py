#!/usr/bin/python3
""" new class for sqlAlchemy """
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """ create tables in environmental"""
    __engine = None
    __session = None

    def __init__(self):
        db_user = getenv("HBNB_MYSQL_USER")
        db_passwd = getenv("HBNB_MYSQL_PWD")
        db_name = getenv("HBNB_MYSQL_DB")
        db_host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(db_user, db_passwd, db_host, db_name),
                                      pool_pre_ping=True)
        """ Drop all tables if HBNB_ENV is 'test' """
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        result = {}
    
        if cls:
            # Convert class name as a string to an actual class if needed
            if isinstance(cls, str):
                cls = eval(cls)
            
            # Query for objects of the specified class
            query = self.__session.query(cls)
            for obj in query:
                key = f"{obj.__class__.__name__}.{obj.id}"
                result[key] = obj
        else:
            # List of classes to query for all types of objects
            classes_to_query = [State, City, User, Place, Review, Amenity]
            for model_class in classes_to_query:
                query = self.__session.query(model_class)
                for obj in query:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    result[key] = obj

        return result

    def new(self, obj):
        """add a new element in the table
        """
        self.__session.add(obj)

    def save(self):
        """save changes
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete an element in the table
        """
        if obj:
            self.session.delete(obj)

    def reload(self):
        """Initialize database and session.
        """
        # Create all database tables
        Base.metadata.create_all(self.__engine)

        # Initialize a new session with the engine
        session_maker = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_maker)

    def close(self):
        """ calls remove()
        """
        self.__session.close()
