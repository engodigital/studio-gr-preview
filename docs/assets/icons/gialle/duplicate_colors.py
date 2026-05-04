#!/usr/bin/env python3
import os
import re
from pathlib import Path

BLUE = "#02519e"
WHITE = "#FFFFFF"

# Colori comuni trovati nelle SVG (background, icon, details)
COLOR_MAP = {
    # Marroni (background attuali)
    "#2C1F00": (WHITE, BLUE),      # main bg
    "#1A1200": (WHITE, BLUE),      # dark bg
    # Ori (icon attuali)
    "#FFD700": (BLUE, WHITE),      # gold icon
    "#B8860B": (BLUE, WHITE),      # dark gold
    # Blu (se presente)
    "#0066cc": (WHITE, BLUE),
    "#003366": (WHITE, BLUE),
}

def swap_colors(svg_content, is_white_blue=True):
    """Sostituisce i colori: white_blue = sfondo bianco + icona blu"""
    result = svg_content

    if is_white_blue:
        # sfondo bianco, icona blu
        replacements = {
            "#2C1F00": WHITE,     # marrone -> bianco
            "#1A1200": WHITE,     # dark -> bianco (per dettagli, resta bianco)
            "#FFD700": BLUE,      # oro -> blu
            "#B8860B": BLUE,      # dark gold -> blu
        }
    else:
        # sfondo blu, icona bianco
        replacements = {
            "#2C1F00": BLUE,      # marrone -> blu
            "#1A1200": BLUE,      # dark -> blu (per dettagli, resta blu)
            "#FFD700": WHITE,     # oro -> bianco
            "#B8860B": WHITE,     # dark gold -> bianco
        }

    for old, new in replacements.items():
        result = result.replace(old, new)

    return result

def process_svg(svg_path, output_dir):
    """Legge un SVG e crea due versioni con colori invertiti"""
    with open(svg_path, 'r', encoding='utf-8') as f:
        content = f.read()

    filename = Path(svg_path).stem

    # Versione white_blue
    white_blue = swap_colors(content, is_white_blue=True)
    white_blue_path = os.path.join(output_dir, f"{filename}_white_blue.svg")
    with open(white_blue_path, 'w', encoding='utf-8') as f:
        f.write(white_blue)
    print(f"✓ Created: {white_blue_path}")

    # Versione blue_white
    blue_white = swap_colors(content, is_white_blue=False)
    blue_white_path = os.path.join(output_dir, f"{filename}_blue_white.svg")
    with open(blue_white_path, 'w', encoding='utf-8') as f:
        f.write(blue_white)
    print(f"✓ Created: {blue_white_path}")

# Cartelle da processare
base_dir = "/Users/marcomarengo/Documents/agency-clients/Promozione Facile/Studio_GR/assets/icons"
folders = [
    base_dir,
    os.path.join(base_dir, "icons-GHL"),
    os.path.join(base_dir, "raw"),
]

for folder in folders:
    print(f"\n📁 Processing: {folder}")
    if not os.path.exists(folder):
        print(f"  ⚠️  Folder not found")
        continue

    svg_files = [f for f in os.listdir(folder) if f.endswith('.svg')]
    if not svg_files:
        print(f"  No SVG files found")
        continue

    for svg_file in sorted(svg_files):
        svg_path = os.path.join(folder, svg_file)
        try:
            process_svg(svg_path, folder)
        except Exception as e:
            print(f"✗ Error processing {svg_file}: {e}")

print("\n✅ Done!")
