# SkipSpotifyAds (macOS)
This program will restart Spotify whenever ads come up for seamless streaming as well as log the songs that you listen to.

![alt-text](https://i.imgur.com/C4AV4G6.png)

![alt-text](https://i.imgur.com/oJa7rlG.png)

1. Extract the repository to `/Users/{user_name}/Documents/SkipSpotifyAds/`.
2. Run `build.py` to install the necessary dependencies and build `SkipSpotifyAds.app`.
3. You can mow move the application into your Applications folder, but keep the repository within the folder you installed it to.


### Python Script (still used, but now witin the app)
![alt-text](https://i.imgur.com/YFOjnpl.png)

1. Dependencies
```
pip3 install SwSpotify
pip3 uninstall werkzeug
pip3 install werkzeug==2.0.3
```

2. Deploy using the .zsh script.  You will need to keep both the .py and .zsh script within the same directory.
3. To view the running script on Screen GNU, run the following command:
```
screen -r skip_spotify_ads
```
To detach, press:
```CTRL+A, CTRL+D```
