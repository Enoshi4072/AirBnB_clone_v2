#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from os import getenv

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        places = relationship("Place", backref="cities", cascade="all, delete-orphan")
    else:
        @property
        def places(self):
            """Getter attribute to list all related places in the city"""
            from models import storage
            all_places = storage.all("Place")
            city_places = [place for place in all_places.values() if place.city_id == self.id]
            return city_places
