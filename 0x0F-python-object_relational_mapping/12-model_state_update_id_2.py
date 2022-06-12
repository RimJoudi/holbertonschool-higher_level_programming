#!/usr/bin/python3
"""
Script that changes the name of the state object in the database
"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

if __name__ == "__main__":

    user = argv[1]
    password = argv[2]
    database = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (user, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    new_state = session.query(State).filter_by(id=2).first()
    new_state.name = 'New Mexico'
    session.add(new_state)
    session.commit()
    session.close()
