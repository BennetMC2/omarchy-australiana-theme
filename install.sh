#!/bin/bash
set -euo pipefail
theme_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
expected_dir="$HOME/.config/omarchy/themes/australiana"
if [[ "$theme_dir" != "$expected_dir" ]]; then
  echo "Place this repository at $expected_dir, then run bash install.sh." >&2
  exit 1
fi
command -v python3 >/dev/null
omarchy hook install theme-set "$theme_dir/branding/australiana-about"
omarchy theme set australiana
