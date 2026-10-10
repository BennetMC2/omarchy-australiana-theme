#!/usr/bin/env python3
"""Install user-owned theme extras without changing the packaged shell."""
import getpass
import json
import os
from pathlib import Path
import shutil
import subprocess

theme = Path(__file__).resolve().parent.parent
os.environ.setdefault('OMARCHY_SHELL_IPC_TIMEOUT', '15s')
config = Path.home() / '.config/omarchy'
plugin = config / 'plugins/australiana.roo'
plugin.mkdir(parents=True, exist_ok=True)
for source in (theme / 'extras/roo').iterdir():
    if source.is_file():
        shutil.copy2(source, plugin / source.name)
subprocess.run(['omarchy', 'plugin', 'validate', str(plugin)], check=True)

# Clone the locally installed lock version; don't ship an ageing PAM service.
clone_id = getpass.getuser() + '.lock'
clone = config / 'plugins' / clone_id
if not clone.exists():
    subprocess.run(['omarchy', 'plugin', 'clone', 'omarchy.lock'], check=True)
manifest = json.loads((clone / 'manifest.json').read_text())
if manifest.get('omarchy', {}).get('clonedFrom') != 'omarchy.lock':
    raise SystemExit('Existing lock plugin is not an Omarchy clone; left unchanged.')
view = clone / 'LockView.qml'
text = view.read_text()
marker = '    // Australiana decoration (authentication remains upstream).'
anchor = '    BorderSurface {\n      id: inputField'
if marker not in text:
    if text.count(anchor) != 1:
        raise SystemExit('Lock view structure changed; refusing to patch it automatically.')
    shutil.copy2(view, clone / 'LockView.qml.before-australiana')
    addition = marker + '\n    AustralianaDecoration { anchors.fill: parent }\n\n'
    text = text.replace(anchor, addition + anchor)
shutil.copy2(theme / 'extras/AustralianaDecoration.qml', clone / 'AustralianaDecoration.qml')
shutil.copy2(theme / 'extras/roo/roo.svg', clone / 'australiana-roo.svg')
view.write_text(text)
subprocess.run(['omarchy', 'plugin', 'validate', str(clone)], check=True)

preferences = config / 'australiana.json'
if not preferences.exists():
    preferences.write_text('{"muted": false}\n')
subprocess.run(['omarchy', 'hook', 'install', 'theme-set', str(theme / 'extras/australiana-extras')], check=True)
subprocess.run(['omarchy-shell', 'shell', 'rescanPlugins'], check=True)
subprocess.run(['omarchy', 'plugin', 'enable', clone_id], check=True)
subprocess.run(['omarchy', 'plugin', 'enable', 'australiana.roo', '--after', 'omarchy.menu'], check=True)
