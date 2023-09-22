import sqlite3

# Define a main method
def create_tables():
    # SQLite connection
    sqlite_conn = sqlite3.connect('youtube.db')
    sqlite_cursor = sqlite_conn.cursor()   

    # Create the CHANNEL table
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS channel (
            Channel_Id VARCHAR(255),
            Channel_Name VARCHAR(255),
            Channel_Views INT,
            Subscribers INT,
            Total_Videos INT, 
            Created_Date DATETIME DEFAULT CURRENT_TIMESTAMP 
        );
    '''

    sqlite_cursor.execute(create_table_query)

    create_table_query = '''
        CREATE TABLE IF NOT EXISTS playlist (
            Channel_Id VARCHAR(255),
            Channel_Name VARCHAR(255),
            Playlist_Name VARCHAR(255),
            Playlist_ID VARCHAR(255),
            Video_Count VARCHAR(255)
        );
    '''

    # Execute the CREATE TABLE query
    sqlite_cursor.execute(create_table_query)

    create_table_query = '''
        CREATE TABLE IF NOT EXISTS video (
            Channel_Id VARCHAR(255),
            Channel_Name VARCHAR(255),
            video_id VARCHAR(255),
            Title VARCHAR(255),
            description VARCHAR(255),
            Published_At VARCHAR(255),
            Duration INT,
            Definition VARCHAR(255),
            Caption VARCHAR(255),
            View_Count INT,
            Like_Count INT,
            Favourite_Count INT,
            Comment_Count INT
        );
    '''

    sqlite_cursor.execute(create_table_query)

    create_table_query = '''
        CREATE TABLE IF NOT EXISTS comment (
            Channel_Id VARCHAR(255),
            Channel_Name VARCHAR(255),
            Comment_Id VARCHAR(255),
            Video_Id VARCHAR(255),
            Author_Display_Name VARCHAR(255),
            Published_At VARCHAR(255),
            Text_Display VARCHAR(255)
        );
    '''

    sqlite_cursor.execute(create_table_query)
