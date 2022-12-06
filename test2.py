from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, CheckConstraint, Float,Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

db_url = "sqlite:///mydb.sqlite"
engine = create_engine(db_url)
# create session
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class TestTable(Base):
    __tablename__ = 'Test Table'
    __table_args__ = (
        CheckConstraint('active = 0 or active = 1'),
    )
    id = Column('id', Integer(),primary_key=True)
    name= Column('name', String(255), nullable=False)
    salary=Column('salary', Float(), default=100.0)
    active=Column('active', Integer(), default=0)


# create tables
Base.metadata.create_all(bind=engine)





try:
    row = TestTable(name='razm', salary=80000,active=1200)
    session.add(row)
    session.commit()
except SQLAlchemyError as e:
    print(e)
finally:
    session.close()