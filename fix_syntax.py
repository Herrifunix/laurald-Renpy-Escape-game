import re

with open('game/core/screens.rpy', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix broken syntax from earlier commits
text = text.replace('£', '#')
text = text.replace('i"', '["')
text = text.replace('"|', '"]')
text = text.replace('inventaire_itemsii|', 'inventaire_items[i]')
text = text.replace('action i', 'action [')
text = text.replace('Show("inventory_screen")|', 'Show("inventory_screen")]')
text = text.replace('Show("crafting_selection_screen")|', 'Show("crafting_selection_screen")]')
text = text.replace('Show("debug_map_locations")|', 'Show("debug_map_locations")]')
text = text.replace('ShowMenu("debug_minigames")|', 'ShowMenu("debug_minigames")]')
text = text.replace('Show("plan_screen")|', 'Show("plan_screen")]')

# Re-append image_viewer_screen if it's missing
if 'screen image_viewer_screen' not in text:
    text += '''\nscreen image_viewer_screen(img):
    modal True
    zorder 100
    
    add "#000000cc" # Fond sombre semi-transparent
    
    add img xalign 0.5 yalign 0.5
    
    textbutton "Fermer" action Hide("image_viewer_screen") xalign 0.5 yalign 0.9 text_size 40
'''

with open('game/core/screens.rpy', 'w', encoding='utf-8') as f:
    f.write(text)
