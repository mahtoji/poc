from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select
from sqlalchemy import or_

engine = create_engine("shillelagh://")
connection = engine.connect()

table = Table('https://docs.google.com/spreadsheets/d/1RZstNkiNBTEBo8mJBwAYh29bQHOynEDxFb54hvHRsAc/edit#gid=1835168426', MetaData(bind=engine),autoload=True)

print(table.name)
print(table.columns.keys())

select_st = select([table]).where(table.c.Org == "CME")
res = connection.execute(select_st)

for _row in res:
    print(_row)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

rows = session.query(table.c.Org).all()
for r in rows:
    print(r)

l = [v for v, in rows]

print(l)

#Find all columns
for c in table.columns:
    rows = session.query(c).all()
    #Find values from all columns
    l = [v for v, in rows]
    print(l)

