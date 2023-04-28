#!/usr/bin/python3
"""
Script that lists all City objects from the database hbtn_0e_101_usa
"""
import sys
from relationship_city import Base, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    """ Create engine to connect to MySQL server """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    """ Create session """
    Session = sessionmaker(bind=engine)
    session = Session()

    """ 
     Query the database for all City objects and their associated State objects 
    """
    cities = session.query(City).order_by(City.id)

    """ Print the results """
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    """ Close the session """
    session.close()
