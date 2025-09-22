#take windows shortcusts vdf file


#parse into python structures


#Set launch executable to winwalkawayscript




#insert entries into linux shortcuts vdf



#pull art and apply


#pull favorite & categories and apply



import os
import sys
import json

#rom lutris.util.log import logger

#from lutris.util.steam import config
#from lutris.util.steam import shortcut
#from lutris.util.steam import vdf
#from lutris.util.steam import vdfutils
#rom lutris.util.steam.config import convert_steamid64_to_steamid32, get_active_steamid64, get_user_data_dirs

#from lutris.util.steam import vdf

#linuxSteamPath = config.get_steam_dir()
#linuxSteamConfig = shortcut.get_config_path()
#linuxSteamShortcutsVDFPath = shortcut.get_shortcuts_vdf_path()

from readsc import binvdf
import vdf
import json
import bvdf
import sys


from steamfiles import appinfo

windowsSteamPath="insertWindowspathhere"

localdir = os.getcwd()
linuxShortcut= os.path.join(localdir,"linuxshortcuts.vdf")
windowsShortcut = os.path.join(localdir,"windowsshortcuts.vdf")

with open('windowsshortcuts.vdf','rb') as f:
    data = appinfo.load(f)