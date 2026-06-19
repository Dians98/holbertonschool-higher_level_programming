#!/usr/bin/python3
"""
Lists all states from the database, using SQLAlchemy ORM.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    state_name = sys.argv[4]

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(
        State.id).filter(State.name == state_name).first()

    if state is None:
        print("Not found")
    else:
        print(state.id)
    session.close()
