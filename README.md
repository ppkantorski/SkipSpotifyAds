# Skip Spotify Ads (macOS)

This script will restart Spotify whenever ads come up.

1. Dependencies
```
pip3 install SwSpotify
pip3 uninstall werkzeug
pip3 install werkzeug==2.0.3
```

2. Deploy using the .zsh script.  You will need to modify the path to the .py within the .zsh script.
3. To view the running script on Screen GNU, run the following command:
```
screen -r skip_spotify_ads
```
To detach, run:
```CTRL+A, CTRL+D```
