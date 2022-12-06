from sqlalchemy import create_engine,insert
from sqlalchemy_utils import database_exists, create_database

from sqlalchemy import MetaData,Table, Column, Integer, String, MetaData,Float, Boolean

db_url = "sqlite:///mydb.sqlite"
engine = create_engine(db_url)

if not database_exists(engine.url):
    create_database(engine.url)


connection = engine.connect()
trans = connection.begin()

meta = MetaData()

emp = Table('emp', meta,
              Column('id', Integer()),
              Column('name', String(255), nullable=False),
              Column('salary', Float(), default=100.0),
              Column('active', Boolean(create_constraint=True), default=0)
              )


meta.create_all(engine)
emp = meta.tables["emp"]

query = insert(emp) 
values_list = [{'id':'2', 'name':'ram', 'salary':80000, 'active':False},
                {'id':'3', 'name':'ramesh', 'salary':70000, 'active':True}]
ResultProxy = connection.execute(query,values_list)
trans.commit()
connection.close()