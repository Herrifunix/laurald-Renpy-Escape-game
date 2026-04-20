default has_cle_cloitre = False
default met_pnj_entree = False

screen exterieur_parvis_screen():
    text "Parvis de la Cathédrale" size 50 xalign 0.5 ypos 50 font "OldLondon.ttf"
    
    # Navigation
    textbutton "Aller vers le Cloître (Ouest)" action Jump("exterieur_ouest") xalign 0.1 yalign 0.5 text_size 30 background "#333b"
    textbutton "Aller vers le Chevet (Est)" action Jump("exterieur_est") xalign 0.9 yalign 0.5 text_size 30 background "#333b"
    
    # Entrée
    textbutton "Entrer dans la Cathédrale" action Jump("entrer_cathedrale_garde") xalign 0.5 yalign 0.8 text_size 40 background "#632b"

screen exterieur_ouest_screen():
    text "Côté Cloître (Ouest)" size 50 xalign 0.5 ypos 50 font "OldLondon.ttf"
    
    textbutton "Retour au Parvis" action Jump("exterieur_parvis") xalign 0.9 yalign 0.5 text_size 30 background "#333b"
    textbutton "Entrer dans le Cloître" action Jump("tentative_entree_cloitre") xalign 0.5 yalign 0.8 text_size 40 background "#632b"

screen exterieur_est_screen():
    text "Chevet Est de la Cathédrale" size 50 xalign 0.5 ypos 50 font "OldLondon.ttf"
    
    textbutton "Retour au Parvis" action Jump("exterieur_parvis") xalign 0.1 yalign 0.5 text_size 30 background "#333b"
    if not has_cle_cloitre:
        textbutton "Inspecter les recoins" action Jump("trouver_cle_cloitre") xalign 0.5 yalign 0.8 text_size 40 background "#632b"


label exterieur_parvis:
    hide screen exterieur_ouest_screen
    hide screen exterieur_est_screen
    scene bg accueil
    play music "audio/Solas-InnOfGoodFortune.mp3" fadein 1.0 if_changed
    show screen exterieur_parvis_screen
    pause
    jump exterieur_parvis

label entrer_cathedrale_garde:
    hide screen exterieur_parvis_screen
    if not met_pnj_entree:
        "Un employé se dresse devant les grandes portes en croisant les bras."
        "Employé" "Désolé, la cathédrale n'est pas encore ouverte au public. Il y a des préparatifs en cours pour un événement, revenez plus tard !"
        $ met_pnj_entree = True
    else:
        "Employé" "Je vous l'ai déjà dit, l'entrée est interdite pour le moment."
    jump exterieur_parvis

label exterieur_ouest:
    hide screen exterieur_parvis_screen
    # Vous pouvez changer 'bg accueil' par un background specifique à l'ouest plus tard
    scene bg accueil
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
    # on utilise portail_sud ou une autre image en attendant mieux
    scene bg portail_sud
    play music "audio/Solas-InnOfGoodFortune.mp3" fadein 1.0 if_changed
    show screen exterieur_est_screen
    pause
    jump exterieur_est

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
