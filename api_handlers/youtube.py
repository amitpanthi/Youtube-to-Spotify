import sys
sys.path.append('..')
from googleapiclient.discovery import build
from helper.parser import parse
from helper.text_cleaner import clean

class Youtube:
	def __init__(self, api_key):
		self.api_key = api_key

	def fetch(self, playlistId):
		#returns the song's list
		songs = []

		yt = build('youtube', 'v3', developerKey=self.api_key)
		nextPageToken = None

		# Extracting all the video titles into a single list
		while True:
			request = yt.playlistItems().list(
					part='snippet',
					playlistId=playlistId,
					maxResults=50,
					pageToken=nextPageToken
				)

			response = request.execute()
			nextPageToken = response.get('nextPageToken')

			songs += parse(response, 'title')

			if not nextPageToken:
				break

		# Preprocessing the extracted titles
		songs = clean(songs)

		return songs