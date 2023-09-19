import streamlit as st
import pandas as pd
import sqlite3

# SQLite connection
sqlite_conn = sqlite3.connect('youtube.db')
sqlite_cursor = sqlite_conn.cursor()

# Q1
sqlite_cursor.execute('''SELECT Channel_Name, Title FROM video''')
results = sqlite_cursor.fetchall()

# Create a dataframe
df = pd.DataFrame(results, columns =  ['Channel_Name', 'Video_Name'])

# Display the Streamlit app
st.title('What are the names of all the videos and their corresponding channels?')

# Display the DataFrame in Streamlit
st.write(df)

#Q2
sqlite_cursor.execute('''SELECT Channel_Name, Total_Videos FROM channel ORDER BY Total_Videos DESC''')
results = sqlite_cursor.fetchall()

# Create a dataframe
df = pd.DataFrame(results, columns =  ['Channel_Name', 'Total_Videos'])

# Display the Streamlit app
st.title('Which channels have the most number of videos, and how many videos do they have?')

# Display the DataFrame in Streamlit
st.write(df)

#Q3
sqlite_cursor.execute('''SELECT Channel_Name, Title, View_Count FROM video ORDER BY View_Count DESC
LIMIT 10; ''')
results = sqlite_cursor.fetchall()

# Create a dataframe
df = pd.DataFrame(results, columns =  ['Channel_Name', 'Video_Name', 'Views'])

# Display the Streamlit app
st.title('What are the top 10 most viewed videos and their respective channels?')

# Display the DataFrame in Streamlit
st.write(df)

#Q4
sqlite_cursor.execute('''SELECT Title, Comment_Count FROM video''')
results = sqlite_cursor.fetchall()

# Create a dataframe
df = pd.DataFrame(results, columns =  ['Video_Name', 'Comment_Count'])

# Display the Streamlit app
st.title('How many comments were made on each video, and what are their corresponding video names?')

# Display the DataFrame in Streamlit
st.write(df)

#Q5
sqlite_cursor.execute('''SELECT Channel_Name, Title, Like_Count FROM video ORDER BY Like_Count DESC''')
results = sqlite_cursor.fetchall()

# Create a dataframe
df = pd.DataFrame(results, columns =  ['Channel_Name', 'Video_Name', 'Like_Count'])

# Display the Streamlit app
st.title('Which videos have the highest number of likes, and what are their corresponding channel names?')

# Display the DataFrame in Streamlit
st.write(df)

#Q6
sqlite_cursor.execute('''SELECT Title, Like_Count FROM video''')
results = sqlite_cursor.fetchall()

# Create a dataframe
df = pd.DataFrame(results, columns =  ['Video_Name', 'Like_Count'])

# Display the Streamlit app
st.title('What is the total number of likes and dislikes for each video, and what are their corresponding video names?')

# Display the DataFrame in Streamlit
st.write(df)

#Q7
sqlite_cursor.execute('''SELECT Channel_Name, Channel_Views FROM channel''')
results = sqlite_cursor.fetchall()

# Create a dataframe
df = pd.DataFrame(results, columns =  ['Channel_Name', 'Channel_Views'])

# Display the Streamlit app
st.title('What is the total number of views for each channel, and what are their corresponding channel names?')

# Display the DataFrame in Streamlit
st.write(df)

#Q8
sqlite_cursor.execute('''SELECT DISTINCT Channel_Name, Published_At
                        FROM video
                        WHERE strftime('%Y', Published_At) = '2022';
                        ''')
results = sqlite_cursor.fetchall()

# Create a dataframe
df = pd.DataFrame(results, columns =  ['Channel_Name', 'Publish_Date'])

# Display the Streamlit app
st.title('What are the names of all the channels that have published videos in the year 2022?')

# Display the DataFrame in Streamlit
st.write(df)

#Q9
sqlite_cursor.execute('''SELECT Channel_Name, AVG(
    CAST(SUBSTR(Duration, 3, INSTR(Duration, 'M') - 3) AS INTEGER) * 60 +
    CAST(SUBSTR(Duration, INSTR(Duration, 'M') + 1, INSTR(Duration, 'S') - 
    INSTR(Duration, 'M') - 1) AS INTEGER)
)/60 AS average_duration_in_minutes FROM video GROUP BY Channel_Name;''')
results = sqlite_cursor.fetchall()

# Create a dataframe
df = pd.DataFrame(results, columns =  ['Channel_Name', 'Avg_Duration_In_Mins'])

# Display the Streamlit app
st.title('What is the average duration of all videos in each channel, and what are their corresponding channel names?')

# Display the DataFrame in Streamlit
st.write(df)

#Q10
sqlite_cursor.execute('''SELECT Channel_Name, Title, Comment_Count FROM video ORDER BY Comment_Count DESC''')
results = sqlite_cursor.fetchall()

# Create a dataframe
df = pd.DataFrame(results, columns =  ['Channel_Name', 'Video_Name', 'Comment_Count'])

# Display the Streamlit app
st.title('Which videos have the highest number of comments, and what are their corresponding channel names?')

# Display the DataFrame in Streamlit
st.write(df)