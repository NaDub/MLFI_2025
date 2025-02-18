import sqlite3
import click
import os

# Define the database path
DATABASE_PATH = os.path.join('instance', 'stocks.sqlite')

def get_db():
    """Opens a connection to the SQLite database."""
    db = sqlite3.connect(
        DATABASE_PATH,
        detect_types=sqlite3.PARSE_DECLTYPES
    )
    db.row_factory = sqlite3.Row
    return db

def close_db(db):
    """Closes the database connection."""
    if db is not None:
        db.close()

def init_db():
    """Initializes the database by executing the SQL script."""
    db = get_db()
    
    with open('Manage_data/schema.sql', 'r', encoding='utf8') as f:
        db.executescript(f.read())

    close_db(db)

@click.command('init-db')
def init_db_command():
    """Clears existing data and creates new tables."""
    init_db()
    click.echo('Initialized the database.')

if __name__ == '__main__':
    init_db_command()
