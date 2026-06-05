import os
import xbmcaddon

#########################################################
# Global Variables - DON'T EDIT
#########################################################

ADDON_ID = xbmcaddon.Addon().getAddonInfo('id')
PATH = xbmcaddon.Addon().getAddonInfo('path')
ART = os.path.join(PATH, 'resources', 'media')

#########################################################
# Bizzle Wizard Settings
#########################################################

ADDONTITLE = '[COLOR skyblue][B]Bizzle[/B][/COLOR] Wizard'
BUILDERNAME = 'bizzlebuild'
EXCLUDES = [ADDON_ID, 'repository.bizzlebuild']

# Your build list
BUILDFILE = 'https://raw.githubusercontent.com/bizzlebuild/plugin.program.bizwiz/main/builds.txt'

# Check every Kodi startup
UPDATECHECK = 0

# Optional extra lists
APKFILE = 'http://'
YOUTUBETITLE = ''
YOUTUBEFILE = 'http://'
ADDONFILE = 'http://'
ADVANCEDFILE = 'http://'

#########################################################
# Icons
#########################################################

ICONBUILDS = os.path.join(ART, 'builds.png')
ICONMAINT = os.path.join(ART, 'maintenance.png')
ICONSPEED = os.path.join(ART, 'speed.png')
ICONAPK = os.path.join(ART, 'apkinstaller.png')
ICONADDONS = os.path.join(ART, 'addoninstaller.png')
ICONYOUTUBE = os.path.join(ART, 'youtube.png')
ICONSAVE = os.path.join(ART, 'savedata.png')
ICONTRAKT = os.path.join(ART, 'keeptrakt.png')
ICONREAL = os.path.join(ART, 'keepdebrid.png')
ICONLOGIN = os.path.join(ART, 'keeplogin.png')
ICONCONTACT = os.path.join(ART, 'information.png')
ICONSETTINGS = os.path.join(ART, 'settings.png')

#########################################################
# Theme
#########################################################

HIDESPACERS = 'No'
SPACER = '='
COLOR1 = 'skyblue'
COLOR2 = 'white'

THEME1 = u'[COLOR {color1}][B]Bizzle[/B][/COLOR] [COLOR {color2}]Wizard[/COLOR] - [COLOR {color1}]{{}}[/COLOR]'.format(color1=COLOR1, color2=COLOR2)
THEME2 = u'[COLOR {color1}]{{}}[/COLOR]'.format(color1=COLOR1)
THEME3 = u'[COLOR {color2}]{{}}[/COLOR]'.format(color2=COLOR2)
THEME4 = u'[COLOR {color1}]Current Build:[/COLOR] [COLOR {color2}]{{}}[/COLOR]'.format(color1=COLOR1, color2=COLOR2)
THEME5 = u'[COLOR {color1}]Current Theme:[/COLOR] [COLOR {color2}]{{}}[/COLOR]'.format(color1=COLOR1, color2=COLOR2)

#########################################################
# Contact
#########################################################

HIDECONTACT = 'No'
CONTACT = 'Thank you for choosing Bizzle Wizard.\n\nGitHub: https://github.com/bizzlebuild/plugin.program.bizwiz'
CONTACTICON = 'icon.png'
CONTACTFANART = 'fanart.jpg'

#########################################################
# Auto Update / Repo
#########################################################

AUTOUPDATE = 'Yes'
AUTOINSTALL = 'Yes'
REPOID = 'repository.bizzlebuild'
REPOADDONXML = 'https://raw.githubusercontent.com/bizzlebuild/repository.bizzlebuild/master/repo/repository.bizzlebuild/addon.xml'
REPOZIPURL = 'https://raw.githubusercontent.com/bizzlebuild/repository.bizzlebuild/master/repo/zips'

#########################################################
# Notification Window
#########################################################

ENABLE = 'Yes'
NOTIFICATION = 'http://'
HEADERTYPE = 'Text'
FONTHEADER = 'Font14'
HEADERMESSAGE = '[COLOR skyblue][B]Bizzle[/B][/COLOR] Wizard'
HEADERIMAGE = 'http://'
FONTSETTINGS = 'Font13'
BACKGROUND = 'fanart.jpg'
