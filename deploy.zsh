SCRIPTPATH=${0:A}
SCRIPTPATH="${SCRIPTPATH//deploy.zsh}"
screen -dmS skip_spotify_ads python3 "${SCRIPTPATH}skip_spotify_ads.py"
