from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select, Connection, inspect, insert, delete, and_, or_
import os

absolute_path = os.path.dirname(__file__)
database_location = "adbook.db"

DATABASE_URL = os.path.join(absolute_path, database_location)

#Temp test
engine = create_engine(f"sqlite:///{DATABASE_URL}", echo=False)
connection = engine.connect()
metadata = MetaData()

metadata.reflect(bind=engine)
zipcode = metadata.tables['zipcode']
address = metadata.tables['address']


# SELECT 
#qry = zipcode.select()
qry = zipcode.select()

res = connection.execute(qry).fetchall()
print(res[0])


# INSERT
# print("Insert")
# with engine.connect() as conn:
#     result = conn.execute(
#         insert(address),
#             [
#                 {"id": "1", "first_name": "Frans","last_name": "Bauer", "street": "Rue des boucher", "house_number": "35", "zipcode": "1000"},
#                 {"id": "2", "first_name": "Gert", "last_name": "Verhulst", "street": "Den boët", "house_number": "1", "zipcode": "2000"}
#             ],
#         )
#     conn.commit()

# print("select")
# qry = address.select()

# res = connection.execute(qry).fetchall()
# for row in res: 
#     print(row)

# EVEN LATEN STAAN ZODAT WE DATA HEBBEN
#quit()

# DELETE 
print("Delete")
with engine.connect() as conn: 
    result = conn.execute(
        delete(address).where(
            or_(address.columns.first_name !='bla', address.columns.first_name =='blabla')
        )
    )
    conn.commit()

print("select")
qry = address.select()

res = connection.execute(qry).fetchall()
for row in res: 
    print(row)