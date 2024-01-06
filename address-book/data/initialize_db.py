# Dataset from public open data: https://public.opendatasoft.com/explore/dataset/georef-belgium-postal-codes/export/

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select, Connection
import pandas as pd


print("Initialize DB")
DATABASE_URL = "sqlite:///data/adbook.db"

engine = create_engine(DATABASE_URL)
metadata = MetaData()

zipcode = Table('zipcode', metadata, 
    Column('zipcode', Integer, primary_key=True), 
    Column('mun_name', String)
)

address = Table('address', metadata, 
    Column('id', String, primary_key=True), 
    Column('first_name', String), 
    Column('last_name', String), 
    Column('street', String), 
    Column('house_number', Integer), 
    Column('zipcode', Integer)
)

metadata.create_all(engine)

temp = pd.read_csv('C:/Users/vandevnj/Documents/Personal/Projecten/Public-projects/address-book/data/temp.csv', sep = ';')

temp.to_sql('zipcode', engine, index=False, if_exists='replace')

print("Done")

#Temp test
engine = create_engine(DATABASE_URL)
connection = engine.connect()
metadata = MetaData()

metadata.reflect(bind=engine)
zipcode = metadata.tables['zipcode']

qry = select([zipcode])
#print(qry)

#results = connection.execute(qry).fetchall()
#print(results[0])