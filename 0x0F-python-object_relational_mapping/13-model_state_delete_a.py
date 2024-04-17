#!/usr/bin/python3
"""deleting all State objects with a name containing
    the letter `a` from a database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
            f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}")
    Base.metadata.bind = engine

    Session = sessionmaker(bind=engine)
    session = Session()

    to_delete = session.query(
                    State).filter(
                        State.name.like('%a%')).all()

    for state in to_delete:
        session.delete(state)

    session.commit()
    session.close()
