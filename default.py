# -*- coding: utf-8 -*-
import os
import re
import sys
import zipfile
from urllib.parse import parse_qsl, urlencode
from urllib.request import urlopen, Request

import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin
import xbmcvfs

try:
    import uservar
except Exception:
    uservar = None

ADDON = xbmcaddon.Addon()
ADDON_ID = ADDON.getAddonInfo('id')
ADDON_NAME = ADDON.getAddonInfo('name')
HANDLE = int(sys.argv[1])
BASE_URL = sys.argv[0]
BUILD_FILE = getattr(uservar, 'BUILDFILE', 'https://raw.githubusercontent.com/bizzlebuild/plugin.program.bizwiz/main/builds.txt')


def build_url(query):
    return BASE_URL + '?' + urlencode(query)


def notify(title, message):
    xbmcgui.Dialog().notification(title, message, ADDON.getAddonInfo('icon'), 5000)


def fetch_text(url):
    req = Request(url, headers={'User-Agent': 'Kodi Bizzle Wizard'})
    with urlopen(req, timeout=20) as response:
        return response.read().decode('utf-8', errors='ignore')


def parse_builds(text):
    builds = []
    current = {}
    for line in text.splitlines():
        line = line.strip()
        if not line:
            if current:
                builds.append(current)
                current = {}
            continue
        match = re.match(r'([A-Za-z0-9_]+)="(.*)"$', line)
        if match:
            key, value = match.groups()
            if key == 'name' and current:
                builds.append(current)
                current = {}
            current[key.lower()] = value
    if current:
        builds.append(current)
    return builds


def list_builds():
    try:
        text = fetch_text(BUILD_FILE)
        builds = parse_builds(text)
    except Exception as exc:
        xbmcgui.Dialog().ok(ADDON_NAME, 'Could not read builds.txt:\n{0}'.format(exc))
        return

    if not builds:
        xbmcgui.Dialog().ok(ADDON_NAME, 'No builds found in builds.txt')
        return

    for build in builds:
        name = build.get('name', 'Unnamed Build')
        version = build.get('version', '')
        label = '{0} {1}'.format(name, version).strip()
        item = xbmcgui.ListItem(label=label)
        item.setArt({
            'icon': build.get('icon', ADDON.getAddonInfo('icon')),
            'fanart': build.get('fanart', ADDON.getAddonInfo('fanart')),
        })
        item.setInfo('video', {'title': label, 'plot': build.get('description', '')})
        url = build_url({'mode': 'install', 'name': name, 'url': build.get('url', '')})
        xbmcplugin.addDirectoryItem(HANDLE, url, item, False)

    xbmcplugin.endOfDirectory(HANDLE)


def download_file(url, destination):
    req = Request(url, headers={'User-Agent': 'Kodi Bizzle Wizard'})
    with urlopen(req, timeout=30) as response, open(destination, 'wb') as output:
        total = int(response.headers.get('content-length') or 0)
        downloaded = 0
        dialog = xbmcgui.DialogProgress()
        dialog.create(ADDON_NAME, 'Downloading build...')
        while True:
            chunk = response.read(1024 * 256)
            if not chunk:
                break
            output.write(chunk)
            downloaded += len(chunk)
            if total:
                percent = int(downloaded * 100 / total)
                dialog.update(percent, 'Downloading build...')
            if dialog.iscanceled():
                dialog.close()
                raise Exception('Download cancelled')
        dialog.close()


def safe_extract(zip_path, target_dir):
    dialog = xbmcgui.DialogProgress()
    dialog.create(ADDON_NAME, 'Extracting build...')
    with zipfile.ZipFile(zip_path, 'r') as archive:
        members = archive.infolist()
        total = len(members) or 1
        for index, member in enumerate(members):
            name = member.filename.replace('\\', '/')
            if name.startswith('/') or '..' in name.split('/'):
                continue
            archive.extract(member, target_dir)
            dialog.update(int((index + 1) * 100 / total), 'Extracting build...')
            if dialog.iscanceled():
                dialog.close()
                raise Exception('Extract cancelled')
    dialog.close()


def install_build(name, url):
    if not url or url == 'http://':
        xbmcgui.Dialog().ok(ADDON_NAME, 'No valid ZIP URL set for this build.')
        return

    yes = xbmcgui.Dialog().yesno(
        ADDON_NAME,
        'Install {0}?\n\nThis will extract the build into your Kodi home folder. Backup first if needed.'.format(name),
        nolabel='Cancel',
        yeslabel='Install'
    )
    if not yes:
        return

    packages = xbmcvfs.translatePath('special://home/addons/packages/')
    home = xbmcvfs.translatePath('special://home/')
    os.makedirs(packages, exist_ok=True)
    zip_path = os.path.join(packages, '{0}.zip'.format(re.sub(r'[^A-Za-z0-9_.-]+', '_', name)))

    try:
        download_file(url, zip_path)
        safe_extract(zip_path, home)
        xbmcgui.Dialog().ok(ADDON_NAME, 'Build installed. Force close Kodi, then reopen it.')
    except Exception as exc:
        xbmcgui.Dialog().ok(ADDON_NAME, 'Install failed:\n{0}'.format(exc))


def main():
    params = dict(parse_qsl(sys.argv[2][1:])) if len(sys.argv) > 2 else {}
    mode = params.get('mode', '')
    if mode == 'install':
        install_build(params.get('name', 'Build'), params.get('url', ''))
    else:
        list_builds()


if __name__ == '__main__':
    main()
