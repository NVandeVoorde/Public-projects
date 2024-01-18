from sqlalchemy import create_engine, MetaData, select, insert
import pandas as pd

from constants import DATABASE_URL
from random import randint


def get_all_data(): 
    """ Get all the data from the database to fill the table, returns a dataframe"""

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
    """ Pass dictionary to insert to database """

    engine = create_engine( f"sqlite:///{DATABASE_URL}")
    connection = engine.connect()
    metadata = MetaData()
    metadata.reflect(bind=engine)
    address = metadata.tables['address']

    connection.execute(address.insert(), [dict])
    connection.commit()
    connection.close()

def selected_row(table): 
    """ Get information from the selected row in the table and return as a dictionary"""
    
    global selected_id

    selected = table.focus()
    details = table.item(selected)
    values = details.get("values")
    columns = list(table['columns'])
    id = details.get('text')
    selected_id = id

    dict_selected = dict(zip(columns, values))
    dict_selected.update({'id' : id})
    return dict_selected


def insert_dict(dict): 
    """ Takes a dictionary and inserts it into the database"""
    
    engine = create_engine( f"sqlite:///{DATABASE_URL}")
    connection = engine.connect()
    metadata = MetaData()
    metadata.reflect(bind=engine)
    address = metadata.tables['address']

    connection.execute(address.insert(), [dict])
    connection.commit()
    connection.close()


def delete_entry(table): 
    """ Takes row from the table and deletes it in the database """

    # Retrieve ID from table 
    selected = table.focus()
    details = table.item(selected)
    id = details.get("text")

    # Delete ID from database
    engine = create_engine( f"sqlite:///{DATABASE_URL}")
    connection = engine.connect()
    metadata = MetaData()
    metadata.reflect(bind=engine)
    address = metadata.tables['address']
    qry = address.delete().where(address.c.id == id)
    connection.execute(qry)
    connection.commit()
    connection.close()


def update_entry(dict, selected): 
    """ Use ID to update entries """
    
    # Retrieve data from entry widget via entry_to_dict
    id = selected

    # Delete ID from database
    engine = create_engine( f"sqlite:///{DATABASE_URL}")
    connection = engine.connect()
    metadata = MetaData()
    metadata.reflect(bind=engine)
    address = metadata.tables['address']
    qry = address.update().where(address.c.id == id).values(dict)
    connection.execute(qry)
    connection.commit()
    connection.close()


def refresh_table(table): 
    """ Refresh the data from the table """

    table.delete(*table.get_children())
    df = get_all_data()
    table['columns'] = df.columns.values.tolist()
    for i in df.columns.values.tolist():
        table.column(i, width=50)
        table.heading(i, text=i)
    for index, row in df.iterrows():
        table.insert("", 'end', text=index, values=list(row))