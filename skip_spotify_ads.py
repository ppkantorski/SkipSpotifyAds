from SwSpotify import spotify
import os
import time
import datetime as dt
import warnings
warnings.simplefilter(action='ignore', category=UserWarning)


SPOTIFY_IN_QUOTES = '"Spotify"'
CHECK_BUFFER = 0.5 # Seconds

os.system('clear')
print("=============================================================================================================")
print("                                                                                        zzz                  \n\
   ▒█▀▀▀█ █░█ ░▀░ █▀▀█ 　 ▒█▀▀▀█ █▀▀█ █▀▀█ ▀▀█▀▀ ░▀░ █▀▀ █░░█ 　 ░█▀▀█ █▀▀▄ █▀▀    |\  z   _,,,---,,_       \n\
   ░▀▀▀▄▄ █▀▄ ▀█▀ █░░█ 　 ░▀▀▀▄▄ █░░█ █░░█ ░░█░░ ▀█▀ █▀▀ █▄▄█ 　 ▒█▄▄█ █░░█ ▀▀█    /,`.-'`'    -.  ;-;;,_   \n\
   ▒█▄▄▄█ ▀░▀ ▀▀▀ █▀▀▀ 　 ▒█▄▄▄█ █▀▀▀ ▀▀▀▀ ░░▀░░ ▀▀▀ ▀░░ ▄▄▄█ 　 ▒█░▒█ ▀▀▀░ ▀▀▀   |,4)  ) )-,_..;\ (  `'-'  \n\
  -------------------------------------------------------------- by b0rd2dEAth --'---''(_/--'--`-'\_)------")
print("=============================================================================================================")

    
ONE_LINE_BANNERS = [
    '(^_^) [o_o] (^.^) (".") ($.$)',
    '_.~"(_.~"(_.~"(_.~"(_.~"(',
    '(<>..<>)  (<>..<>)',
    '//\(oo)/\\\\ //\(oo)/\\\\',
    '[($)] [($)] [($)] [($)]',
    '=^_^= <3',
    '@)}---^-----',
    '_.~"~._.~"~._.~"~._.~"~._',
    '>>------> (+)'
]
banner_indexes = list(range(len(ONE_LINE_BANNERS)))
banner_indexes.shuffle()

last = None
while True:
    try:
        current = spotify.current()
    except Exception as e:
        current = ('', '')
    
    if current == ('Advertisement', ''):
        os.system('pkill -x Spotify')
        os.system('open /Applications/Spotify.app')
        os.system(f"osascript -e 'tell application {SPOTIFY_IN_QUOTES} to play next track'")
        banner_index = banner_indexes.pop(0)
        if len(banner_indexes) == 0:
            banner_indexes = list(range(len(ONE_LINE_BANNERS)))
            banner_indexes.shuffle()
        print(f'[{dt.datetime.now()}] Ads have been skipped. {ONE_LINE_BANNERS[banner_index]}')
    elif current != ('', '') and last != ('', '') and last != current:
        print(f'[{dt.datetime.now()}] Currently Playing: {current[0]} by {current[1]}')
    
    last = current
    time.sleep(CHECK_BUFFER)
