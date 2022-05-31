import spotipy
import constants
from spotipy.oauth2 import SpotifyClientCredentials

# Move to another place later
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
  client_id=constants.spotify_client_id,
	client_secret=constants.spotify_client_secret))

house_playlist = sp.playlist_tracks(playlist_id="5ZhYpkuIMDnaX8uDWdBbAv")

for track in house_playlist["items"]:
  #URI
  track_uri = track["track"]["uri"]
  
  #Track name
  track_name = track["track"]["name"]
  
  #Main Artist
  artist_uri = track["track"]["artists"][0]["uri"]
  artist_info = sp.artist(artist_uri)
  
  #Name, popularity, genre
  artist_name = track["track"]["artists"][0]["name"]
  artist_pop = artist_info["popularity"]
  artist_genres = artist_info["genres"]
  
  #Album
  album = track["track"]["album"]["name"]
  
  #Popularity of the track
  track_pop = track["track"]["popularity"]

  #Track Features
  track_danceability = sp.audio_features(track_uri)[0]['danceability']
  track_bpm = sp.audio_features(track_uri)[0]['tempo']
  
  print(track_name, str(track_danceability*100)+"%", track_bpm)
  

