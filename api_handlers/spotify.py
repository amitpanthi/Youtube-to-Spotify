import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth

class Spotify:
	def __init__(self, client_id, client_secret, uid):
		self.client_id = client_id
		self.client_secret = client_secret
		self.uid = uid

	def generate(self, playlist_name, songs_list):
		token = SpotifyClientCredentials(client_id=self.client_id, client_secret=self.client_secret)
		cache_token = token.get_access_token()
		sp = spotipy.Spotify(cache_token)

		response = sp.user_playlist_create(user=self.uid, name=playlist_name, public=False)

		print(response)
