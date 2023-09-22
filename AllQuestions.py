import pandas as pd
import sqlite3

# Function to create a new SQLite connection and cursor
def get_connection_cursor():
    sqlite_conn = sqlite3.connect('youtube.db')
    sqlite_cursor = sqlite_conn.cursor()
    return sqlite_cursor

def q1():
    # What are the names of all the videos and their corresponding channels?
    sqlite_cursor = get_connection_cursor()
    sqlite_cursor.execute('''SELECT Channel_Name, Title FROM video''')
    results = sqlite_cursor.fetchall()
    df = pd.DataFrame(results, columns =  ['Channel_Name', 'Video_Name'])
    sqlite_cursor.close()
    return df

def q2():
    # Which channels have the most number of videos, and how many videos do they have?
    sqlite_cursor = get_connection_cursor()
    sqlite_cursor.execute('''SELECT Channel_Name, Total_Videos FROM channel ORDER BY Total_Videos DESC''')
    results = sqlite_cursor.fetchall()
    df = pd.DataFrame(results, columns =  ['Channel_Name', 'Total_Videos'])
    sqlite_cursor.close()
    return df

def q3():
    # What are the top 10 most viewed videos and their respective channels?
    sqlite_cursor = get_connection_cursor()
    sqlite_cursor.execute('''SELECT Channel_Name, Title, View_Count FROM video ORDER BY View_Count DESC
    LIMIT 10; ''')
    results = sqlite_cursor.fetchall()
    df = pd.DataFrame(results, columns =  ['Channel_Name', 'Video_Name', 'Views'])
    sqlite_cursor.close()
    return df

def q4():
    # How many comments were made on each video, and what are their corresponding video names?
    sqlite_cursor = get_connection_cursor()
    sqlite_cursor.execute('''SELECT Title, Comment_Count FROM video''')
    results = sqlite_cursor.fetchall()
    df = pd.DataFrame(results, columns =  ['Video_Name', 'Comment_Count'])
    sqlite_cursor.close()
    return df

def q5():
    # Which videos have the highest number of likes, and what are their corresponding channel names?
    sqlite_cursor = get_connection_cursor()
    sqlite_cursor.execute('''SELECT Channel_Name, Title, Like_Count FROM video ORDER BY Like_Count DESC''')
    results = sqlite_cursor.fetchall()
    df = pd.DataFrame(results, columns =  ['Channel_Name', 'Video_Name', 'Like_Count'])
    sqlite_cursor.close()
    return df

def q6():
    # What is the total number of likes and dislikes for each video, and what are their corresponding video names?
    sqlite_cursor = get_connection_cursor()
    sqlite_cursor.execute('''SELECT Title, Like_Count FROM video''')
    results = sqlite_cursor.fetchall()
    df = pd.DataFrame(results, columns =  ['Video_Name', 'Like_Count'])
    sqlite_cursor.close()
    return df

def q7():
    # What is the total number of views for each channel, and what are their corresponding channel names?
    sqlite_cursor = get_connection_cursor()
    sqlite_cursor.execute('''SELECT Channel_Name, Channel_Views FROM channel''')
    results = sqlite_cursor.fetchall()
    df = pd.DataFrame(results, columns =  ['Channel_Name', 'Channel_Views'])
    sqlite_cursor.close()
    return df

def q8():
    # What are the names of all the channels that have published videos in the year 2022?
    sqlite_cursor = get_connection_cursor()
    sqlite_cursor.execute('''SELECT DISTINCT Channel_Name, Published_At
                            FROM video
                            WHERE strftime('%Y', Published_At) = '2022';
                            ''')
    results = sqlite_cursor.fetchall()
    df = pd.DataFrame(results, columns =  ['Channel_Name', 'Publish_Date'])
    sqlite_cursor.close()
    return df

def q9():
    # What is the average duration of all videos in each channel, and what are their corresponding channel names?
    sqlite_cursor = get_connection_cursor()
    sqlite_cursor.execute('''SELECT Channel_Name, AVG(
        CAST(SUBSTR(Duration, 3, INSTR(Duration, 'M') - 3) AS INTEGER) * 60 +
        CAST(SUBSTR(Duration, INSTR(Duration, 'M') + 1, INSTR(Duration, 'S') - 
        INSTR(Duration, 'M') - 1) AS INTEGER)
    )/60 AS average_duration_in_minutes FROM video GROUP BY Channel_Name;''')
    results = sqlite_cursor.fetchall()
    df = pd.DataFrame(results, columns =  ['Channel_Name', 'Avg_Duration_In_Mins'])
    sqlite_cursor.close()
    return df

def q10():
    # Which videos have the highest number of comments, and what are their corresponding channel names?
    sqlite_cursor = get_connection_cursor()
    sqlite_cursor.execute('''SELECT Channel_Name, Title, Comment_Count FROM video ORDER BY Comment_Count DESC''')
    results = sqlite_cursor.fetchall()
    df = pd.DataFrame(results, columns =  ['Channel_Name', 'Video_Name', 'Comment_Count'])
    sqlite_cursor.close()
    return df