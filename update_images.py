import os
import re

# Dictionary mappings based on your actual file locations
# All paths are relative to game/images
IMAGE_FOLDERS = {
    "bureau.png": "gui/bureau.png",
    "Parvis-portail-Sud.png": "scenes/Parvis-portail-Sud.png",
    "Portail-nord.png": "scenes/Portail-nord.png",
    "Est-Chevet.png": "scenes/Est-Chevet.png",
    "Portail-Ouest-BasseOeuvre.png": "scenes/Portail-Ouest-BasseOeuvre.png",
    "kiosque.png": "scenes/kiosque.png",
    "carolingienne.png": "scenes/carolingienne.png",
    "artfrancais.png": "scenes/artfrancais.png",
    "rosace.png": "scenes/rosace.png",
    "horloge.png": "scenes/horloge.png",
    "horloge-astronomique.png": "scenes/horloge-astronomique.png",
    "horloge-astronomique-ouvert.png": "scenes/horloge-astronomique-ouvert.png",
    "orgues.png": "scenes/orgues.png",
    "click1.png": "gui/click1.png",
    "click2.png": "gui/click2.png",
    "cloitre_faille.webm": "scenes/cloitre_faille.webm",
    "coffre-mini.png": "items/coffre-mini.png",
    "cryptex-mini.png": "items/cryptex-mini.png",
    "cloitre.png": "scenes/cloitre.png",
    "lunettes.png": "items/lunettes.png",
    "cryptex.png": "items/cryptex.png",
    "coffre-taille-normale.png": "items/coffre-taille-normale.png",
    "coffre-mini-up.png": "items/coffre-mini-UP.png",
    "parchemin.png": "items/parchemin.png",
    "parchemin-up.png": "items/parchemin-up.png",
    "parchemin1.png": "items/parchemin1.png",
    "open_image.png": "gui/open_image.png",
    "open_image_hover.png": "gui/open_image_hover.png",
    "backpack.png": "gui/backpack.png",
    "backpack-hover.png": "gui/backpack-hover.png",
    "inventory_bg.png": "gui/inventory_bg.png",
    "minimap.png": "gui/minimap.png",
    "minimap-hover.png": "gui/minimap-hover.png",
    "plan_cathedrale_grand_fond.png": "items/plan_cathedrale_grand_fond.png",
    "cryptex-mini-hover.png": "items/cryptex-mini-hover.png",
    "safebox/": "safe_i/"
}

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    for img, path in IMAGE_FOLDERS.items():
        # Match 'images/IMG' or "images/IMG" exactly to prevent double replacement
        # \1 captures the quote type
        content = re.sub(r'([\'"])images/' + re.escape(img) + r'\1', r'\g<1>images/' + path + r'\g<1>', content)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

for root, _, files in os.walk('game'):
    for file in files:
        if file.endswith('.rpy'):
            update_file(os.path.join(root, file))

print("Done")