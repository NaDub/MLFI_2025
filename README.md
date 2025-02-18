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

- **Scraping Data:** Run the scraper to collect stock data from Yahoo Finance:
  ```sh
  python Manage_data/scraper.py
  ```
- **Analyzing Stylized Facts:** Use the modules in `StilizedFacts` to verify key financial properties.
- **Running Prediction Algorithms:** The `Algorithm` directory contains various models for predicting stock trends.
- **Visualizing Data:** Utilize the `Visualize` module to generate meaningful graphs and insights.

## Database Structure

The project utilizes a SQLite database (`stocks.sqlite`) to store the scraped financial data. The schema is defined in `schema.sql` and managed using `db_manager.py`.

## License

This project is licensed under the MIT License.

