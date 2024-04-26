#!/usr/bin/python3
"""Script that creates the State "California" with the City "San Francisco"."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sys import argv

if __name__ == '__main__':
    user, password, db_name = argv[1], argv[2], argv[3]
    engine = create_engine(f'mysql+mysqldb://{user}:{password}\
                           @localhost:3306/{db_name}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='California')
    new_city = City(name='San Francisco', state=new_state)

    session.add(new_state)
    session.add(new_city)

    session.commit()
