import requests
import urllib.parse

#BQCc6Yzl1nrzX4bqGtH-iK4eiOGd_xL4FZo8D2rrIIffpMqj-fFMtGzypgxL3e2c1DT1rjORFWRp4wMXdy5KXnen-eNWc8CqaCTm_TyKqUhkZwvH-e3Zr0U6APyo2Qh5cwZ7I9qa1VEKz1pK520ceKxnbwV8Qx1PZjLZq0VMF2RwFEm4hy4JB44
class SpotifyClient(object):
    def __init__(self, api_token):
        self.api_token = api_token
    
    def search_song(self, artist, track):
        query = urllib.parse.quote(f'{artist}{track}')
        url = f"https://api.spotify.com/v1/search?q={query}&type=track"
        response = requests.get(
            url,
            headers={
                "Content-Type":"application/json",
                "Authorization": f"Bearer {self.api_token}"
            }
        ) 

        response_json = response.json()  

        results = response_json['tracks']['items']

        if results:
            return results[0]['id']
        else:
            raise Exception(f"No song found for {artist} = {track}")

    def add_song_to_spotify(self, song_id):
        url = "https://api.spotify.com/v1/me/tracks"
        response = requests.put(
            url,
            json={
                "ids" : [song_id]
            },
            headers={
                "Content-Type":"application/json",
                "Authorization": f"Bearer {self.api_token}"
            }

        )

        return response.ok
