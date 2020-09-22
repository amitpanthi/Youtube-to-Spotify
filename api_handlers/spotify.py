
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
import os

class Spotify:
	def __init__(self, username, client_id, client_secret):
		self.username = username
		self.client_id = client_id
		self.client_secret = client_secret


	def initSpot(self):
		scope = 'playlist-modify-public'

		token = util.prompt_for_user_token(self.username, scope, client_id=self.client_id, client_secret=self.client_secret, redirect_uri='https://example.com/callback/')
		sp = spotipy.Spotify(auth=token)
		return sp


	def getPlaylistID(self, spotify, username, playlist_name):
		playlists = spotify.user_playlists(username)
		for playlist in playlists["items"]:
			if playlist["name"]==playlist_name:
				return playlist['id']



	def getTracks(self, spotify, songs_list):
		ids = []

		for song in songs_list:
			res = spotify.search(song, limit=1, type='track')
			if(res['tracks']['total'] == 0): #could not find a song
				continue
			else:
				ids.append(res['tracks']['items'][0]['id'])

		return ids

	def generate(self, playlist_name, songs_list):
		# create a spotify object
		spotify = self.initSpot()

		# create the playlist
		spotify.user_playlist_create(self.username, name=playlist_name, public=True) #creates a playlist with the given name

		# get the playlist id
		playlist_id = self.getPlaylistID(spotify, self.username, playlist_name)
		
		# search for each track in the songs list
		track_list = self.getTracks(spotify, songs_list)

		# add the track ids onto your playlist
		spotify.user_playlist_add_tracks(user=self.username, playlist_id=playlist_id ,tracks=track_list)

