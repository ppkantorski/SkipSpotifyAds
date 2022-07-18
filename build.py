import os
import shutil

# Install module if not already installed
import importlib
def install(package):
    try:
        importlib.import_module(package)
    except ImportError:
        os.system(f"pip3 install {package}")

# Import / Install
packages = ['SwSpotify']
[install(pkg) for pkg in packages]

# Uninstall broken package (part of SwSpotify) then install older version
os.system("pip3 uninstall werkzeug")
os.system("pip3 install werkzeug==2.0.3")

# Define script path
script_path = os.path.dirname(os.path.abspath( __file__ ))

# Run setup script
os.system(f'python3 {script_path}/setup.py py2app -A')

# Clean up directories
shutil.rmtree(f'{script_path}/build')
os.system(f'mv {script_path}/dist/SkipSpotifyAds.app {script_path}/SkipSpotifyAds.app')
shutil.rmtree(f'{script_path}/dist')
