#!/usr/bin/env python3
"""Theme welcome sound and persistent mute control. No privileged operations."""
import fcntl
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time


def main():
    config = Path(os.environ.get('AUSTRALIANA_CONFIG_ROOT', str(Path.home() / '.config')))
    state = Path(os.environ.get('AUSTRALIANA_STATE_ROOT', str(Path.home() / '.local/state'))) / 'australiana'
    state.mkdir(parents=True, exist_ok=True)
    settings = config / 'omarchy/australiana.json'
    with (state / 'sound.lock').open('w') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        try:
            prefs = json.loads(settings.read_text())
        except (FileNotFoundError, ValueError):
            prefs = {}
        action = sys.argv[1] if len(sys.argv) > 1 else 'status'
        if action in ('mute', 'unmute', 'mute-toggle'):
            prefs['muted'] = not prefs.get('muted', False) if action == 'mute-toggle' else action == 'mute'
            settings.parent.mkdir(parents=True, exist_ok=True)
            temporary = settings.with_suffix('.tmp')
            temporary.write_text(json.dumps(prefs, indent=2) + '\n')
            temporary.replace(settings)
            print('Kookaburra muted' if prefs['muted'] else 'Kookaburra unmuted')
            return
        if action == 'status':
            print('muted' if prefs.get('muted') else 'unmuted')
            return
        if action != 'theme' or len(sys.argv) != 3:
            raise SystemExit('Usage: australiana.py status|mute|unmute|mute-toggle|theme <name>')
        name = sys.argv[2]
        previous_path = state / 'sound-theme'
        previous = previous_path.read_text().strip() if previous_path.exists() else ''
        previous_path.write_text(name + '\n')
        # Refreshing the current theme is silent; only entering Australiana plays.
        if name != 'australiana' or previous == name or prefs.get('muted', False):
            return
        last_path = state / 'sound-last-played'
        try:
            last = float(last_path.read_text())
        except (FileNotFoundError, ValueError):
            last = 0
        if time.time() - last < 60:
            return
        player = shutil.which('pw-play')
        clip = config / 'omarchy/themes/australiana/extras/sounds/kookaburra.wav'
        if player and clip.is_file():
            subprocess.Popen([player, '--volume=0.35', str(clip)], stdout=subprocess.DEVNULL,
                             stderr=subprocess.DEVNULL, start_new_session=True)
            last_path.write_text(str(time.time()))


if __name__ == '__main__':
    main()
