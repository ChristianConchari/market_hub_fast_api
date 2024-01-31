"""
This module contains the configuration for the database connection and the
session manager.
"""

from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DATABASE_NAME = "database.sqlite"
BASE_DIR = Path(__file__).parent.resolve()
DATABASE_URL = f"sqlite:///{BASE_DIR / DATABASE_NAME}"

engine = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()
