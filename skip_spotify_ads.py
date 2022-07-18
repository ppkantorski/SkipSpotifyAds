from SwSpotify import spotify
import threading
import subprocess
import os
import time
import datetime as dt
import random
import warnings
warnings.simplefilter(action='ignore', category=UserWarning)


SPOTIFY_IN_QUOTES = '"Spotify"'
CHECK_BUFFER = 0.5 # Seconds
LOOP_BUFFER = 0.1
TIMEOUT_THRESHOLD = 5
BANNER = ("\
=============================================================================================================\n\
                                                                                       zzz                   \n\
   ▒█▀▀▀█ █░█ ░▀░ █▀▀█ 　 ▒█▀▀▀█ █▀▀█ █▀▀█ ▀▀█▀▀ ░▀░ █▀▀ █░░█ 　 ░█▀▀█ █▀▀▄ █▀▀    |\ z    _,,,---,,_         \n\
   ░▀▀▀▄▄ █▀▄ ▀█▀ █░░█ 　 ░▀▀▀▄▄ █░░█ █░░█ ░░█░░ ▀█▀ █▀▀ █▄▄█ 　 ▒█▄▄█ █░░█ ▀▀█    /,`.-'`'    -.  ;-;;,_     \n\
   ▒█▄▄▄█ ▀░▀ ▀▀▀ █▀▀▀ 　 ▒█▄▄▄█ █▀▀▀ ▀▀▀▀ ░░▀░░ ▀▀▀ ▀░░ ▄▄▄█ 　 ▒█░▒█ ▀▀▀░ ▀▀▀   |.>}  ) )-,_..;\ (  `'-'    \n\
  -------------------------------------------------------------- by b0rd2dEAth --'---''(_/--'--`-'\_)------   \n\
=============================================================================================================\
")
ONE_LINE_BANNERS = [
    '(x_x) [o_o] (^.^) ("-") (T.T)',
    '_.~"(_.~"(_.~"(_.~"(_.~"(',
    '(<>..<>)  -=:o:=-  (<>..<>)',
    '(<(<>(<>.(<>..<>).<>)<>)>)',
    '//\\\\(oo)//\\\\  /\\oo/\\  //\\\\(oo)//\\\\',
    '[($)] [($)] [($)] [($)] [($)]',
    '*(>=^‿‿^=) <3 (=^‿‿^=<)*',
    '@)}---^-----  ~♡ ⓛ ⓞ ⓥ ⓔ ♡~',
    '_.~"~._.~"~._.~"~._.~"~._.~"~._',
    '>>------> >>------>  ((+))',
    'c|█| c|█| c|▄| c|▄| c|_| c|_|',
    '░▀░   ░▀░   ░▀░   ▒▀▒   ░▀░',
    '▀█▄ ▄█▀ ▀█▀ █▀▀ ▀▀█ ██ ▀▀▀▀',
    '_.~"~._(-(-_(-_-)_-)-)_.~"~._',
    '─=≡Σ((( つ◕ل͜◕)つ)xxxxx[;;;;;;;;;>',
    '<(''<)  <( ' ' )>  (> '')>',
    '(ノಠ益ಠ)ノ彡   ლ(ಠ益ಠლ)╯',
    '龴(ↀ◡ↀ)龴   ^(ↀᴥↀ)^   龴(ↀ◡ↀ)龴',
    '☁ ▅▒░☼‿☼░▒▅ ☁ ▅▒░☼_☼░▒▅ ☁ ▅▒░☼.☼░▒▅ ☁',
    '¸¸♬·¯·♩¸¸♪·¯·♫¸¸♬·¯·♩¸¸♪·¯·♫¸¸',
    '(✿ ♥‿♥)︻╦╤─    ༼☉ɷ⊙༽ (✖╭╮✖)',
    '(╯°□°)--︻╦╤─ - - - - - - ',
    '┏(-_-)┛┗(-_-)┓┗(-_-)┛┏(-_-)┓',
    'd(^o^)b ¸¸♬·¯·♩¸¸♪·¯·♫¸¸♪·¯·♫¸¸',
    '( •_•)O*¯`·.¸.·´¯`°Q(•_• )',
    '◢♂◣◥♀◤◢♂◣◥♀◤◢♂◣◥♀◤◢♂◣◥♀◤◢♂◣◥♀◤',
    '––•–√\\/––√\\/––•––––•–√\\/––√\\/––•––',
    '┻━┻︵  \\(°□°)/ ︵ ┻━┻ ',
    '(c ͡|Q ͜ʖ ͡o)-c[█]     ٩(͡๏̯͡๏)۶ c[○┬●]כ ',
    '♪┏(°.°)┛┗(°.°)┓┗(°.°)┛┏(°.°)┓♪',
    'ʕ•̫͡•ʕ*̫͡*ʕ•͓͡•ʔ-̫͡-ʕ•̫͡•ʔ*̫͡*ʔ-̫͡-ʔ',
    '┌∩┐(◣_◢)┌∩┐  </3  ┌∩┐(◣_◢)┌∩┐',
    '(づ ￣ ³￣)づ    Ⓢ Ⓜ Ⓞ Ⓞ Ⓣ Ⓗ',
    '༼ つ ͡◕ Ѿ ͡◕ ༽つ ლ(́◕◞Ѿ◟◕‵ლ)',
    'ᕙ༼ ,,ԾܫԾ,, ༽ᕗ ᕙ༼ ,,இܫஇ ,, ༽ᕗ',
    '♪└(￣◇￣)┐♪└(￣◇￣)┐♪└(￣◇￣)┐♪'
]


def main():
    
    os.system('clear')
    print(BANNER)
    notify(title="Skip Spotify Ads", message=f"Skip Spotify Ads is now live!")
    
    banner_indexes = list(range(len(ONE_LINE_BANNERS)))
    random.shuffle(banner_indexes)
    
    
    last = None
    while True:
        try:
            current = spotify.current()
        except Exception as e:
            current = ('', '')
        
        if current == ('Advertisement', ''):
            if process_is_running('Spotify'):
                os.system('killall Spotify')
            time.sleep(LOOP_BUFFER)
            time_in = time.time()
            while True:
                if not process_is_running('Spotify'):
                    try:
                        os.system(f'open -gj -a {SPOTIFY_IN_QUOTES}')
                    except:
                        pass
                time.sleep(LOOP_BUFFER)
                time_out = time.time()-time_in
                if process_is_running('Spotify') or time_out > TIMEOUT_THRESHOLD:
                    break
            time_in = time.time()
            while True:
                if process_is_running('Spotify'):
                    os.system(f"osascript -e 'tell application {SPOTIFY_IN_QUOTES} to play next track'")
                    break
                time.sleep(LOOP_BUFFER)
                time_out = time.time()-time_in
                if not process_is_running('Spotify') or time_out > TIMEOUT_THRESHOLD:
                    break
            if time_out <= TIMEOUT_THRESHOLD:
                banner_index = banner_indexes.pop(0)
                if len(banner_indexes) == 0:
                    banner_indexes = list(range(len(ONE_LINE_BANNERS)))
                    random.shuffle(banner_indexes)
                print(f'[{dt.datetime.now()}] Ads have been skipped. {ONE_LINE_BANNERS[banner_index]}')
                notify(title="Skip Spotify Ads", message=f"Ads have been skipped.\n{ONE_LINE_BANNERS[banner_index]}")
        elif current != ('', '') and last != ('', '') and last != current:
            print(f'[{dt.datetime.now()}] Now Playing: {current[0]} by {current[1]}')
            notify(title="Skip Spotify Ads", message=f"Now Playing:\n{current[0]} by {current[1]}".replace('"', '\\"'))
        last = current
        time.sleep(CHECK_BUFFER)


# For making object run in background
def background_thread(target, args_list):
    args = ()
    for arg in args_list:
        args += (arg,)
    pr = threading.Thread(target=target, args=args)
    pr.daemon = True
    pr.start()
    return pr

def notify(title, message):
    background_thread(notify_command, [title, message])

def notify_command(title, message):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(message, title))

def process_is_running(process_name):
    try:
        call = subprocess.check_output(f"pgrep -f '{process_name}'", shell=True)
        return True
    except subprocess.CalledProcessError:
        return False


if __name__ == '__main__':
    main()
