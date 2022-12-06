from sqlalchemy import create_engine , insert
from sqlalchemy_utils import database_exists, create_database
import pandas as pd

from sqlalchemy import MetaData,Table, Column, Integer, String, MetaData,Float, Boolean






db_url = "sqlite:///mydb.sqlite"
engine = create_engine(db_url)

connection = engine.connect()
trans = connection.begin()


meta = MetaData()
meta.reflect(bind=engine)

df = pd.read_csv("test.csv")
df["active"] = df["active"].astype(int)
df.to_sql('test',
          con=engine,
          index=False,
          index_label='id',
          if_exists='replace')

# emp = meta.tables["emp"]

# query = insert(emp) 
# values_list = [{'Id':'2', 'name':'ram', 'salary':80000, 'active':False},
#                {'Id':'3', 'name':'ramesh', 'salary':70000, 'active':True}]
# ResultProxy = connection.execute(query,values_list)

trans.commit()
connection.close()