import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import os
from dotenv import load_dotenv
load_dotenv()
from bs4 import BeautifulSoup

# Replace these with your Spotify app credentials
CLIENT_ID = os.getenv('Spotify_Client_ID')
CLIENT_SECRET = os.getenv('Spotify_Client_Secret')

# Ensure the redirect URL matches the one in your Spotify Developer Dashboard
REDIRECT_URL = "http://localhost:8888/callback"
SCOPE = "playlist-modify-private"

# Prompt user for a date
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# Fetch Billboard Hot 100 chart for the given date
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
webpage = response.content
soup = BeautifulSoup(webpage, 'html.parser')

# Extract song titles
song_titles = soup.select(selector="div li h3#title-of-a-story")
song_list = [title.getText().strip() for title in song_titles]

# Extract artist names
artists = soup.select(selector="div li.lrv-u-width-100p span")
artist_list = [artist.getText().strip() for artist in artists if not artist.getText().strip().isdigit() and "-" not in artist.getText().strip()]

# Spotify authentication
auth_sp = SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URL
)
token = auth_sp.get_access_token(as_dict=False)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope=SCOPE,
    redirect_uri=REDIRECT_URL,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    show_dialog=True,
    cache_path="token.txt"
))

# Get user ID
user_id = sp.current_user()["id"]

# Search for tracks and collect URIs
song_uris = []
year = date.split("-")[0]

for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Create a new playlist
playlist = sp.user_playlist_create(
    user=user_id,
    name="Pythonista playlist",
    public=False,
    description="Playlist created by Python code"
)
print(playlist)

# Get playlist ID
spotify_playlist_id = playlist["uri"]
print(spotify_playlist_id)
spotify_playlist_id_found = spotify_playlist_id.split(":")[2]
print(spotify_playlist_id_found)

# Add items to the playlist
item_list = []
for index in range(min(100, len(song_list))):  # Ensure we don't exceed the length of song_list
    song = song_list[index]
    artist = artist_list[index]
    query = sp.search(q=f"track:{song} artist:{artist}", type="track", limit=1, market="US")
    try:
        song_uri = query["tracks"]["items"][0]["uri"]
        item_list.append(song_uri)
    except IndexError:
        print(f"Track {song} not found")
        continue

print(playlist)
print(item_list)

# Add items to the playlist
added = sp.playlist_add_items(playlist_id=playlist["id"], items=item_list)
print(added)
