from distutils.core import setup
APP = ['app/skip_spotify_ads_app.py']
DATA_FILES = ['app/skip_spotify_ads.py']
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'app/icon.icns',
    'plist': {
        'CFBundleShortVersionString': '0.2.0',
        'LSUIElement': True,
    },
    'packages': [],
}
setup(
    app=APP,
    name='SkipSpotifyAds',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    install_requires=['SwSpotify']
)