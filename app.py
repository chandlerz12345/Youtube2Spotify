import json
import requests
from secrets import spotify_user_id

class CreatePlaylist:
    def __init__(self):
        self.user_id = 

    def get_youtube_client(self):
        pass
    def get_liked_videos(self):
        pass
    def create_playlist(self):
        request_body = json.dumps({}
            "name" + "Youtube Liked Vids",
            "description": "All Liked Youtube Videos",
            "public": True
        })

        query = "https://api.spotify.com/v1/users/{}/playlists".format(self.user_id)
        response = requests.post (
            query,
            data = request_body,
            headers = (
                "Content_Type":"application/json"
                "Authorization" : "Bearer {}".format(spotify_token)
            )
        )
        response_json = response.json()

        return response_json["id"]

    def get_spotify_uri(self, song_name, artist):
        pass


    def add_song_to_playlist(self):
        pass

