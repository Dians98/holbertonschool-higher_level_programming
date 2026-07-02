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

    state_name = "New Mexico"

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name=state_name)
    existing_state = session.query(State).filter_by(id=2).first()

    if existing_state:
        # 2. Update the attribute
        existing_state.name = "New Mexico"

        # 3. Commit the changes (SQLAlchemy knows it was modified, so no .add() is needed)
        session.commit()

    session.close()
