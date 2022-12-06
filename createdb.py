from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

from sqlalchemy import MetaData,Table, Column, Integer, String, MetaData,Float, Boolean

db_url = "sqlite:///mydb.sqlite"
engine = create_engine(db_url)

if not database_exists(engine.url):
    create_database(engine.url)

connection = engine.connect()

meta = MetaData()

emp = Table('emp', meta,
              Column('id', Integer()),
              Column('name', String(255), nullable=False),
              Column('salary', Float(), default=100.0),
              Column('active', Boolean(), default=True)
              )

meta.create_all(engine)