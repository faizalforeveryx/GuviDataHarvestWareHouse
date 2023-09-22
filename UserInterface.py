import streamlit as st
from FetchAndMigrateToSql import fetch_migrate
from AllQuestions import *

st.set_page_config(page_title="YouTube Data Harvesting", page_icon=":play:", layout="wide")
st.title(":blue[YouTube Data Harvesting]")

def main():
    API_Key = st.text_input('Enter the API Key: ')
    channel_ids_string = st.text_input('Enter the Channel ID(s) (comma-separated): ')
    # Remove spaces from the input string
    channel_ids_string = channel_ids_string.replace(' ', '')
    # Split the string by commas to get a list of channel IDs
    channel_ids = channel_ids_string.split(',')

    if st.button("Fetch Channel Data"):
        try:
            output = fetch_migrate(API_Key, channel_ids)
            st.markdown(f'<p style="color: green; font-size: 20px;">{output}</p>', unsafe_allow_html=True)
        except:
            st.error("An error occurred. Please check your API Key or Channel ID(s).")

    questions = st.selectbox("Select the Question", ('Tap to view',
                                                     '1. What are the names of all the videos and their corresponding channels?',
                                                     '2. Which channels have the most number of videos, and how many videos do they have?',
                                                     '3. What are the top 10 most viewed videos and their respective channels?',
                                                     '4. How many comments were made on each video, and what are their corresponding video names?',
                                                     '5. Which videos have the highest number of likes, and what are their corresponding channel names?',
                                                     '6. What is the total number of likes and dislikes for each video, and what are their corresponding video names?',
                                                     '7. What is the total number of views for each channel, and what are their corresponding channel names?',
                                                     '8. What are the names of all the channels that have published videos in the year 2022?',
                                                     '9. What is the average duration of all videos in each channel, and what are their corresponding channel names?',
                                                     '10. Which videos have the highest number of comments, and what are their corresponding channel names?'))

    if st.button("View data"):
        if questions == '1. What are the names of all the videos and their corresponding channels?':
            st.dataframe(q1())

        elif questions == '2. Which channels have the most number of videos, and how many videos do they have?':
            st.dataframe(q2())

        elif questions == '3. What are the top 10 most viewed videos and their respective channels?':
            st.dataframe(q3())

        elif questions == '4. How many comments were made on each video, and what are their corresponding video names?':
            st.dataframe(q4())

        elif questions == '5. Which videos have the highest number of likes, and what are their corresponding channel names?':
            st.dataframe(q5())

        elif questions == '6. What is the total number of likes and dislikes for each video, and what are their corresponding video names?':
            st.dataframe(q6())

        elif questions == '7. What is the total number of views for each channel, and what are their corresponding channel names?':
            st.dataframe(q7())

        elif questions == '8. What are the names of all the channels that have published videos in the year 2022?':
            st.dataframe(q8())

        elif questions == '9. What is the average duration of all videos in each channel, and what are their corresponding channel names?':
            st.dataframe(q9())

        elif questions == '10. Which videos have the highest number of comments, and what are their corresponding channel names?':
            st.dataframe(q10())


if __name__ == "__main__":
     main()