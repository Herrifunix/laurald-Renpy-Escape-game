default has_cle_cloitre = False
default met_pnj_entree = False

transform pulse_alpha:
    alpha 0.5
    linear 1.0 alpha 1.0
    linear 1.0 alpha 0.5
    repeat

screen exterieur_parvis_screen():
    text "Parvis de la Cathédrale" size 50 xalign 0.5 ypos 50 font "OldLondon.ttf"
    
    # Navigation (flèches latérales)
    button:
        xalign 0.0 yalign 0.5 xysize (150, 1080)
        action Jump("exterieur_ouest")
        background Solid("#0000") hover_background Solid("#0008")
        text "<" align (0.5, 0.5) size 80 color "#fff"
        
    button:
        xalign 1.0 yalign 0.5 xysize (150, 1080)
        action Jump("exterieur_est")
        background Solid("#0000") hover_background Solid("#0008")
        text ">" align (0.5, 0.5) size 80 color "#fff"
    
    # Entrée (Porte Centrale)
    imagebutton:
        # Ajustez xpos et ypos pour superposer exactement l'image sur le décor
        xalign 0.295 yalign 0.84
        idle "images/scenes/portes-avant.png"
        hover Transform("images/scenes/portes-avant.png", zoom=1.05)
        focus_mask True
        action Jump("entrer_cathedrale_garde")

screen exterieur_ouest_screen():
    text "Côté Cloître (Ouest)" size 50 xalign 0.5 ypos 50 font "OldLondon.ttf"
    
    # Navigation (flèches latérales)
    button:
        xalign 0.0 yalign 0.5 xysize (150, 1080)
        action Jump("exterieur_nord")
        background Solid("#0000") hover_background Solid("#0008")
        text "<" align (0.5, 0.5) size 80 color "#fff"
        
    button:
        xalign 1.0 yalign 0.5 xysize (150, 1080)
        action Jump("exterieur_parvis")
        background Solid("#0000") hover_background Solid("#0008")
        text ">" align (0.5, 0.5) size 80 color "#fff"
    
    # Entrée Basse Oeuvre
    button:
        xalign 0.45 yalign 0.65 xysize (350, 500)
        action Jump("entrer_basse_oeuvre")
        background Solid("#0000") hover_background Solid("#ffffff22")

    # Entrée Cloître (partie rouge)
    imagebutton:
        xalign 0.701 yalign 0.99
        idle "images/scenes/porte-cloitre.png"
        hover Transform("images/scenes/porte-cloitre.png", zoom=1.05)
        focus_mask True
        action Jump("tentative_entree_cloitre")

screen exterieur_est_screen():
    text "Chevet de la Cathédrale" size 50 xalign 0.5 ypos 50 font "OldLondon.ttf"
    
    # Navigation (flèches latérales)
    button:
        xalign 0.0 yalign 0.5 xysize (150, 1080)
        action Jump("exterieur_parvis")
        background Solid("#0000") hover_background Solid("#0008")
        text "<" align (0.5, 0.5) size 80 color "#fff"
        
    button:
        xalign 1.0 yalign 0.5 xysize (150, 1080)
        action Jump("exterieur_nord")
        background Solid("#0000") hover_background Solid("#0008")
        text ">" align (0.5, 0.5) size 80 color "#fff"
    
    # Zone cliquable pour trouver la clé du cloître
    if not has_cle_cloitre:
        button:
            xalign 0.7 yalign 0.85 xysize (200, 150)
            action Jump("trouver_cle_cloitre")
            background Solid("#0000") hover_background Solid("#ff03")
            text "❗" align (0.5, 0.5) color "#ff0" hover_color "#ffff" size 80 at pulse_alpha

    # Mosaïque
    textbutton "Observer la mosaïque" action Jump("visiter_mosaique") xalign 0.5 yalign 0.15 text_size 30 background "#333b"

screen exterieur_nord_screen():
    text "Portail Nord" size 50 xalign 0.5 ypos 50 font "OldLondon.ttf"
    
    # Navigation (flèches latérales)
    button:
        xalign 0.0 yalign 0.5 xysize (150, 1080)
        action Jump("exterieur_est")
        background Solid("#0000") hover_background Solid("#0008")
        text "<" align (0.5, 0.5) size 80 color "#fff"
        
    button:
        xalign 1.0 yalign 0.5 xysize (150, 1080)
        action Jump("exterieur_ouest")
        background Solid("#0000") hover_background Solid("#0008")
        text ">" align (0.5, 0.5) size 80 color "#fff"
        
    # Entrée Portail Nord
    imagebutton:
        xalign 0.35 yalign 0.65
        idle "images/scenes/portes-nord.png"
        hover Transform("images/scenes/portes-nord.png", zoom=1.05)
        focus_mask True
        action Jump("entrer_nord")


label exterieur_parvis:
    hide screen exterieur_ouest_screen
    hide screen exterieur_est_screen
    hide screen exterieur_nord_screen
    scene bg accueil
    play music "audio/Solas-InnOfGoodFortune.mp3" fadein 1.0 if_changed
    show screen exterieur_parvis_screen
    pause
    jump exterieur_parvis

label entrer_cathedrale_garde:
    hide screen exterieur_parvis_screen
    hide screen exterieur_ouest_screen
    hide screen exterieur_est_screen
    hide screen exterieur_nord_screen
    show hotesse at center
    if not met_pnj_entree:
        "Une hôtesse se dresse devant les grandes portes en vous souriant légèrement."
        "Hôtesse" "Désolé, la cathédrale n'est pas encore ouverte au public. Il y a des préparatifs en cours pour un événement."
        show hotesse bye at center
        "Hôtesse" "Revenez plus tard !"
        $ met_pnj_entree = True
    else:
        show hotesse triste at center
        "Hôtesse" "Je vous l'ai déjà dit, l'entrée est toujours interdite pour le moment."
    hide hotesse
    jump exterieur_parvis

label exterieur_ouest:
    hide screen exterieur_parvis_screen
    hide screen exterieur_est_screen
    hide screen exterieur_nord_screen
    scene bg basse_oeuvre_ouest
    play music "audio/Solas-InnOfGoodFortune.mp3" fadein 1.0 if_changed
    show screen exterieur_ouest_screen
    pause
    jump exterieur_ouest

label tentative_entree_cloitre:
    hide screen exterieur_ouest_screen
    if has_cle_cloitre:
        "Vous glissez la vieille clé trouvée à l'Est dans l'imposante serrure de la porte du cloître..."
        "La lourde porte s'ouvre dans un couinement sourd."
        jump rencontre_moine
    else:
        "La porte massive menant au cloître est fermée à clé."
        "Il faudrait d'abord trouver le moyen de l'ouvrir."
        jump exterieur_ouest

label exterieur_est:
    hide screen exterieur_parvis_screen
    hide screen exterieur_ouest_screen
    hide screen exterieur_nord_screen
    scene bg chevet_est
    play music "audio/Solas-InnOfGoodFortune.mp3" fadein 1.0 if_changed
    show screen exterieur_est_screen
    pause
    jump exterieur_est

label exterieur_nord:
    hide screen exterieur_parvis_screen
    hide screen exterieur_ouest_screen
    hide screen exterieur_est_screen
    scene bg portail_nord
    play music "audio/Solas-InnOfGoodFortune.mp3" fadein 1.0 if_changed
    show screen exterieur_nord_screen
    pause
    jump exterieur_nord

label entrer_basse_oeuvre:
    hide screen exterieur_ouest_screen
    "Vous tentez d'ouvrir la porte de la Basse-Œuvre, mais elle résiste."
    "La Basse-Œuvre est pour le moment fermée."
    jump exterieur_ouest

label entrer_nord:
    hide screen exterieur_nord_screen
    "La grande porte du transept est fermée."
    "Rien ne semble indiquer qu'elle puisse être ouverte depuis l'extérieur."
    jump exterieur_nord

label trouver_cle_cloitre:
    hide screen exterieur_est_screen
    "En fouillant attentivement près des murs et derrière de petits arbustes sur ce pan du bâtiment..."
    "Vous trouvez une très vieille clé métallique dissimulée sous des feuilles !"
    
    $ has_cle_cloitre = True
    
    python:
        # On crée un objet "Clé du cloître" et on le place dans l'inventaire visuel si activé
        cle_cloitre_item = Item("Clé du Cloître", "Une vieille clé trouvée du côté Est de la cathédrale.", "cryptex-mini.png", item_id="cle_cloitre")
        player_inventory.add_item(cle_cloitre_item)
        
    $ renpy.notify("Vous avez obtenu la Clé du Cloître !")
    jump exterieur_est

