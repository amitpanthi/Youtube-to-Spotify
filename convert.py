import credentials
from helper.text_cleaner import clean
from api_handlers.youtube import Youtube
from api_handlers.spotify import Spotify

yt_api_key = credentials.youtube_key
youtube = Youtube(yt_api_key)
#songs_list = youtube.fetch('PL7q6nAW6-CMsgIpYt9hwRycy6lShNf6wP')

spot = Spotify(credentials.spotify_client, credentials.spotify_secret, credentials.spotify_uname)
rsep = spot.generate(playlist_name="Test", songs_list="placeholder")
print(rsep)

