# Imports
from databases import Database
from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    MetaData,
    String,
    Table,
    create_engine
)
from sqlalchemy.sql import func
import os


# Env vars
DATABASE_URL = os.getenv("DATABASE_URL")


# SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()
contacts = Table(
    "contact",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(256)),
    Column("phone", String(50)),
    Column("email", String(256)),
)


# Databases query builder
database = Database(DATABASE_URL)
