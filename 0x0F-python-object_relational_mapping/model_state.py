#!/usr/bin/python3
"""
A python file that contains the class definition of a state
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """This class links to the `states` table of our database.
    Attributes:
        id (int): id of the state.
        name (str): name of the state.
    """

    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
