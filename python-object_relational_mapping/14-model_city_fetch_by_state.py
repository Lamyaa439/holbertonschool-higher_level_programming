#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa.
Results are displayed as: <state name>: (<city id>) <city name>
Sorted in ascending order by cities.id
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # get command line argument
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database
    ),
    pool_pre_ping= True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # query all cities with their associated states, sorted by city id
    results = session.query(City, State).join(State).order_by(City.id).all()

    # display results
    for city, state in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    
    session.close()