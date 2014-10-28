import spotipy
import spotipy.util as util
import argparse

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("spotify_username", type=str, help="the Spotify user to whose 'My Music' you wish to import")
	parser.add_argument("rdio_username", type=str, help="the Rdio user from whose 'Collection' you wish to import")
	args = parser.parse_args()

	
