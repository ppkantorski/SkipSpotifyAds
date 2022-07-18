# Skip Spotify Ads (macOS)

![alt-text](https://i.imgur.com/YFOjnpl.png)

This script will restart Spotify whenever ads come up for seamless streaming as well as log the songs that you listen to.

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
