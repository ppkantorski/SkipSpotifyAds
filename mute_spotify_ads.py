from SwSpotify import spotify
import os
import time
import warnings
warnings.simplefilter(action='ignore', category=UserWarning)


SPOTIFY = '"Spotify"'
while True:
    try:
        current = spotify.current()
    except Exception as e:
        current = ('', '')
    
    if current == ('Advertisement', ''):
        os.system('pkill -x Spotify')
        os.system('open /Applications/Spotify.app')
        os.system(f"osascript -e 'tell application {SPOTIFY} to play next track'")
    
    time.sleep(0.5)