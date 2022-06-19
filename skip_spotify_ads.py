from SwSpotify import spotify
import os
import time
import datetime as dt
import warnings
warnings.simplefilter(action='ignore', category=UserWarning)


SPOTIFY_IN_QUOTES = '"Spotify"'
DELAY = 0.5 # Seconds

os.system('clear')
print("=============================================================================================================")
print("\
   ▒█▀▀▀█ █░█ ░▀░ █▀▀█ 　 ▒█▀▀▀█ █▀▀█ █▀▀█ ▀▀█▀▀ ░▀░ █▀▀ █░░█ 　 ░█▀▀█ █▀▀▄ █▀▀    |\  zzz _,,,---,,_ \n\
   ░▀▀▀▄▄ █▀▄ ▀█▀ █░░█ 　 ░▀▀▀▄▄ █░░█ █░░█ ░░█░░ ▀█▀ █▀▀ █▄▄█ 　 ▒█▄▄█ █░░█ ▀▀█    /,`.-'`'    -.  ;-;;,_ \n\
   ▒█▄▄▄█ ▀░▀ ▀▀▀ █▀▀▀ 　 ▒█▄▄▄█ █▀▀▀ ▀▀▀▀ ░░▀░░ ▀▀▀ ▀░░ ▄▄▄█ 　 ▒█░▒█ ▀▀▀░ ▀▀▀   |,>)  ) )-,_..;\ (  `'-' \n\
  -------------------------------------------------------------- by b0rd2dEAth --'---''(_/--'--`-'\_)------")
print("=============================================================================================================")

last = ('', '')
while True:
    try:
        current = spotify.current()
    except Exception as e:
        current = ('', '')
    
    if current == ('Advertisement', ''):
        os.system('pkill -x Spotify')
        os.system('open /Applications/Spotify.app')
        os.system(f"osascript -e 'tell application {SPOTIFY_IN_QUOTES} to play next track'")
        print(f'[{dt.datetime.now()}] Ads have been skipped. :)')
    elif current != ('', '') and last != current:
        print(f'[{dt.datetime.now()}] Currently Playing: {current[0]} by {current[1]}')
    
    last = current
    time.sleep(DELAY)
