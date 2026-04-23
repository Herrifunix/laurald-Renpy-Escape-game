init python:
    def advance_time():
        times = ['matin', 'midi', 'soir', 'nuit']
        current_idx = times.index(store.time_of_day)
        store.time_of_day = times[(current_idx + 1) % len(times)]
        renpy.restart_interaction()

default time_of_day = "matin"

screen horloge_ui():
    zorder 100
    frame:
        xalign 0.98 yalign 0.02
        padding (10, 10)
        background "#000a"
        vbox:
            spacing 5
            text "Heure : [time_of_day.capitalize()]" size 20 color "#fff" xalign 0.5
            textbutton "Avancer le temps" action Function(advance_time) xalign 0.5 text_size 16

screen salle_mosaique():
    # Décor principal
    add "#222" # Mur sombre
    
    # La mosaïque de base
    frame:
        xalign 0.5 yalign 0.4
        xysize (600, 400)
        background "#555"
        text "Mosaïque Ancienne" xalign 0.5 ypos 10 size 30 color "#aaa"
        
        # Motif selon l'heure
        if time_of_day == "matin":
            add Solid("#ffff99", xysize=(200, 200)) xalign 0.2 yalign 0.5
            text "Un motif de soleil se révèle à la lumière de l'Est." xalign 0.5 yalign 0.9 size 24 color "#ffff99"
        elif time_of_day == "midi":
            add Solid("#ffffcc", xysize=(200, 200)) xalign 0.5 yalign 0.5
            text "Le zénith illumine le centre de la fresque." xalign 0.5 yalign 0.9 size 24 color "#ffffcc"
        elif time_of_day == "soir":
            add Solid("#ff9966", xysize=(200, 200)) xalign 0.8 yalign 0.5
            text "Les rayons couchants frappent le côté Ouest." xalign 0.5 yalign 0.9 size 24 color "#ff9966"
        elif time_of_day == "nuit":
            add Solid("#666699", xysize=(200, 200)) xalign 0.5 yalign 0.5
            text "L'obscurité fait briller des symboles lunaires cachés." xalign 0.5 yalign 0.9 size 24 color "#bfbfff"

    textbutton "Quitter la salle" action Jump("exterieur_parvis") xalign 0.5 yalign 0.9 text_size 30 background "#333b"

label visiter_mosaique:
    show screen horloge_ui
    call screen salle_mosaique
    hide screen horloge_ui
    return