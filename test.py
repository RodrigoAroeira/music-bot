import builtins
import os

from dotenv import load_dotenv

# from pprint import pprint as print
from spot_client import SpotifyClient
from track import Track
from utils import extract_spotify_track_id


def canonical_from_spotify_url(
    spotify: SpotifyClient,
    url: str,
) -> Track:
    track_id = extract_spotify_track_id(url)
    if not track_id:
        raise ValueError("Invalid Spotify track URL")

    track_json = spotify.get_track(track_id)
    return Track.from_spotify_json(track_json)


def main():
    load_dotenv()
    SPOTIPY_CLIENT_ID = os.environ["SPOTIPY_CLIENT_ID"]
    SPOTIPY_CLIENT_SECRET = os.environ["SPOTIPY_CLIENT_SECRET"]

    client = SpotifyClient(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
    URL = "https://open.spotify.com/track/4wajJ1o7jWIg62YqpkHC7S?si=17ae661a9482474e"
    URL2 = "https://open.spotify.com/track/2pw9RZWZibttZzoFhwjuy6?si=6e1801bceed44881"
    # URL3 = "https://open.spotify.com/album/4WnkQO4xD9ljQooB3VIxCV?si=tNEtQ6kEQgeuLpw6ZPWRRA"
    for url in [URL, URL2]:
        can = canonical_from_spotify_url(client, url)
        print(can)
        builtins.print()


if __name__ == "__main__":
    main()
