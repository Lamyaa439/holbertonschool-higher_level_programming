#!/usr/bin/python3
"""
Changes the name of a State object from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            user, passwd, db_name
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve the state with id 2
    state_to_update = session.query(State).filter(State.id == 2).first()

    # Update the name if the state exists
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    session.close()


if __name__ == "__main__":
    main()
