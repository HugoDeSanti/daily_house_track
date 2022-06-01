import spotipy
import constants
import random
from spotipy.oauth2 import SpotifyClientCredentials



def main():
  sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=constants.spotify_client_id,
    client_secret=constants.spotify_client_secret))

  house_playlist = sp.playlist_tracks(playlist_id="5ZhYpkuIMDnaX8uDWdBbAv")
  playlist_len = find_playlist_length('5ZhYpkuIMDnaX8uDWdBbAv')
  track_number = random.randrange(1,playlist_len)

  # Find the actual song that pertains to the randonmly generated song_number
  # You have to loop through the iterator since Spotify only displays 100 songs
  # at a time, if you want the rest of the songs you have to scroll
  # See the find_playlist_length function for the same logic
  for i in range(int(track_number/100)):
    house_playlist = sp.next(house_playlist)

  track = house_playlist["items"][track_number%100-1]
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
  track_danceability = str(round(sp.audio_features(track_uri)[0]['danceability'], 2) * 100) + "%"
  track_bpm = int(round(sp.audio_features(track_uri)[0]['tempo'], 0))
  track_energy = sp.audio_features(track_uri)[0]['energy']
  
  print("Track:", track_name)
  print("Artist:", artist_name)
  print("BPM:", track_bpm)
  print("Danceability:", track_danceability)
  print("Energy:", track_energy)



def find_playlist_length(playlist_id):
  sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=constants.spotify_client_id,
    client_secret=constants.spotify_client_secret))

  counter = 0
  playlist = sp.playlist_tracks(playlist_id)

  # Spotify API limits house_playlist to 100 tracks, so I need the following piece
  # of code to continue looping through the songs.
  while playlist:
    for track in playlist["items"]:
      counter += 1
    if playlist['next']:
      playlist = sp.next(playlist)
    else:
      playlist = None
  return counter

main()
  
  


  