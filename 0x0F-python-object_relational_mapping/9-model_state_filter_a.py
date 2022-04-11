#!/usr/bin/python3
"""module doc"""
import sys
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)
    Base.metadate.create_all(engine)
    session = Session(engine)
    for state in session.query(State).order_by(State.id).all():
        if 'a' in state.name or 'A' in state.name:
            print("{}: {}".format(state.id, state.name,))
