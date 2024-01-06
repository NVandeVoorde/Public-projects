from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select, Connection, inspect
DATABASE_URL = "sqlite:///data/adbook.db"

#Temp test
engine = create_engine(DATABASE_URL)
connection = engine.connect()
metadata = MetaData()

# Reflect the existing tables from the database
metadata.reflect(bind=engine)

# Access the 'zipcode' table from the reflected metadata
zipcode = metadata.tables['zipcode']


inspector = inspect(engine)
inspector.get_columns('zipcode')
#tables_dbo = inspector.get_table_names()
#print(tables_dbo)

qry = zipcode.select()

res = connection.execute(qry).fetchall()
print(res[0])
connection.close()