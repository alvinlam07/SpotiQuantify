import os
from dotenv import load_dotenv
from textwrap import dedent

import spotipy.exceptions
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
redirect_uri = os.getenv('REDIRECT_URI')

scope = 'user-library-read'
artistScope = 'user-top-read'

## Sample Class ##
# class User:
#     def __init__(self,name,artistArr ,songArr):
#         self.username = name
#         self.artists = artistArr
#         self.songs = songArr

def printChoicePrompt():
    print(dedent(f"""
    ******************************
    SpotiQuantify
    ******************************
    What would you like to do?
    1. Display Top 50 Artists
    2. Display Top 50 Tracks
    3. Exit
    """))

def getTimeRange():
    while True:
        print(dedent(f"""
        Which time range would you like to see?
        1. 12 months
        2. 6 months
        3. 4 weeks
        """))
        user_input = input('Choice: ')
        match user_input:
            case '1':
                return 'long_term'
            case '2':
                return 'medium_term'
            case '3':
                return 'short_term'
            case _:
                print('Please enter a valid choice...')

print('Starting Authorization Process...')
try:
    sp = Spotify(auth_manager=SpotifyOAuth(client_id=client_id,client_secret=client_secret,redirect_uri=redirect_uri,scope=artistScope))
except spotipy.exceptions.SpotifyBaseException as e:
    print(f'Spotify API error: {e}')
except Exception as e:
    print(f'An error occured: {e}')
finally:
    print('Authorization Process Completed!')
    user = sp.current_user()
    print(f'User: {user["display_name"]}')
    print(f'ID: {user["id"]}')
    print(f'URI: {user["uri"]}')

while True:
    printChoicePrompt()
    user_input = input('Choice: ')
    match user_input:
        case '1': # Display Top 50 Artists
            time_range = getTimeRange()
            top_artists = sp.current_user_top_artists(limit=50, time_range=time_range)
            print('----- Top 50 Artists ----')
            for i, artist in enumerate(top_artists['items'], 1):
                print(f'{i}: {artist['name']}')
        case '2': # Display Top 50 Tracks
            time_range = getTimeRange()
            top_tracks = sp.current_user_top_tracks(limit=50, time_range=time_range)
            print('----- Top 50 Tracks ----')
            for i, track in enumerate(top_tracks['items'], 1):
                print(f'{i}: {track['name']}')
        case '3': # Exit program
            break
        case _:
            print('Please enter a valid choice...')