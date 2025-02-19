import pandas as pd
import sqlite3
import os

from Manage_data.scraper import *

# Configurations
DATABASE_PATH = os.path.join('instance', 'stocks.sqlite')

import sqlite3

def check_entry(title, db_path=DATABASE_PATH, table_name="stocks"):
    """Check if a given title already exists in the database."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = f"SELECT COUNT(*) FROM {table_name} WHERE Title = ?"
    cursor.execute(query, (title,))
    result = cursor.fetchone()[0]

    conn.close()
    
    return result > 0


def add_history(df, db_path=DATABASE_PATH):
    """Save a Pandas DataFrame to SQLite while ensuring column names match."""
    conn = sqlite3.connect(db_path)
    df.to_sql("stocks", conn, if_exists="append", index=False, method="multi")
    conn.close()

def add_yahoo(title:str):
    url = f'https://finance.yahoo.com/quote/{title}/history/?period1=1000000000&period2=19999999999'
    if check_entry(title=title):
        print('entry already exists or no title') # Im gonna change this
    else: 
        df = parse_yahoo(url)
        df = treat_yahoo(df)
        add_history(df)

def select_step(df, granularity="daily"):
    df['Date'] = pd.to_datetime(df['Date'])

    if granularity == "daily":
        return df
    elif granularity == "weekly":
        rule = "W-MON"
    elif granularity == "monthly":
        rule = "MS"
    else:
        raise ValueError("Invalid granularity. Choose 'weekly', 'monthly'")

    aggregation = {
        'Open': 'first',
        'High': 'max',
        'Low': 'min',
        'Close': 'last',
        'Adj_Close': 'last',
        'Volume': 'sum',
        'Title': 'first'
    }

    df = df.set_index('Date').resample(rule).agg(aggregation).reset_index()

    return df

def get_data(title:str, granularity='daily', db_path=DATABASE_PATH, table_name="stocks"):
    """
    Retrieve data from an SQLite database and return it as a Pandas DataFrame.
    granularity = daily or weekly or monthly
    """
    add_yahoo(title)
    conn = sqlite3.connect(db_path)   
    query = f"SELECT * FROM {table_name} WHERE Title = ?"
    df = pd.read_sql_query(query, conn, params=(title,))
    df = select_step(df=df, granularity=granularity)
    conn.close()
    return df

# Example usage
if __name__ == '__main__':
    get_data('META')