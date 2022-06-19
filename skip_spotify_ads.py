from SwSpotify import spotify
import os
import time
import datetime as dt
import warnings
warnings.simplefilter(action='ignore', category=UserWarning)


SPOTIFY = '"Spotify"'

print("=============================================================================================================")
print("\
   ▒█▀▀▀█ █░█ ░▀░ █▀▀█ 　 ▒█▀▀▀█ █▀▀█ █▀▀█ ▀▀█▀▀ ░▀░ █▀▀ █░░█ 　 ░█▀▀█ █▀▀▄ █▀▀    |\  zzz _,,,---,,_ \n\
   ░▀▀▀▄▄ █▀▄ ▀█▀ █░░█ 　 ░▀▀▀▄▄ █░░█ █░░█ ░░█░░ ▀█▀ █▀▀ █▄▄█ 　 ▒█▄▄█ █░░█ ▀▀█    /,`.-'`'    -.  ;-;;,_ \n\
   ▒█▄▄▄█ ▀░▀ ▀▀▀ █▀▀▀ 　 ▒█▄▄▄█ █▀▀▀ ▀▀▀▀ ░░▀░░ ▀▀▀ ▀░░ ▄▄▄█ 　 ▒█░▒█ ▀▀▀░ ▀▀▀   |,>)  ) )-,_..;\ (  `'-' \n\
  -------------------------------------------------------------------------------'---''(_/--'--`-'\_)------")
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
        os.system(f"osascript -e 'tell application {SPOTIFY} to play next track'")
        print(f'[{dt.datetime.now()}] Ads have been skipped. :)')
    elif current != ('', '') and last != current:
        print(f'[{dt.datetime.now()}] Currently Playing: {current[0]} by {current[1]}')
    
    last = current
    time.sleep(0.5)
