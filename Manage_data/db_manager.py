import sqlite3
import os


# Configurations
DATABASE_PATH = os.path.join('instance', 'stocks.sqlite')


def save_to_db(df, db_path=DATABASE_PATH):
    """Save a Pandas DataFrame to SQLite while ensuring column names match."""
    conn = sqlite3.connect(db_path)
    df.to_sql("stocks", conn, if_exists="append", index=False, method="multi")
    conn.close()

# def add_summary_subtitles(channel_id:str, max_results:int = 7):
#     """
#     Function to summarize and add this to the database.

#     Args:
#         channel_id: id of a youtube channel.
#     """
#     conn = sqlite3.connect(DATABASE)
    
#     try:
#         video_list = get_video(channel_id=channel_id, max_results=max_results)
#         for video in video_list: 
#             if entry_exists(conn, video['date'], video['name']):
#                 print(f"An entry with {video['date']} and {video['name']} already exists.\n\n\n")
#                 continue         
#             text = get_subtitles(video['video_id'])
#             text = synthesize_video_with_llm(text[:8000])
#             add_entry(conn, video['date'], video['name'], text, video['title'])
#     finally:
#         conn.close()

# def check_entry_info(conn, scan): 
#     cursor = conn.cursor()
#     cursor.execute(
#         'SELECT 1 FROM scan_info WHERE scan = ?',
#         (scan,)
#     )
#     return cursor.fetchone() is not None

# def entry_exists(conn, date, name):
#     """
#     Function to check if an entry with the given date and name already exists in the database.
    
#     Args:
#         conn (sqlite3.Connection): Database connection.
#         date (str): Date in format YYYY-MM-DDTHH:MM:SSZ.
#         name (str): Name of the YouTube channel.
        
#     Returns:
#         bool: True if the entry exists, False otherwise.
#     """
#     cursor = conn.cursor()
#     cursor.execute(
#         'SELECT 1 FROM yt_summaries WHERE date = ? AND name = ?',
#         (date, name)
#     )
#     return cursor.fetchone() is not None


# Example usage
if __name__ == '__main__':
    print('test')