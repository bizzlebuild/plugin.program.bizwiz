# -*- coding: utf-8 -*-
import os
import xbmcaddon

ADDON_ID = xbmcaddon.Addon().getAddonInfo('id')
PATH = xbmcaddon.Addon().getAddonInfo('path')
ART = os.path.join(PATH, 'resources', 'media')

ADDONTITLE = 'Bizzle Wizard'
BUILDERNAME = 'bizzlebuild'
EXCLUDES = [ADDON_ID, 'repository.bizzlebuild']
BUILDFILE = 'https://raw.githubusercontent.com/bizzlebuild/plugin.program.bizwiz/main/builds.txt'
UPDATECHECK = 0
APKFILE = 'http://'
YOUTUBETITLE = ''
YOUTUBEFILE = 'http://'
ADDONFILE = 'http://'
ADVANCEDFILE = 'http://'

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

HIDESPACERS = 'No'
SPACER = '='
COLOR1 = 'skyblue'
COLOR2 = 'white'
THEME1 = '[COLOR {color1}]{{}}[/COLOR]'.format(color1=COLOR1, color2=COLOR2)
THEME2 = '[COLOR {color1}][B]{{}}[/B][/COLOR]'.format(color1=COLOR1, color2=COLOR2)
THEME3 = '[COLOR {color2}]{{}}[/COLOR]'.format(color1=COLOR1, color2=COLOR2)
THEME4 = '[COLOR {color1}]Current Build:[/COLOR] [COLOR {color2}]{{}}[/COLOR]'.format(color1=COLOR1, color2=COLOR2)
THEME5 = '[COLOR {color1}]Current Theme:[/COLOR] [COLOR {color2}]{{}}[/COLOR]'.format(color1=COLOR1, color2=COLOR2)

HIDECONTACT = 'No'
CONTACT = 'Thank you for choosing Bizzle Wizard.\n\nGitHub: https://github.com/bizzlebuild/plugin.program.bizwiz'
CONTACTICON = ICONCONTACT
CONTACTFANART = 'http://'

AUTOUPDATE = 'No'
AUTOINSTALL = 'No'
REPOID = 'repository.bizzlebuild'
REPOADDONXML = 'http://'
REPOZIPURL = 'http://'

ENABLE = 'No'
NOTIFICATION = 'http://'
HEADERTYPE = 'Text'
FONTHEADER = 'font13'
HEADERMESSAGE = 'Bizzle Wizard'
HEADERIMAGE = 'http://'
FONTSETTINGS = 'font12'
BACKGROUND = ''
