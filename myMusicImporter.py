import spotipy
import spotipy.util as util
from rdio.rdio import Rdio

def rdioCollectionForUser(rdio, user):
	"""
	
	"""
	try:
    	# authenticate against the Rdio service
    	url = rdio.begin_authentication('oob')
    	print("Go to: %s" % url)
    	verifier = raw_input("Then enter the code: ").strip()
    	rdio.complete_authentication(verifier)

    	# get tracks in collection
    	tracks = rdio.call('getTracksInCollection',
                       {'sort': 'artist', 'extras': '-*,key'})
    	if (tracks['status'] == 'ok'):
    		return tracks
		else:
        	print("ERROR: %s" % tracks['message'])
			return 1 #TODO: Return an error message?

	except HTTPError as e:
    	# if we have a protocol error, print it
    	print(e.read())	
		return 1 #TODO: Return an error message?

	return tracks 

def spotifyTrackIDForSong(sp, songName, artist):
	"""
	Returns the Spotify track ID of the first song found matching the given
	song name and artist. 
	"""
	query = "artist:" + artist + "+track:" + songName + "&type=track"
	#TODO: What if search results are empty?
	return sp.search(query, limit=1)[0]['trackID']

def main(argv):
	if len(argv) != 3:
		print "Usage: python myMusicImporter.py <spotify-username> <rdio-username>"
		return 1
	
	spotifyUser = argv[1]
	rdioUser = argv[2]

	scope = 'user-library-modify'
	token = util.prompt_for_user_token(username, scope)
	
	RDIO_CONSUMER_KEY = os.getenv('RDIO_CONSUMER_KEY')
	RDIO_CONSUMER_SECRET = os.getenv('RDIO_CONSUMER_SECRET')

	if RDIO_CONSUMER_KEY and RDIO_CONSUMER_SECRET:
		rdio = Rdio((RDIO_CONSUMER_KEY, RDIO_CONSUMER_SECRET))
		rdioCollection = rdioCollectionForUser(rdio, rdioUser)
	else:
		print "Both RDIO_CONSUMER_KEY and RDIO_CONSUMER_SECRET must be \
				set as environment variables."
		return 1 #TODO: return an error code?

	tids = [] # spotify track ids
	for rdioTrack in rdioCollection:
		tids.append(spotifyTrackIDForSong(sp, rdioTrack['name'], rdioTrack['artist']))
	if token:
		sp = spotipy.Spotify(auth=token)
		results = sp.current_user_saved_tracks_add(tracks=tids)
		#TODO: What to do with results?	
		sp.trace = False
	else:
		print "Can't get token for ", spotifyUser	
