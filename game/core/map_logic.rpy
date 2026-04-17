# map_logic.rpy
# Variables pour activer/désactiver les lieux sur la carte
default location_cloitre_active = True
default location_accueil_active = True
default location_basse_oeuvre_active = True
default location_orgue_active = True
default location_croisee_active = False # Était commenté
default location_horloge_active = True
default location_choeur_active = True

# Screen de debug pour activer/désactiver les lieux
screen debug_map_locations():
    modal True
    tag debug_map
    style_prefix "confirm"
    
    frame:
        xalign 0.5
        yalign 0.5
        padding (40, 40)
        
        vbox:
            spacing 10
            label "Menu Debug - Lieux (Locations)" xalign 0.5
            
            textbutton "Cloître" action ToggleVariable("location_cloitre_active")
            textbutton "Accueil" action ToggleVariable("location_accueil_active")
            textbutton "Basse Oeuvre" action ToggleVariable("location_basse_oeuvre_active")
            textbutton "Orgue" action ToggleVariable("location_orgue_active")
            textbutton "Croisée" action ToggleVariable("location_croisee_active")
            textbutton "Horloge" action ToggleVariable("location_horloge_active")
            textbutton "Choeur" action ToggleVariable("location_choeur_active")
            
            null height 20
            
            textbutton "Fermer" action Hide("debug_map_locations") xalign 0.5

# Style pour le texte du debug
style debug_text is text:
    size 24
    color "#ffffff"
