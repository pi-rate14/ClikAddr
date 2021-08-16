from spotifyToken import SPOTIFY_KEY
from spotify_client import SpotifyClient
from youtube_client import YouTubeClient

spotifyKey = SPOTIFY_KEY

def run():
    youtube_client = YouTubeClient('./creds/client_secret.json')
    spotify_client = SpotifyClient(spotifyKey)
    playlists = youtube_client.get_playlists()

    for index, playlist in enumerate(playlists):
        print(f"{index}: {playlist.title}")
    choice = int(input("enter your choice: "))
    chosen_playlist = playlists[choice] 
    print(f"You Selected: {chosen_playlist.title}")

    songs = youtube_client.get_videos_from_playlist(chosen_playlist.id)
    print(f"Attempting to add {len(songs)}")

    for song in songs: 
        spotify_song_id = spotify_client.search_song(song.artist, song.track)
        if spotify_song_id:
            added_song = spotify_client.add_song_to_spotify(spotify_song_id)
            if added_song:
                print(f"Added {song.artist}") 
if __name__ == '__main__':
    run()