# data_engineering/load.py

import sqlite3
import pandas as pd

def load_data(df, db_name, table_name):
    """
    Loads transformed data into a SQLite database.

    Parameters:
    - df (pd.DataFrame): Transformed data.
    - db_name (str): Name of the SQLite database file.
    - table_name (str): Name of the table to insert data into.

    Returns:
    - None
    """
   


def generate_create_table_query(df, table_name):
    """
    Generates a SQL query to create a table based on the DataFrame schema.

    Parameters:
    - df (pd.DataFrame): Data to base the table schema on.
    - table_name (str): Name of the table to create.

    Returns:
    - str: SQL create table query.
    """
   
