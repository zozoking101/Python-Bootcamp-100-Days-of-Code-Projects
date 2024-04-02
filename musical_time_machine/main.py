import requests
from bs4 import BeautifulSoup
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint


date = input("What year you would like to travel to? \n"
             "Type the date in YYYY-MM-DD format: ")

URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(URL)
print(response.status_code)
data = response.text

web_soup = BeautifulSoup(data, "html.parser")
pretty_data = web_soup.prettify()

with open("billboard_top_100.txt", mode="w") as f:
    f.write(pretty_data)

with open("billboard_top_100.txt", mode="r") as f:
    content = f.read()

soup = BeautifulSoup(content, "html.parser")
top_100_song_list = soup.select("li ul li .a-font-primary-bold-s")
top_100_songs = [i.string.strip() for i in top_100_song_list]
# print(top_100_songs)

top_100_artist_list = soup.select("li ul li .a-font-primary-s")
top_100_artists = [i.string.strip() for i in top_100_artist_list]
# print(top_100_artists)

top_100 = [f"{top_100_songs[i]} {top_100_artists[i]}" for i in range(len(top_100_artist_list))]

# for i in top_100:
#     print(i)

# 1. In order to create a playlist in Spotify you must have an account with Spotify. If you don't already have an account, you can sign up for a free one here: http://spotify.com/signup/

# 2. Once you've signed up/ signed in, go to https://developer.spotify.com/dashboard/ and create a new Spotify App:

# 3. Once you've created a Spotify app, copy the Client ID and Client Secret into your Python project.

# Spotify uses OAuth to allow third-party applications (e.g. our Python code) to access a Spotify user's account without giving them the username or password. We'll explore OAuth more in later modules on web development, but if you want you can read more about it here: https://developer.okta.com/blog/2017/06/21/what-the-heck-is-oauth

# Authenticating with Spotify is quite complicated, especially when you want to access a user's account. So instead, we're going to use one of the most popular Python Spotify modules - Spotipy to make things easier.

# Now that you've come so far and completed 45 days of Python, you're going to approach this challenge like a real developer, figuring things out from the documentation.

# 4. Using the Spotipy documentation, figure out how to authenticate your Python project with Spotify using your unique Client ID/ Client Secret.

# 5. Use http://example.com as your Redirect URI. You're looking to get the currentuser id (your Spotify username). As per the documentation, make sure you set the redirect URI in the Spotify Dashboard as well.

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost/",
        client_id=os.environ.get("SPOTIFY_CLIENT_ID"),
        client_secret=os.environ.get("SPOTIFY_CLIENT_SECRET"),
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

song_uris = []
# year = date.split("-")[0]
year = "2000"

for song in top_100:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    pprint(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# date = "2000-08-12"  # comment this practice date

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
