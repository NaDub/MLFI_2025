import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
from Manage_data.db_manager import save_to_db


def fetch_decorator(func):
    """
    Decorator function that fetches the content from a URL and 
    parses it using the provided parsing function.
    """
    def wrapper(url: str):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            return func(soup)
        else:
            print(f"Request failure for {url}: {response.status_code}")
            return None
    return wrapper

@fetch_decorator
def parse_yahoo(soup: BeautifulSoup):
    """
    Function to get data on yahoo.
    """
    # Find title
    text = soup.find_all('h1', class_='yf-xxbei9')[0].text.strip()
    title = re.findall(r"\((.*?)\)", text)[0]

    # Find columns
    columns = ['Date', 'Open', 'High', 'Low', 'Close','Adj_Close',
       'Volume', 'Title']

    # Find all cells
    rows = soup.find_all('tr', class_='yf-1jecxey')
    data = []
    for row in rows[1:]:
        cells = row.find_all('td', class_='yf-1jecxey')
        values = [cell.text.strip() for cell in cells]
        values.append(title)
        data.append(values)

    # Create a dataframe
    df = pd.DataFrame(data, columns=columns)
    df.reset_index(drop=True, inplace=True)
    df.dropna(inplace=True) # On my examples delete only 'dividend rows'
    # Change this soon as possible
    return df

if __name__ == '__main__':
    tester = parse_yahoo('https://finance.yahoo.com/quote/META/history/?period1=1582042649&period2=1739895424')
    # print(tester.tail())
    # print(tester.columns)
    # print(tester[tester['Title'].isna() == True])
    # save_to_db(tester)

