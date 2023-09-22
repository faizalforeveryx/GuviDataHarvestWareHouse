import sqlite3
import pymongo
import time

# Define a main method
def migrate_to_sql(channel_ids):

    # SQLite connection
    sqlite_conn = sqlite3.connect('youtube.db')
    sqlite_cursor = sqlite_conn.cursor()   

    # Delete from sql started
    tables = ["channel", "comment", "playlist", "video"]
    for table in tables:
        delete_sql = f"DELETE FROM {table} WHERE channel_id IN ({','.join(['?']*len(channel_ids))})"
        sqlite_cursor.execute(delete_sql, channel_ids)
        if table=="channel":
            records_deleted = sqlite_cursor.rowcount
            print('No of channels deleted from sql db: ', records_deleted)
        sqlite_conn.commit()
    # Delete from sql ended

    myclient = pymongo.MongoClient("mongodb+srv://meetafhere:test123@cluster0.ysvxil8.mongodb.net/?retryWrites=true&w=majority")
    mydb = myclient["youtube"]
    mycol = mydb["channels"] 

    query = {"channel_details.Channel Id": {"$in": channel_ids}}
    mongo_data = mycol.find(query)

    for document in mongo_data:
        # Record the start time
        start_time = time.time()
        
        channel_id = document["channel_details"][0]['Channel Id']
        channel_name = document["channel_details"][0]['Channel Name']
        print('Migration started for the channel: ', channel_name)

        print('Insertion into channel table started')
        insert_query = '''
            INSERT INTO channel (Channel_Id, Channel_Name, Channel_Views, Subscribers, Total_Videos)
            VALUES (?, ?, ?, ?, ?);
        '''
        data_to_insert = (
            channel_id,
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
        INSERT INTO playlist (Channel_Id, Channel_Name, Playlist_Name, Playlist_ID, Video_Count)
        VALUES (?, ?, ?, ?, ?);
        '''
    
        playlist_details_length = len(document["playlist_details"])
        for i in range(0, playlist_details_length):
            data_to_insert = (
                channel_id,
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
        INSERT INTO video (Channel_Id, Channel_Name, Video_Id, Title, Description, Published_At, 
                        Duration, Definition, Caption, View_Count, Like_Count, Favourite_Count, Comment_Count)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        '''

        video_details_length = len(document["video_details"])
        for i in range(0, video_details_length):
            data_to_insert = (
                channel_id,
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
        INSERT INTO comment (Channel_Id, Channel_Name, Comment_Id, Video_Id, Author_Display_Name, Published_At, Text_Display)
        VALUES (?, ?, ?, ?, ?, ?, ?);
        '''
    
        comment_details_length = len(document["comment_details"])
        for i in range(0, comment_details_length):
            data_to_insert = (
                channel_id,
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
        print(f'Migration finished for the channel: {channel_name} in {execution_time:.2f}seconds')

# if __name__ == "__main__":
#     migrate_to_sql()
