from flask import Flask, render_template
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app =  Flask(__name__)
app.config.from_pyfile('settings.py')

@app.route("/")
def index():
    birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

    results = spotify.artist_albums(birdy_uri, album_type='album')
    albums = results['items']
    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])
    
    return render_template("index.html", albums=albums)

@app.route('/samples/')
def second_samples():
    lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    results = spotify.artist_top_tracks(lz_uri)
    
    return render_template("samples.html", results=results['tracks'][:10])
