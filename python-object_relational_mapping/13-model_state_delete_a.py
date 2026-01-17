#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter a
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

    # Filter for states containing 'a' and delete them
    session.query(State).filter(State.name.like('%a%')).delete(
        synchronize_session='fetch'
    )

    session.commit()
    session.close()


if __name__ == "__main__":
    main()
