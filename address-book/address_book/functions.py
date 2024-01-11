from sqlalchemy import create_engine, MetaData, select, insert
from sqlalchemy.orm import sessionmaker
import pandas as pd
import tkinter as tk
import os
from constants import DATABASE_URL


def get_all_data(): 

    engine = create_engine( f"sqlite:///{DATABASE_URL}")
    connection = engine.connect()
    metadata = MetaData()

    metadata.reflect(bind=engine)
    address = metadata.tables['address']

    qry = select(address)

    df = pd.DataFrame()
    df = pd.read_sql_query(
        sql = qry, 
        con = engine, 
        index_col = 'id'
    )
    connection.close()
    return df


def insert_data(dict): 

    engine = create_engine( f"sqlite:///{DATABASE_URL}")
    #Session = sessionmaker(bind=engine)
    #session = Session()

    connection = engine.connect()
    metadata = MetaData()
    metadata.reflect(bind=engine)
    address = metadata.tables['address']

    connection.execute(address.insert(), [ 
        dict
    ])
    connection.commit()
    connection.close()