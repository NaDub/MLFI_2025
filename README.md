# Project Overview

This project is designed to scrape stock data from Yahoo Finance, analyze stylized financial facts, test prediction algorithms, and visualize the results. It also includes a SQLite database to store and manage the collected data.

## Project Structure

```
├── Algorithm            # Contains predictive algorithms for stock data analysis
├── instance            # Contains the SQLite database
│   └── stocks.sqlite   # Database file storing financial data
├── Manage_data         # Data management module
│   ├── db_manager.py   # Manages database interactions
│   ├── init_db.py      # Initializes the database schema
│   ├── schema.sql      # SQL script for database schema
│   └── scraper.py      # Scraper for fetching data from Yahoo Finance
├── README.md           # Project documentation
├── StilizedFacts       # Module for analyzing stylized facts in financial data
└── Visualize           # Visualization tools for data representation
```

## Installation

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd <repository-name>
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Initialize the database:
   ```sh
   python Manage_data/init_db.py
   ```

## Usage

- **Scraping Data:** Use following function to collect stock data from Yahoo Finance:
  ```sh
  from Manage_data.scraper import get_data

  get_data('META') 
  ```
output:
```
>>> get_data('META')
entry already exists or no title
     Title       Date    Open    High     Low   Close  Adj_close     Volume
0     META 2025-02-18  736.00  736.73  706.44  716.37     716.37   21815704
1     META 2025-02-14  726.14  740.91  725.62  736.67     736.67   16884300
2     META 2025-02-13  721.52  729.00  718.04  728.56     728.56   12569100
3     META 2025-02-12  715.30  727.10  712.60  725.38     725.38   12016500
4     META 2025-02-11  713.32  723.66  710.04  719.80     719.80   12998000
...    ...        ...     ...     ...     ...     ...        ...        ...
3201  META 2012-05-24   32.95   33.21   31.77   33.03      32.90   50237200
3202  META 2012-05-23   31.37   32.50   31.36   32.00      31.88   73600000
3203  META 2012-05-22   32.61   33.59   30.94   31.00      30.88  101786600
3204  META 2012-05-21   36.53   36.66   33.00   34.03      33.90  168192700
3205  META 2012-05-18   42.05   45.00   38.00   38.23      38.08  573576400

[3206 rows x 8 columns]
```
- **Analyzing Stylized Facts:** Use the modules in `StilizedFacts` to verify key financial properties.
- **Running Prediction Algorithms:** The `Algorithm` directory contains various models for predicting stock trends.
- **Visualizing Data:** Utilize the `Visualize` module to generate meaningful graphs and insights.

## Database Structure

The project utilizes a SQLite database (`stocks.sqlite`) to store the scraped financial data. The schema is defined in `schema.sql` and managed using `db_manager.py`.

## License

This project is licensed under the MIT License.

