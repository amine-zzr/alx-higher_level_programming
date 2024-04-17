#!/usr/bin/python3
"""listing all City objects from a database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":

    username, password, db_name = sys.argv[1:]
    engine = create_engine(
            f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}")

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    session.close()
