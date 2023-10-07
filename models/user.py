#!/usr/bin/python3
""" User Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

class User(BaseModel, Base):
    """ User class """
    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        places = relationship("Place", backref="user", cascade="all, delete-orphan")
        reviews = relationship("Review", backref="user", cascade="all, delete-orphan")
    else:
        @property
        def places(self):
            """Getter attribute to list all related places of the user"""
            from models import storage
            all_places = storage.all("Place")
            user_places = [place for place in all_places.values() if place.user_id == self.id]
            return user_places

        @property
        def reviews(self):
            """Getter attribute to list all related reviews of the user"""
            from models import storage
            all_reviews = storage.all("Review")
            user_reviews = [review for review in all_reviews.values() if review.user_id == self.id]
            return user_reviews
