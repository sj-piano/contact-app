# Imports
from databases import Database
from sqlalchemy import (
    Column,
    Integer,
    MetaData,
    String,
    Table,
    create_engine
)
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
