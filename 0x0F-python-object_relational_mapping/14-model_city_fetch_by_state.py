#!/usr/bin/python3
"""
Script that lists all City objects from the database
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)

if __name__ == "__main__":

    user = argv[1]
    password = argv[2]
    database = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (user, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    new_table = session.query(City, State)\
        .filter(City.state_id == State.id)\
        .order_by(City.id.asc()).all()

    for cities, states in new_table:
        print("{}: ({}) {}".format(states.name, cities.id, cities.name))
    session.close()
