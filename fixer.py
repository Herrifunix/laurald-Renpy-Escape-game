import os
import subprocess
import shutil

filepath = "game/core/screens.rpy"

# Recover original from git
subprocess.run(['git', 'checkout', 'HEAD', '--', 'game/screens.rpy'])
shutil.copyfile('game/screens.rpy', filepath)

# Then apply the edits safely in Python!
with open(filepath, "r", encoding="utf-8") as f:
    text = f.read()

# Only two specific fixes.
# 1. Selected inventory screen selection text fixing
text = text.replace("S\u00e9lectionnez un objet pour voir les d\u00e9tails.", "Sélectionnez un objet pour voir les détails.")

# 2. Append the missing image_viewer_screen to the bottom of the file
if "screen image_viewer_screen" not in text:
    text += """

screen image_viewer_screen(img):
    modal True
    zorder 100
    
    add "#000000cc" # Fond sombre semi-transparent
    
    add img xalign 0.5 yalign 0.5
    
    textbutton "Fermer" action Hide("image_viewer_screen") xalign 0.5 yalign 0.9 text_size 40
"""

with open(filepath, "w", encoding="utf-8") as f:
    f.write(text)

print("Screens fixed successfully!")
