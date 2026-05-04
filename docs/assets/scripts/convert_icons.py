#!/usr/bin/env python3
import os
import re
from pathlib import Path

icons_dir = Path("/Users/marcomarengo/Documents/agency-clients/Promozione Facile/Studio_GR/assets/icons")
source_dir = icons_dir
blu_dir = icons_dir / "blu"
bianche_dir = icons_dir / "bianche"

# Colori per ogni formato
formats = {
    "blu": {"bg": "#02519e", "icon": "#FFFFFF"},
    "bianche": {"bg": "#FFFFFF", "icon": "#02519e"}
}

# Lettura SVG dalla cartella icons
svg_files = [f for f in source_dir.glob("icon-*.svg")]

for svg_file in svg_files:
    with open(svg_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Estrai il path (la parte che contiene la vera icona)
    path_match = re.search(r'<path\s+d="([^"]+)"', content)

    if not path_match:
        print(f"Avvertenza: nessun path trovato in {svg_file.name}")
        continue

    icon_path = path_match.group(1)
    base_name = svg_file.stem.replace("icon-", "")

    # Crea versione BLU
    blu_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200">
  <rect width="200" height="200" rx="24" fill="{formats['blu']['bg']}"/>
  <rect width="200" height="200" rx="24" fill="{formats['blu']['icon']}" fill-opacity="0.08"/>
  <g transform="translate(40.0000, 40.0000) scale(0.234375)" fill="{formats['blu']['icon']}">
    <path d="{icon_path}"/>
  </g>
</svg>'''

    # Crea versione BIANCHE
    bianche_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200">
  <rect width="200" height="200" rx="24" fill="{formats['bianche']['bg']}"/>
  <rect width="200" height="200" rx="24" fill="{formats['bianche']['icon']}" fill-opacity="0.08"/>
  <g transform="translate(40.0000, 40.0000) scale(0.234375)" fill="{formats['bianche']['icon']}">
    <path d="{icon_path}"/>
  </g>
</svg>'''

    # Salva nei rispettivi formati
    blu_file = blu_dir / f"{base_name}.svg"
    bianche_file = bianche_dir / f"{base_name}.svg"

    with open(blu_file, 'w', encoding='utf-8') as f:
        f.write(blu_svg)
    print(f"✓ Creato {blu_file.name}")

    with open(bianche_file, 'w', encoding='utf-8') as f:
        f.write(bianche_svg)
    print(f"✓ Creato {bianche_file.name}")

print("\nConversione completata!")
