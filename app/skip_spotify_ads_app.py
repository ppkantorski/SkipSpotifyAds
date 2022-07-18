__author__ = "Patrick Kantorski"
__version__ = "1.0.3"
__maintainer__ = "Patrick Kantorski"
__status__ = "Development Build"

import rumps
import os, sys
import importlib
import time
#import webbrowser
import threading
import json


app_path = os.path.dirname(os.path.abspath( __file__ ))
data_path = app_path.replace('/app', '/data')
sys.path.append(data_path)
sys.dont_write_bytecode = True


# Import SkipSpotifyAds
from skip_spotify_ads import SkipSpotifyAds


class SkipSpotifyAdsApp(object):
    def __init__(self):
        # Initialize SkipSpotifyAds
        self.skip_spotify_ads = SkipSpotifyAds()
        
        # Overload the SkipSpotifyAds notify function
        self.skip_spotify_ads.notify = self.notify
        
        # For detecting termination
        #self.has_terminated = False
        
        self.config = {
            "app_name": "SkipSpotifyAds",
            "start": "\u25B6 Start Ad Skip",
            "stop": "\u25A0 Stop Ad Skip",
            "stopping": "\u29D7 Stopping Ad Skip..",
            "auto_start_off": "    Auto-Start",
            "auto_start_on": "\u2713 Auto-Start",
            "about": "About SkipSpotifyAds 🎶",
            "restart": "Restart",
            "quit": "Quit"
        }
        
        self.options = {
            "auto_start": False,
        }
        
        self.app = rumps.App(self.config["app_name"])#, quit_button=None)
        self.stop_loop = rumps.Timer(self.stop_loop_iteration, 1)
        self.stop_loop.stop()
        self.stop_loop.count = 0
        
        # Initialize RSID
        self.obstruct = Obstruct()
        self.obstruct.seed = int((random.getnode()**.5+69)*420)
        self.password_prompt()
        
        # Initialize menu
        self.app.title = ''
        self.app.icon = f'{app_path}/icon_off.icns'
        
        # Read Options file (used for storing app specific options like auto start)
        if os.path.exists(f'{app_path}/.options'):
            with open(f'{app_path}/.options', 'r') as f:
                self.options = json.load(f)
        
        # load menu buttons
        self.load_menu_buttons()
        
        # Define app menu layout
        self.app.menu = [
            self.start_stop_button,
            self.auto_start_button,
            None,
            self.about_button,
            None,
            self.restart_button
            #self.quit_button
        ]
    
    # Run app alias
    def run(self):
        self.app.run()
    
    def load_menu_buttons(self):
        # Menu Buttons
        if self.options['auto_start']:
            self.start_stop_button = rumps.MenuItem(
                title=self.config["stop"],
                callback=self.start_stop_loop
            )
            self.auto_start_button = rumps.MenuItem(
                title=self.config["auto_start_on"],
                callback=self.auto_start
            )
            print("Starting SkipSpotifyAds")
            self.skip_spotify_ads.terminate = False
            self.background_thread(self.skip_spotify_ads.run, [])
            self.app.icon = f'{app_path}/icon.icns'
            
        else:
            self.start_stop_button = rumps.MenuItem(
                title=self.config["start"],
                callback=self.start_stop_loop
            )
            self.auto_start_button = rumps.MenuItem(
                title=self.config["auto_start_off"],
                callback=self.auto_start
            )
        self.about_button = rumps.MenuItem(
            title = self.config["about"],
            callback = self.open_about
        )
        self.restart_button = rumps.MenuItem(
            title = self.config["restart"],
            callback = self.restart_app
        )
        self.quit_button = rumps.MenuItem(
            title = self.config["quit"],
            callback = self.quit_app,
            key = 'q'
        )
    
    def restart_app(self, sender):
        if sender.title == self.config["restart"]:
            command = "ps -ef | grep SkipSpotifyAds"
            processes = os.popen(command).readlines()
            
            #print(processes)
            app_dir = None
            for line in processes:
                if 'SkipSpotifyAds.app' in line:
                    split_lines = line.split(' ')
                    print(split_lines)
                    app_dir = split_lines[len(split_lines)-1].replace('/Contents/MacOS/SkipSpotifyAds\n', '')
                    break
            
           # print(f'killall SkipSpotifyAds; open {app_dir}')
            if not (app_dir is None):
                os.system(f'killall SkipSpotifyAds; open {app_dir}')
            #os.system(f"python3 {app_path}/restart.py")
    
    
    def quit_app(self, sender):
        if sender.title == self.config["quit"]:
            rumps.quit_application()
    
    
    def stop_loop_iteration(self, sender):
        self.start_stop_button.title = self.config["stopping"]
        self.start_stop_button.set_callback(None)
        self.app.icon = f'{app_path}/icon_stopping.icns'
        if self.skip_spotify_ads.has_terminated:
            self.start_stop_button.title = self.config["start"]
            self.start_stop_button.set_callback(self.start_stop_loop)
            self.skip_spotify_ads.terminate = False
            self.app.icon = f'{app_path}/icon_off.icns'
            self.stop_loop.stop()
            
        sender.count += 1
    
    def start_stop_loop(self, sender):
        if sender.title == self.config["start"]:
            self.stop_loop.count = 0
            #self.notify('SkipSpotifyAds Startup', "Starting DataSync...")
            print("Starting Ad Block")
            self.skip_spotify_ads.terminate = False
            self.background_thread(self.skip_spotify_ads.run, [])
            sender.title = self.config["stop"]
            self.app.icon = f'{app_path}/icon.icns'
            self.stop_loop.stop()
        # Start the timer when stop is pressed
        elif sender.title == self.config["stop"]:
            self.notify('SkipSpotifyAds Shutdown', "Stopping Ad Skipper...")
            
            self.skip_spotify_ads.terminate = True
            self.stop_loop.start()
    
    def auto_start(self, sender):
        if sender.title == self.config["auto_start_off"]:
            self.options['auto_start'] = True
            with open(f'{app_path}/.options', 'w') as f:
                f.write(json.dumps(self.options, sort_keys=True, indent=4))
            
            
            sender.title = self.config["auto_start_on"]
        elif sender.title == self.config["auto_start_on"]:
            
            self.options['auto_start'] = False
            with open(f'{app_path}/.options', 'w') as f:
                f.write(json.dumps(self.options, sort_keys=True, indent=4))
            
            sender.title = self.config["auto_start_off"]
    
    def open_about(self, sender):
        if sender.title.lower().startswith("about"):
            
            query = """tell app "%s"\n\t\
                display dialog ¬\n\t\t\
                "\nSkipSpotifyAds was created by %s.\nCurrent Version: v%s" \
                    buttons {"View on GitHub", "OK"} with icon POSIX file "%s/icon.icns"\n\t\
                    set the button_pressed to the button returned of the result\n\tif the button_pressed is "View on GitHub" then\n\t\t\
                    open location "https://github.com/ppkantorski/SkipSpotifyAds"\n\t\
                    end if\nend tell"""
            command = f"osascript -e '{query}'"%(self.config["app_name"],__author__, __version__, app_path)
            #os.system(command)
            os.popen("sudo -S %s"%(command), 'w').write(self.obstruct.decrypt(self.password))
            #webbrowser.open('https://github.com/ppkantorski/SkipSpotifyAds')
    
    
    def notify(self, title, message):
        self.background_thread(self.notify_command, [title, message])
    
    def notify_command(self, title, message):
        title = title.replace('"', '\\"').replace("'", "'"+'"\'"'+"\'")
        message = message.replace('"', '\\"').replace("'", "'"+'"\'"'+"\'")
        app_name = self.config["app_name"].replace('"', '\\"').replace("'", "'"+'"\'"'+"\'")
        query = f'tell app "{app_name}" to display notification "{message}" with title "{title}"'
        command = f"osascript -e '{query}'"
        os.popen("sudo -S %s"%(command), 'w').write(self.obstruct.decrypt(self.password))
    
    #def notify_command(self, title, message):
    #    command =\
    #        """
    #        osascript -e 'tell app "{}" to display notification "{}" with title "{}"'
    #        """.format(
    #                self.config["app_name"].replace('"', '\\"').replace("'", "'"+'"\'"'+"\'"),
    #                message.replace('"', '\\"').replace("'", "'"+'"\'"'+"\'"), \
    #                title.replace('"', '\\"').replace("'", "'"+'"\'"'+"\'")
    #            )
    #    
    #    os.popen("sudo -S %s"%(command), 'w').write(self.obstruct.decrypt(self.password))
    
    
    def skip_spotify_ads_loop(self):
        MAX_ERRORS = 3
        #self.skip_spotify_ads.has_terminated = False
        error_count = 0
        while True:
            try:
                self.skip_spotify_ads.main()
                error_count = 0
            except Exception as e:
                print(e)
                error = "Error {0}".format(str(e.args[0])).encode("utf-8")
                self.notify('SkipSpotifyAds Error', error)
                error_count += 1
            self.has_restarted = self.skip_spotify_ads.has_restarted
            
            if error_count >= MAX_ERRORS:
                self.skip_spotify_ads.terminate = True
            
            if self.skip_spotify_ads.terminate:
                break
            
            time.sleep(5)
        
        #self.skip_spotify_ads.has_terminated = True
    
    
    
    # Prompt user for password with retry loop
    def password_prompt(self):
        try:
            self.obstruct.read()
        except:
            self.obstruct.encrypted = None
            if os.path.exists(f'{app_path}/.rsid'):
                os.remove(f'{app_path}/.rsid')
        
        if self.obstruct.encrypted is None:
            # Prompt user for password
            max_attempts = 3
            attempts = 0
            while True:
                self.get_password()
                is_valid = self.verify_password()
                
                if is_valid:
                    self.obstruct.write()
                    break
                #os.system('say "Invalid password."')
                attempts += 1
                if attempts >= max_attempts:
                    rumps.quit_application()
        else:
            self.password = self.obstruct.encrypted
    
    # Get password from user
    def get_password(self):
        permission_request = rumps.Window(
            'Enter user password',
            'Skip Spotify Ads Admin Permissions Requested',
            dimensions= (200, 20)
        )
        self.password = self.obstruct.encrypt(permission_request.run().text.strip())
    
    # Verify password is usable
    def verify_password(self):
        response = os.popen(f'dscl /Local/Default -authonly "$USER" {self.obstruct.decrypt(self.password)}').read()
        if len(response) == 0:
            return True
        else:
            return False
    
    
    ## For making object run in background
    def background_thread(self, target, args_list):
        args = ()
        for arg in args_list:
            args += (arg,)
        pr = threading.Thread(target=target, args=args)
        pr.daemon = True
        pr.start()
        return pr



# Custom cryptography
alias_1 = [126943972912743,7091320453098334569,7500641,123597941861477,125762789470061,1970628964]
alias_2 = [469786060655,6451042,418430674286,1919509355,431365777273,125762789470061]
for i in range(len(alias_1)):
    globals()\
        [(alias_2[i]).to_bytes(int(-((alias_2[i]).bit_length()/8)//1*-1),'big',signed=True).decode()]=\
        importlib.import_module((alias_1[i]).to_bytes(int(-((alias_1[i]).bit_length()/8)//1*-1),'big',signed=True).decode())

# Stay in school kids
class Obstruct(object):
    def __init__(self):
        self.seed = None
        self.encrypted = None
        self.public_key, self.private_key = alien.newkeys(212+300)
        self.int_type = 'big'
    def to_num(self, s):
        if not (self.seed is None):
            return int.from_bytes(s.encode(),self.int_type,signed=True)+self.seed
        else:
            return int.from_bytes(s.encode(),self.int_type,signed=True)
    def from_num(self, n):
        if not (self.seed is None):
            return (n-self.seed).to_bytes(int(-((n-self.seed).bit_length()/8)//1*-1),self.int_type,signed=True).decode()
        else:
            return n.to_bytes(int(-(n.bit_length()/8)//1*-1),self.int_type,signed=True).decode()
    def oshuf(self, s):
        cat = list(str(s)); doggy.shuffle(cat)
        return ''.join(cat)
    def ushuf(self, s):
        cat = [i for i in range(1,len(list(str(s)))+1)]; doggy.shuffle(cat)
        cat = list(zip(list(str(s)), cat)); cat.sort(key=lambda x: x[1])
        return ''.join([str(a) for (a, b) in cat])
    def ostr(self):
        return ''.join(doggy.choice(mango.ascii_uppercase+mango.ascii_letters+mango.digits) for i in range(24))
    def encrypt(self, s):
        doggy.seed(self.seed)
        self.encrypted = alien.encrypt(self.oshuf(str(self.to_num(s))).encode(), self.public_key).hex()
        return self.encrypted
    def decrypt(self, s):
        doggy.seed(self.seed)
        return self.from_num(int(self.ushuf(alien.decrypt(bob.unhexlify(s), self.private_key).decode())))
    def write(self):
        if not (self.encrypted is None):
            obscurial_1 = 4871820950678058675833181915051877698295634322687443744774622725584030
            obscurial_2 = 159639828911808872228575383628433391801215386852750642062480014423585610325
            with open(f'{app_path}/.rsid', 'wb') as big_poop:
                doggy.seed(self.seed)
                rick.dump({
                    self.ostr():(self.ostr()+self.ostr()+self.ostr()+self.ostr()+self.ostr()),
                    self.ostr():self.oshuf(self.private_key.save_pkcs1().decode('utf-8')\
                        .replace(self.from_num(int(int(obscurial_1+22)/4)+self.seed),self.ostr())\
                        .replace(self.from_num(int(int(obscurial_2+5)/2)+self.seed),self.ostr())),
                    self.ostr():self.oshuf(self.ostr()+'\n\n'+self.encrypted+'\n\n'+self.ostr()),
                    self.ostr():(self.ostr()+self.ostr()+self.ostr()+self.ostr()+self.ostr()+self.ostr())[doggy.randint(3, 13):]
                }, big_poop, protocol=rick.HIGHEST_PROTOCOL)
    def read(self):
        if os.path.exists(f'{app_path}/.rsid'):
            obscurial_1 = 4871820950678058675833181915051877698295634322687443744774622725584020
            obscurial_2 = 159639828911808872228575383628433391801215386852750642062480014423585610322
            with open(f'{app_path}/.rsid', 'rb') as portal:
                loaded = rick.load(portal)
                doggy.seed(self.seed);
                self.private_key = [self.ostr() for i in range(6)]
                self.private_key = loaded[self.ostr()]
                ostr_1, ostr_2 = self.ostr(), self.ostr()
                self.private_key = alien.PrivateKey.load_pkcs1(self.ushuf(self.private_key)\
                    .replace(ostr_1, self.from_num(int(int(obscurial_1+32)/4)+self.seed))\
                    .replace(ostr_2, self.from_num(int(int(obscurial_2+8)/2)+self.seed)).encode('utf-8'))
                ostr_1, ostr_2, ostr_3 = self.ostr(), self.ostr(), self.ostr()
                self.encrypted = self.ushuf(loaded[ostr_1]).replace(ostr_2+'\n\n','').replace('\n\n'+ostr_3,'')
                del loaded

if __name__ == '__main__':
    app = SkipSpotifyAdsApp()
    app.run()