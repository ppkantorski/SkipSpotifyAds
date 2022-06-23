from SwSpotify import spotify
import os
import time
import datetime as dt
import random
import warnings
warnings.simplefilter(action='ignore', category=UserWarning)


SPOTIFY_IN_QUOTES = '"Spotify"'
CHECK_BUFFER = 0.5 # Seconds

os.system('clear')

BANNER = ("\
=============================================================================================================\n\
                                                                                       zzz                   \n\
   ▒█▀▀▀█ █░█ ░▀░ █▀▀█ 　 ▒█▀▀▀█ █▀▀█ █▀▀█ ▀▀█▀▀ ░▀░ █▀▀ █░░█ 　 ░█▀▀█ █▀▀▄ █▀▀    |\ z    _,,,---,,_         \n\
   ░▀▀▀▄▄ █▀▄ ▀█▀ █░░█ 　 ░▀▀▀▄▄ █░░█ █░░█ ░░█░░ ▀█▀ █▀▀ █▄▄█ 　 ▒█▄▄█ █░░█ ▀▀█    /,`.-'`'    -.  ;-;;,_     \n\
   ▒█▄▄▄█ ▀░▀ ▀▀▀ █▀▀▀ 　 ▒█▄▄▄█ █▀▀▀ ▀▀▀▀ ░░▀░░ ▀▀▀ ▀░░ ▄▄▄█ 　 ▒█░▒█ ▀▀▀░ ▀▀▀   |.>}  ) )-,_..;\ (  `'-'    \n\
  -------------------------------------------------------------- by b0rd2dEAth --'---''(_/--'--`-'\_)------   \n\
=============================================================================================================\
")
print(BANNER)

ONE_LINE_BANNERS = [
    '(x_x) [o_o] (^.^) ("-") (T.T)',
    '_.~"(_.~"(_.~"(_.~"(_.~"(',
    '(<>..<>)  -=:o:=-  (<>..<>)',
    '//\\\\(oo)//\\\\  /\\oo/\\  //\\\\(oo)//\\\\',
    '[($)] [($)] [($)] [($)] [($)]',
    '(>=^‿‿^=) <3 (=^‿‿^=<)',
    '@)}---^-----  ~♡ⓛⓞⓥⓔ♡~',
    '_.~"~._.~"~._.~"~._.~"~._',
    '>>------> >>------>  ((+))',
    'c|█| c|█| c|▄| c|▄| c|_| c|_|',
    '░▀░   ░▀░   ░▀░   ▒▀▒   ░▀░',
    '▀█▄ ▄█▀ ▀█▀ █▀▀ ▀▀█ ██ ▀▀▀▀',
    '^^^^\(-(-_(-_-)_-)-)/^^^^',
    '(<(<>(<>.(<>..<>).<>)<>)>)',
    ')xxxxx[;;;;;;;;;>',
    '<(''<)  <( ' ' )>  (> '')>',
    '(ノಠ益ಠ)ノ彡   ლ(ಠ益ಠლ)╯',
    '٩(͡๏̯͡๏)۶  duf.  c[○┬●]כ ',
    '龴ↀ◡ↀ龴   ^ↀᴥↀ^   龴ↀ◡ↀ龴',
    '☁ ▅▒░☼‿☼░▒▅ ☁ ▅▒░☼_☼░▒▅ ☁',
    '¸¸♬·¯·♩¸¸♪·¯·♫¸¸♬·¯·♩¸¸♪·¯·♫¸¸',
    '(✿ ♥‿♥)︻╦╤─    ༼☉ɷ⊙༽ (✖╭╮✖)',
    '(╯°□°)--︻╦╤─ - - - ',
    '┏(-_-)┛┗(-_-)┓┗(-_-)┛┏(-_-)┓',
    'd(^o^)b ¸¸♬·¯·♩¸¸♪·¯·♫¸¸',
    '( •_•)O*¯`·.¸.·´¯`°Q(•_• )',
    '◢♂◣◥♀◤◢♂◣◥♀◤◢♂◣◥♀◤◢♂◣◥♀◤◢♂◣◥♀◤',
    '––•–√\\/––√\\/––•––––•–√\\/––√\\/––•––',
    '┻━┻︵  \(°□°)/ ︵ ┻━┻ ',
    '(c ͡|Q ͜ʖ ͡o)-c[_]',
    '♪┏(°.°)┛┗(°.°)┓┗(°.°)┛┏(°.°)┓♪',
    'ʕ•̫͡•ʕ*̫͡*ʕ•͓͡•ʔ-̫͡-ʕ•̫͡•ʔ*̫͡*ʔ-̫͡-ʔ',
    '┌∩┐(◣_◢)┌∩┐  </3  ┌∩┐(◣_◢)┌∩┐',
    '(づ ￣ ³￣)づ    ⓈⓂⓄⓄⓉⒽ',
    '─=≡Σ((( つ◕ل͜◕)つ',
    '༼ つ ͡◕ Ѿ ͡◕ ༽つ ლ(́◕◞Ѿ◟◕‵ლ)',
    'ᕙ༼ ,,ԾܫԾ,, ༽ᕗ ᕙ༼ ,,இܫஇ,, ༽ᕗ',
    '♪└(￣◇￣)┐♪└(￣◇￣)┐♪└(￣◇￣)┐♪'
]


banner_indexes = list(range(len(ONE_LINE_BANNERS)))
random.shuffle(banner_indexes)


last = None
while True:
    try:
        current = spotify.current()
    except Exception as e:
        current = ('', '')
    
    if current == ('Advertisement', ''):
        os.system('pkill -x Spotify; open /Applications/Spotify.app')
        time.sleep(0.02)
        os.system(f"osascript -e 'tell application {SPOTIFY_IN_QUOTES} to play next track'")
        banner_index = banner_indexes.pop(0)
        if len(banner_indexes) == 0:
            banner_indexes = list(range(len(ONE_LINE_BANNERS)))
            random.shuffle(banner_indexes)
        print(f'[{dt.datetime.now()}] Ads have been skipped. {ONE_LINE_BANNERS[banner_index]}')
    elif current != ('', '') and last != ('', '') and last != current:
        print(f'[{dt.datetime.now()}] Now Playing: {current[0]} by {current[1]}')
    
    last = current
    time.sleep(CHECK_BUFFER)
