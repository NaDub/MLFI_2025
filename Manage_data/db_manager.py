import pandas as pd
import sqlite3
import os

from Manage_data.scraper import *

# Configurations
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, "../instance/stocks.sqlite")  # Remonte d'un niveau et va dans instance
DATABASE_PATH = os.path.abspath(DATABASE_PATH) 

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
    print(f'Adding Symbol: {title}')
    url = f'https://finance.yahoo.com/quote/{title}/history/?period1=1262304000&period2=19999999999'
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
        raise ValueError("Invalid granularity. Choose 'daily', 'weekly', 'monthly'")

    aggregation = {
        'Open': 'first',
        'High': 'max',
        'Low': 'min',
        'Close': 'last',
        'Adj_close': 'last',
        'Volume': 'sum'
    }

    df = df.groupby("Title", group_keys=False).apply(
    lambda x: x.set_index("Date").resample(rule).agg(aggregation).assign(Title=x["Title"].iloc[0])).reset_index()

    return df


import sqlite3
import pandas as pd
from typing import List

def get_data(titles: List[str], granularity='daily', db_path=DATABASE_PATH, table_name="stocks") -> pd.DataFrame:
    """
    Fetches financial data for multiple stock symbols from an SQLite database 
    and returns it as a Pandas DataFrame.

    Parameters:
    - titles (List[str]): A list of stock symbols (e.g., ['AAPL', 'GOOGL']).
    - granularity (str, optional): The time frame for aggregation. 
      Options: 'daily' (default), 'weekly', or 'monthly'.
    - db_path (str, optional): Path to the SQLite database file. Defaults to `DATABASE_PATH`.
    - table_name (str, optional): Name of the database table containing stock data. Defaults to "stocks".

    Returns:
    - pd.DataFrame: A DataFrame containing the requested financial data 
      with the specified granularity for all titles.

    Example:
    ```python
    df = get_data(['AAPL', 'GOOGL'], granularity='weekly')
    print(df.head())
    ```
    """
    
    if isinstance(titles, str):
        titles = [titles]

    if not titles:
        raise ValueError("The list of titles cannot be empty.")
    
    for title in titles:
        add_yahoo(title)

    conn = sqlite3.connect(db_path)
    placeholders = ','.join('?' * len(titles))
    query = f"SELECT * FROM {table_name} WHERE Title IN ({placeholders})"
    df = pd.read_sql_query(query, conn, params=titles)
    df = select_step(df=df, granularity=granularity)
    conn.close()

    return df


# def get_data(title: str, granularity='daily', db_path=DATABASE_PATH, table_name="stocks") -> pd.DataFrame:
#     """
#     Fetches financial data from an SQLite database and returns it as a Pandas DataFrame.

#     This function retrieves stock market data for a given title (e.g., stock symbol) from 
#     a specified database table. It also ensures that data is available by calling `add_yahoo(title)`, 
#     which fetches missing data if necessary. The retrieved data is then processed based on 
#     the selected granularity.

#     Parameters:
#     - title (str): The stock symbol or financial instrument identifier (e.g., '^FCHI').
#     - granularity (str, optional): The time frame for aggregation. 
#       Options: 'daily' (default), 'weekly', or 'monthly'.
#     - db_path (str, optional): Path to the SQLite database file. Defaults to `DATABASE_PATH`.
#     - table_name (str, optional): Name of the database table containing stock data. Defaults to "stocks".

#     Returns:
#     - pd.DataFrame: A DataFrame containing the requested financial data with the specified granularity.

#     Example:
#     ```python
#     df = get_data('^FCHI', granularity='weekly')
#     print(df.head())
#     ```
#     """
#     add_yahoo(title)
#     conn = sqlite3.connect(db_path)
#     query = f"SELECT * FROM {table_name} WHERE Title = ?"
#     df = pd.read_sql_query(query, conn, params=(title,))
#     df = select_step(df=df, granularity=granularity)
#     conn.close()
#     return df

# Example usage
if __name__ == '__main__':
    df = get_data('META')
    df.head()