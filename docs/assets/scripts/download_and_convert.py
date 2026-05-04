#!/usr/bin/env python3
import re
from pathlib import Path

# URLs degli SVG da scaricare
urls = [
    ("https://assets.cdn.filesafe.space/Vlybbph2lwD1CXos345s/media/69e13b4d2c135a8c839f2c9a.svg", "music"),
    ("https://assets.cdn.filesafe.space/Vlybbph2lwD1CXos345s/media/69e13b4dbde9ef25bd1154b4.svg", "weights"),
    ("https://assets.cdn.filesafe.space/Vlybbph2lwD1CXos345s/media/69e13b4d0b562c728128f826.svg", "phone-shake"),
    ("https://assets.cdn.filesafe.space/Vlybbph2lwD1CXos345s/media/69e13b4d0b562c728128f828.svg", "thumbs-up"),
    ("https://assets.cdn.filesafe.space/Vlybbph2lwD1CXos345s/media/69e13b4dc56ad279082cb6a2.svg", "bubbles"),
    ("https://assets.cdn.filesafe.space/Vlybbph2lwD1CXos345s/media/69e13b4d8696a78b8d6a1c52.svg", "chart"),
    ("https://assets.cdn.filesafe.space/Vlybbph2lwD1CXos345s/media/69e13b4dbde9ef25bd1154b5.svg", "clipboard"),
    ("https://assets.cdn.filesafe.space/Vlybbph2lwD1CXos345s/media/69e13b4d50b9a3263a5d75fe.svg", "users-settings"),
    ("https://assets.cdn.filesafe.space/Vlybbph2lwD1CXos345s/media/69e89789a1636a6c651e017d.svg", "book"),
    ("https://assets.cdn.filesafe.space/Vlybbph2lwD1CXos345s/media/69e89789a48992f6898a1fee.svg", "person"),
    ("https://assets.cdn.filesafe.space/Vlybbph2lwD1CXos345s/media/69e89789717d5dd4e1fab239.svg", "download"),
    ("https://assets.cdn.filesafe.space/Vlybbph2lwD1CXos345s/media/69e89789a1636a6c651e017f.svg", "location"),
    ("https://assets.cdn.filesafe.space/Vlybbph2lwD1CXos345s/media/69e89e3b717d5dd4e1fc4f94.svg", "clock"),
]

import urllib.request

icons_dir = Path("/Users/marcomarengo/Documents/agency-clients/Promozione Facile/Studio_GR/assets/icons")
blu_dir = icons_dir / "blu"
bianche_dir = icons_dir / "bianche"

for url, name in urls:
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
        
        # Estrai il path
        path_match = re.search(r'<path\s+d="([^"]+)"', content)
        if not path_match:
            print(f"❌ {name}: nessun path trovato")
            continue
        
        icon_path = path_match.group(1)
        
        # Versione BLU
        blu_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200">
  <rect width="200" height="200" rx="24" fill="#02519e"/>
  <rect width="200" height="200" rx="24" fill="#FFFFFF" fill-opacity="0.08"/>
  <g transform="translate(40.0000, 40.0000) scale(0.234375)" fill="#FFFFFF">
    <path d="{icon_path}"/>
  </g>
</svg>'''
        
        # Versione BIANCHE
        bianche_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200">
  <rect width="200" height="200" rx="24" fill="#FFFFFF"/>
  <rect width="200" height="200" rx="24" fill="#02519e" fill-opacity="0.08"/>
  <g transform="translate(40.0000, 40.0000) scale(0.234375)" fill="#02519e">
    <path d="{icon_path}"/>
  </g>
</svg>'''
        
        with open(blu_dir / f"{name}.svg", 'w') as f:
            f.write(blu_svg)
        with open(bianche_dir / f"{name}.svg", 'w') as f:
            f.write(bianche_svg)
        
        print(f"✓ {name}")
    except Exception as e:
        print(f"❌ {name}: {e}")

print("\nDone!")
