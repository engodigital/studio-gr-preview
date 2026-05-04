#!/usr/bin/env python3
import os
from pathlib import Path

BLUE = "#02519e"
WHITE = "#FFFFFF"
DUPLICATI_DIR = "/Users/marcomarengo/Documents/agency-clients/Promozione Facile/Studio_GR/assets/icons/duplicati"

def swap_colors(svg_content, is_white_blue=True):
    """Sostituisce i colori: white_blue = sfondo bianco + icona blu"""
    result = svg_content

    if is_white_blue:
        # sfondo bianco, icona blu
        replacements = {
            "#2C1F00": WHITE,      # bg marrone -> bianco
            "#1A1200": WHITE,      # bg dark -> bianco
            "#FFD700": BLUE,       # icona oro -> blu
            "#B8860B": BLUE,       # icona oro dark -> blu
            "#C8960C": BLUE,       # variante oro -> blu
            "#181818": WHITE,      # bg scuro -> bianco
            "#FBC21D": BLUE,       # icona giallo -> blu
        }
    else:
        # sfondo blu, icona bianco
        replacements = {
            "#2C1F00": BLUE,       # bg marrone -> blu
            "#1A1200": BLUE,       # bg dark -> blu
            "#FFD700": WHITE,      # icona oro -> bianco
            "#B8860B": WHITE,      # icona oro dark -> bianco
            "#C8960C": WHITE,      # variante oro -> bianco
            "#181818": BLUE,       # bg scuro -> blu
            "#FBC21D": WHITE,      # icona giallo -> bianco
        }

    for old, new in replacements.items():
        result = result.replace(old, new)

    return result

def process_svg(svg_path):
    """Legge un SVG e crea due versioni con colori invertiti"""
    with open(svg_path, 'r', encoding='utf-8') as f:
        content = f.read()

    filename = Path(svg_path).stem

    # Versione white_blue
    white_blue = swap_colors(content, is_white_blue=True)
    white_blue_path = os.path.join(DUPLICATI_DIR, f"{filename}_white_blue.svg")
    with open(white_blue_path, 'w', encoding='utf-8') as f:
        f.write(white_blue)
    print(f"✓ {filename}_white_blue.svg")

    # Versione blue_white
    blue_white = swap_colors(content, is_white_blue=False)
    blue_white_path = os.path.join(DUPLICATI_DIR, f"{filename}_blue_white.svg")
    with open(blue_white_path, 'w', encoding='utf-8') as f:
        f.write(blue_white)
    print(f"✓ {filename}_blue_white.svg")

# Cartelle da processare
base_dir = "/Users/marcomarengo/Documents/agency-clients/Promozione Facile/Studio_GR/assets/icons"
folders = [
    base_dir,
    os.path.join(base_dir, "icons-GHL"),
    os.path.join(base_dir, "raw"),
]

total_count = 0
for folder in folders:
    if not os.path.exists(folder):
        continue

    svg_files = sorted([f for f in os.listdir(folder) if f.endswith('.svg')])
    if not svg_files:
        continue

    for svg_file in svg_files:
        svg_path = os.path.join(folder, svg_file)
        try:
            process_svg(svg_path)
            total_count += 1
        except Exception as e:
            print(f"✗ Errore: {svg_file} - {e}")

print(f"\n✅ Completato! {total_count} SVG elaborati ({total_count*2} file totali)")
