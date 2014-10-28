rdio2spotify
============

Imports an Rdio user's "My Collection" to a Spotify playlist

### Dependencies

1. Rdio Web Service API: `pip install rdio`
2. Spotify Web API: `pip install spotipy`

### Setup

You'll need both an Rdio and a Spotify developer account, as well as Rdio and Spotify API keys. Once you have those set up, export them as environment variables:

    $ export SPOTIPY_CONSUMER_KEY='your_spotify_consumer_id'
	$ export SPOTIPY_CONSUMER_SECRET='your_spotify_consumer_secret'
	$ export RDIO_CONSUMER_KEY='your_rdio_consumer_key'
	$ export RDIO_CONSUMER_SECRET='your_rdio_consumer_secret'

### Usage

By default, myMusicImporter imports songs to a given Spotify user's "My Music" from a given users' Rdio "Collection": `python myMusicImporter.py <rdio-username> <spotify-username>`. But myMusicImporter also supports importing from other sources as well:

- A Spotify playlist: `python myMusicImporter.py --sp-playlist-uri <spotify-playlist-uri> <spotify-username>`
- An Rdio playlist: `python myMusicImporter.py --rd-playlist-uri <rdio-playlist-uri> <spotify-username>`
