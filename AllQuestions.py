import pandas as pd
import sqlite3

# Common function to execute SQL queries
def execute_query(sql_query):
    sqlite_conn = sqlite3.connect('youtube.db')
    sqlite_cursor = sqlite_conn.cursor()
    sqlite_cursor.execute(sql_query)
    results = sqlite_cursor.fetchall()
    sqlite_conn.close()
    return results

def q1():
    # What are the names of all the videos and their corresponding channels?
    sql_query = '''SELECT Channel_Name, Title FROM video'''
    results = execute_query(sql_query)
    df = pd.DataFrame(results, columns=['Channel_Name', 'Video_Name'])
    return df

def q2():
    # Which channels have the most number of videos, and how many videos do they have?
    sql_query = '''SELECT Channel_Name, Total_Videos FROM channel ORDER BY Total_Videos DESC'''
    results = execute_query(sql_query)
    df = pd.DataFrame(results, columns=['Channel_Name', 'Total_Videos'])
    return df

def q3():
    # What are the top 10 most viewed videos and their respective channels?
    sql_query = '''SELECT Channel_Name, Title, View_Count FROM video ORDER BY View_Count DESC LIMIT 10'''
    results = execute_query(sql_query)
    df = pd.DataFrame(results, columns=['Channel_Name', 'Video_Name', 'Views'])
    return df

def q4():
    # How many comments were made on each video, and what are their corresponding video names?
    sql_query = '''SELECT Title, Comment_Count FROM video'''
    results = execute_query(sql_query)
    df = pd.DataFrame(results, columns=['Video_Name', 'Comment_Count'])
    return df

def q5():
    # Which videos have the highest number of likes, and what are their corresponding channel names?
    sql_query = '''SELECT Channel_Name, Title, Like_Count FROM video ORDER BY Like_Count DESC'''
    results = execute_query(sql_query)
    df = pd.DataFrame(results, columns=['Channel_Name', 'Video_Name', 'Like_Count'])
    return df

def q6():
    # What is the total number of likes and dislikes for each video, and what are their corresponding video names?
    sql_query = '''SELECT Title, Like_Count FROM video'''
    results = execute_query(sql_query)
    df = pd.DataFrame(results, columns=['Video_Name', 'Like_Count'])
    return df

def q7():
    # What is the total number of views for each channel, and what are their corresponding channel names?
    sql_query = '''SELECT Channel_Name, Channel_Views FROM channel'''
    results = execute_query(sql_query)
    df = pd.DataFrame(results, columns=['Channel_Name', 'Channel_Views'])
    return df

def q8():
    # What are the names of all the channels that have published videos in the year 2022?
    sql_query = '''SELECT DISTINCT Channel_Name, Published_At
                   FROM video
                   WHERE strftime('%Y', Published_At) = '2022';'''
    results = execute_query(sql_query)
    df = pd.DataFrame(results, columns=['Channel_Name', 'Publish_Date'])
    return df

def q9():
    # What is the average duration of all videos in each channel, and what are their corresponding channel names?
    sql_query = '''SELECT Channel_Name, AVG(
        CAST(SUBSTR(Duration, 3, INSTR(Duration, 'M') - 3) AS INTEGER) * 60 +
        CAST(SUBSTR(Duration, INSTR(Duration, 'M') + 1, INSTR(Duration, 'S') - INSTR(Duration, 'M') - 1) AS INTEGER)
    )/60 AS average_duration_in_minutes FROM video GROUP BY Channel_Name;'''
    results = execute_query(sql_query)
    df = pd.DataFrame(results, columns=['Channel_Name', 'Avg_Duration_In_Mins'])
    return df

def q10():
    # Which videos have the highest number of comments, and what are their corresponding channel names?
    sql_query = '''SELECT Channel_Name, Title, Comment_Count FROM video ORDER BY Comment_Count DESC'''
    results = execute_query(sql_query)
    df = pd.DataFrame(results, columns=['Channel_Name', 'Video_Name', 'Comment_Count'])
    return df
