#!/usr/bin/python3
"""python file that contains the class definition of a State"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymeta = MetaData()
Base = declarative_base(metadata=mymeta)

class State(Base):
   """class with id and name"""
   __tablename__ = 'states'
   id = Column(Integer, primary_key=True, nullable=False, unique=True)
   name = Column(String(128), nullable=False)
