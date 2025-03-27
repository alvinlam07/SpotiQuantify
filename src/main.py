import os
from dotenv import load_dotenv

from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
redirect_uri = os.getenv('REDIRECT_URI')

scope = 'user-library-read'
sp = Spotify(auth_manager=SpotifyOAuth(client_id=client_id,client_secret=client_secret,redirect_uri=redirect_uri,scope=scope))

user = sp.current_user()
print(f'User: {user["display_name"]}')
print(f'ID: {user["id"]}')
print(f'URI: {user["uri"]}')