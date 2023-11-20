#!/usr/bin/python3
"""lists all State objects that contain the letter a"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
    .format(sys.arv[1], sys.argv[2], sys.argv[3]))
    
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states_a = session.query(State).filter(State.name.like('%a%'))
    for state in states_a:
        print("{}: {}".format(state.id, state.name))
    
    session.close()