import sqlite3
import pymongo
import time

# Define a main method
def main():

    # SQLite connection
    sqlite_conn = sqlite3.connect('youtube.db')
    sqlite_cursor = sqlite_conn.cursor()   

    myclient = pymongo.MongoClient("mongodb+srv://meetafhere:test123@cluster0.ysvxil8.mongodb.net/?retryWrites=true&w=majority")
    mydb = myclient["youtube"]
    mycol = mydb["channels"] 

    mongo_data = mycol.find()

    for document in mongo_data:
        # Record the start time
        start_time = time.time()
        
        channel_name = document["channel_details"][0]['Channel Name']
        print('Insertion started for the channel: ', channel_name)

        print('Insertion into channel table started')
        insert_query = '''
            INSERT INTO channel (Channel_Id, Channel_Name, Channel_Views, Subscribers, Total_Videos)
            VALUES (?, ?, ?, ?, ?);
        '''
        data_to_insert = (
            document["channel_details"][0]['Channel Id'],
            channel_name,
            document["channel_details"][0]['Views'],
            document["channel_details"][0]['Subscribers'],
            document["channel_details"][0]['Total Videos']
        )
        
        sqlite_cursor.execute(insert_query, data_to_insert)
        sqlite_conn.commit()  
        print('Insertion into channel table finished')

        print('Insertion into playlist table started')
        insert_query = '''
        INSERT INTO playlist (Channel_Name, Playlist_Name, Playlist_ID, Video_Count)
        VALUES (?, ?, ?, ?);
        '''
    
        playlist_details_length = len(document["playlist_details"])
        for i in range(0, playlist_details_length):
            data_to_insert = (
                channel_name,
                document["playlist_details"][i]['Playlist Name'],
                document["playlist_details"][i]['Playlist ID'],
                document["playlist_details"][i]['Video Count']

            )
            sqlite_cursor.execute(insert_query, data_to_insert)
            sqlite_conn.commit()  
        
        print('Insertion into playlist table finished')
        
        print('Insertion into video table started')
        insert_query = '''
        INSERT INTO video (Channel_Name, Video_Id, Title, Description, Published_At, 
                        Duration, Definition, Caption, View_Count, Like_Count, Favourite_Count, Comment_Count)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        '''

        video_details_length = len(document["video_details"])
        for i in range(0, video_details_length):
            data_to_insert = (
                channel_name,
                document["video_details"][i]['video_id'],
                document["video_details"][i]['title'],
                document["video_details"][i]['description'],
                document["video_details"][i]['publishedAt'],
                document["video_details"][i]['duration'],
                document["video_details"][i]['definition'],
                document["video_details"][i]['caption'],
                document["video_details"][i]['viewCount'],
                document["video_details"][i]['likeCount'],
                document["video_details"][i]['favouriteCount'],
                document["video_details"][i]['commentCount']

            )
            sqlite_cursor.execute(insert_query, data_to_insert)
            sqlite_conn.commit() 

        print('Insertion into video table finished')


        print('Insertion into comment table started')
        insert_query = '''
        INSERT INTO comment (Channel_Name, Comment_Id, Video_Id, Author_Display_Name, Published_At, Text_Display)
        VALUES (?, ?, ?, ?, ?, ?);
        '''
    
        comment_details_length = len(document["comment_details"])
        for i in range(0, comment_details_length):
            data_to_insert = (
                channel_name,
                document["comment_details"][i]['commentId'],
                document["comment_details"][i]['videoId'],
                document["comment_details"][i]['authorDisplayName'],
                document["comment_details"][i]['publishedAt'],
                document["comment_details"][i]['textDisplay']

            )
            sqlite_cursor.execute(insert_query, data_to_insert)
            sqlite_conn.commit()

        print('Insertion into comment table finished')
        execution_time = time.time() - start_time
        print(f'Insertion finished for the channel: {channel_name} in {execution_time:.2f}seconds')

if __name__ == "__main__":
    main()
