import os
from dotenv import load_dotenv

from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util

load_dotenv()
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
redirect_uri = os.getenv('REDIRECT_URI')
username = os.getenv('SPOTIFY_USERNAME')

scope = 'user-library-read'
artistScope = 'user-top-read'

## Sample Class ##
# class User:
#     def __init__(self,name,artistArr ,songArr):
#         self.username = name
#         self.artists = artistArr
#         self.songs = songArr

def main():
    sp = Spotify(auth_manager=SpotifyOAuth(client_id=client_id,client_secret=client_secret,redirect_uri=redirect_uri,scope=artistScope))

    if sp:
        user = sp.current_user()
        top_artists = sp.current_user_top_artists(limit=50, time_range="medium_term")
        count = 0

        print(f'User: {user["display_name"]}')
        print(f'ID: {user["id"]}')
        print(f'URI: {user["uri"]}')
        print("----- Top 50 Artists ----")
        for i, artist in enumerate(top_artists["items"],1):
            print(f"{i}: {artist["name"]}")

main();


