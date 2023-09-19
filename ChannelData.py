import pymongo
from googleapiclient.discovery import build
from requests import HTTPError
from googleapiclient.errors import HttpError

def get_channel_stats(youtube, channel_id):
    all_data = []

    request = youtube.channels().list(part="snippet,contentDetails,statistics", id=channel_id)
    response = request.execute()

    for i in response.get('items', []):
        data = {
            'Channel Id': channel_id,
            'Channel Name': i['snippet']['title'],
            'Subscribers': i['statistics']['subscriberCount'],
            'Views': i['statistics']['viewCount'],
            'Total Videos': i['statistics']['videoCount'],
            'Playlist Id': i['contentDetails']['relatedPlaylists']['uploads']
        }
        all_data.append(data)

    return all_data

# Set the playlist ID for which we want to retrieve video IDs
# Function to get video IDs from playlist IDs
def get_videos_ids(youtube, channel_playlist_id):
    # Create an empty list to store the video IDs
    videos_ids = []

    request = youtube.playlistItems().list(
        part="contentDetails",
        playlistId=channel_playlist_id,
        maxResults=50
    )

    # Execute the request and get the response
    response = request.execute()

    # Extract video IDs from the response and add to the list
    for item in response['items']:
        video_id = item['contentDetails']['videoId']
        videos_ids.append(video_id)

    # Check if there are more pages of videos
    while 'nextPageToken' in response:
        request = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=channel_playlist_id,
            maxResults=50,
            pageToken=response['nextPageToken']
        )

        response = request.execute()

        # Extract video IDs from the response and add to the list
        for item in response['items']:
            video_id = item['contentDetails']['videoId']
            videos_ids.append(video_id)
                
    return videos_ids

def get_channel_playlists(youtube, channel_id):
    all_playlists = []

    try:
        request = youtube.playlists().list(
            part="snippet,contentDetails",
            channelId=channel_id,
            maxResults=50  # You can adjust this value based on your needs
        )

        response = request.execute()

        for item in response['items']:
            playlist_data = {
                'Channel Name': item['snippet']['channelTitle'],
                'Playlist Name': item['snippet']['title'],
                'Playlist ID': item['id'],
                'Description': item['snippet']['description'],
                'Video Count': item['contentDetails']['itemCount']
            }
            all_playlists.append(playlist_data)

        # Check if there are more pages of playlists
        while 'nextPageToken' in response:
            request = youtube.playlists().list(
                part="snippet,contentDetails",
                channelId=channel_id,
                maxResults=50,
                pageToken=response['nextPageToken']
            )

            response = request.execute()

            for item in response['items']:
                playlist_data = {
                    'Playlist Name': item['snippet']['title'],
                    'Playlist ID': item['id'],
                    'Description': item['snippet']['description'],
                    'Video Count': item['contentDetails']['itemCount']
                }
                all_playlists.append(playlist_data)

    except HTTPError as e:
        print(f"Error fetching playlists: {e}")

    return all_playlists

def get_video_details(youtube, video_ids):

    all_video_info = []
    
    for i in range(0, len(video_ids), 50):
        request = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            id=','.join(video_ids[i:i+50])
        )
        response = request.execute() 

        for video in response['items']:
            stats_to_keep = {'snippet': ['channelTitle', 'title', 'description', 'tags', 'publishedAt'],
                             'contentDetails': ['duration', 'definition', 'caption'],
                             'statistics': ['viewCount', 'likeCount', 'dislikeCount', 'favouriteCount', 'commentCount']
                             
                            }
            video_info = {}
            video_info['video_id'] = video['id']

            for k in stats_to_keep.keys():
                for v in stats_to_keep[k]:
                    try:
                        video_info[v] = video[k][v]
                    except:
                        video_info[v] = None
            all_video_info.append(video_info)
    
    return all_video_info  

def get_comment_details(youtube, video_ids):
    all_comments = []

    for video_id in video_ids:
        try:
            request = youtube.commentThreads().list(
                part="snippet",
                videoId=video_id,
                maxResults=100
            )

            response = request.execute()

            for item in response['items']:
                comment_details = {
                    'commentId': item['id'],
                    'videoId': video_id,
                    'authorDisplayName': item['snippet']['topLevelComment']['snippet']['authorDisplayName'],
                    'publishedAt': item['snippet']['topLevelComment']['snippet']['publishedAt'],
                    'textDisplay': item['snippet']['topLevelComment']['snippet']['textDisplay']
                }
                all_comments.append(comment_details)

            # Check if there are more pages of comments
            while 'nextPageToken' in response:
                request = youtube.commentThreads().list(
                    part="snippet",
                    videoId=video_id,
                    maxResults=100,
                    pageToken=response['nextPageToken']
                )
                
                response = request.execute()

                for item in response['items']:
                    comment_details = {
                        'commentId': item['id'],
                        'videoId': video_id,
                        'authorDisplayName': item['snippet']['topLevelComment']['snippet']['authorDisplayName'],
                        'publishedAt': item['snippet']['topLevelComment']['snippet']['publishedAt'],
                        'textDisplay': item['snippet']['topLevelComment']['snippet']['textDisplay']
                    }
                    all_comments.append(comment_details)

        except HttpError as e:
            if 'commentsDisabled' in str(e):
                print(f"Comments are disabled for video with ID: {video_id}")
            else:
                print(f"Error fetching comments for video with ID {video_id}: {e}")

    return all_comments

def getChannelData(youtube, channel_id):
    print('Fetch process started for channel_id:', channel_id)
    channel_details = get_channel_stats(youtube, channel_id)
    playlist_details = get_channel_playlists(youtube, channel_id)
    video_ids = get_videos_ids(youtube, channel_details[0]['Playlist Id'])
    video_details = get_video_details(youtube, video_ids)
    comment_details = get_comment_details(youtube, video_ids)
    print('Fetch process ended for channel_id:', channel_id)

#     # Assuming you have the necessary comment_details function
#     cm = comment_details(video_ids[0])
    data = {
        'channel_details': channel_details,
        'playlist_details': playlist_details,
        'video_details': video_details,
        'comment_details': comment_details
    }

    return data

# Define a main method
def main():
    # Define your API key
    api_key = 'AIzaSyDZriL-vfkvXgVHgchRkp__ALp7Ir9Z9gk'
    channel_ids = ['UCvyBHHuExqhMOG2vHqkggXA', 'UCpR62MSOeBQVXub13xwZ8aA', 'UCu7Zwf4X_OQ-TEnou0zdyRA',
                   'UC_uuQgT36XQCp4WQim6In-Q', 'UCzBjutX2PmitNF4avysL-vg', 'UC78Ib99EBhMN3NemVjYm3Ig',
                   'UCmBuL9OfCclzvTyJB5OYSFw', 'UCOn8m3Y9rtZ6_T0ht8o6nAA', 'UCEo_JfTH_9FK-7k9-mAWJkQ',
                   'UC0imHw-zG3H0wyXgd06bNLg']
    # Specify the API service name and version
    api_service_name = "youtube"
    api_version = "v3"

    # Create the YouTube Data API client
    youtube = build(api_service_name, api_version, developerKey=api_key)
    myclient = pymongo.MongoClient("mongodb+srv://meetafhere:test123@cluster0.ysvxil8.mongodb.net/?retryWrites=true&w=majority")
    mydb = myclient["youtube"]
    mycol = mydb["channels"]

    for channel_id in channel_ids:
        result = getChannelData(youtube, channel_id)
        mycol.insert_one(result)
        print('\n')

# Run the main method if this script is executed
if __name__ == "__main__":
    main()
