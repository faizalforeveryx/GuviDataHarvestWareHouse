import streamlit as st
from FetchAndMigrateToSql import fetch_migrate
from AllQuestions import *

st.set_page_config(page_title="YouTube Data Harvesting", page_icon=":play:", layout="wide")
st.title(":blue[YouTube Data Harvesting]")

# Define a dictionary to map questions to their corresponding functions
question_to_function = {
    '1. What are the names of all the videos and their corresponding channels?': q1,
    '2. Which channels have the most number of videos, and how many videos do they have?': q2,
    '3. What are the top 10 most viewed videos and their respective channels?': q3,
    '4. How many comments were made on each video, and what are their corresponding video names?': q4,
    '5. Which videos have the highest number of likes, and what are their corresponding channel names?': q5,
    '6. What is the total number of likes and dislikes for each video, and what are their corresponding video names?': q6,
    '7. What is the total number of views for each channel, and what are their corresponding channel names?': q7,
    '8. What are the names of all the channels that have published videos in the year 2022?': q8,
    '9. What is the average duration of all videos in each channel, and what are their corresponding channel names?': q9,
    '10. Which videos have the highest number of comments, and what are their corresponding channel names?': q10,
}

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

    # Add an initial "Select a Question" option
    questions = st.selectbox("You can choose any of the questions to get result among all channels", ["Select a Question"] + list(question_to_function.keys()))

    # Check if a valid question is selected
    if questions != "Select a Question":
        selected_function = question_to_function.get(questions)
        if selected_function:
            st.dataframe(selected_function())

if __name__ == "__main__":
    main()
