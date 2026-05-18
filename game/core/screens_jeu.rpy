################################################################################
## Écrans spécifiques au jeu (escape game)
##
## Écrans personnalisés : inventaire, plan/carte, coffre, cryptex, cadenas,
## boutons de PNJ, etc. Séparés de screens.rpy (écrans standards de Ren'Py)
## pour la lisibilité. Ren'Py charge les deux fichiers automatiquement.
################################################################################

# Eveque bouton dans le cloitre :
screen eveque_button():
    imagebutton:
        # Utilisez l'image de l'évêque pour le bouton
        idle "eveque.png"   # Image lorsque l'évêque n'est pas survolé
        hover "eveque_hover.png" # Image lorsque l'évêque est survolé
        xpos 0  # Position x du bouton
        ypos 200  # Position y du bouton
        action Jump("dial_eveque") # Étiquette vers laquelle sauter lorsque cliqué

screen eveque_button2():
    imagebutton:
        # Utilisez l'image de l'évêque pour le bouton
        idle "eveque.png"   # Image lorsque l'évêque n'est pas survolé
        hover "eveque_hover.png" # Image lorsque l'évêque est survolé
        xpos 0  # Position x du bouton
        ypos 200  # Position y du bouton
        action Jump("dial_eveque2") # Étiquette vers laquelle sauter lorsque cliqué

# Plan carolingienne
screen carolingienne():
    modal True
    frame:
        background None
        align (0.5, 0.5)  # Centre le frame à l'écran
        add "images/items/cryptex.png"

# Plan Art Français
screen artfrancais():
    modal True
    frame:
        background None
        align (0.5, 0.5)  # Centre le frame à l'écran
        add "images/items/cryptex.png"

#######################################################################################################################################################################################
# AFFICHAGE DU 1ER COFFRE DU JEU
# Style de frame transparent
style transparent_frame:
        background None
        xpadding 0
        ypadding 0
        
screen cadenas():
    modal True
    frame:
        background None
        align (0.5, 0.5)  # Centre le frame à l'écran
        add "images/items/coffre-taille-normale.png"

    frame:
        background None
        align (0.5, 0.5)  # Centre le frame à l'écran
        #xpos 650
        #ypos 450
        vbox:
            hbox:
                spacing 10

                vbox:
                    imagebutton auto "images/safe_i/up_%s.png" focus_mask True xalign .5 yalign .365 action If(numb1 < 9, SetVariable("numb1", numb1 + 1), SetVariable("numb1", 0))
                    add "images/safe_i/cl_%s.png" % (numb1) xalign .5 yalign .47 zoom 0.9
                    imagebutton auto "images/safe_i/dwn_%s.png" focus_mask True xalign .5 yalign .59 action If(numb1 > 0, SetVariable("numb1", numb1 - 1), SetVariable("numb1", 9))

                vbox:
                    imagebutton auto "images/safe_i/up_%s.png" focus_mask True xalign .5 yalign .365 action If(numb2 < 9, SetVariable("numb2", numb2 + 1), SetVariable("numb2", 0))
                    add "images/safe_i/cl_%s.png" % (numb2) xalign .5 yalign .47 zoom 0.9
                    imagebutton auto "images/safe_i/dwn_%s.png" focus_mask True xalign .5 yalign .59 action If(numb2 > 0, SetVariable("numb2", numb2 - 1), SetVariable("numb2", 9))

                vbox:
                    imagebutton auto "images/safe_i/up_%s.png" focus_mask True xalign .5 yalign .365 action If(numb3 < 9, SetVariable("numb3", numb3 + 1), SetVariable("numb3", 0))
                    add "images/safe_i/cl_%s.png" % (numb3) xalign .5 yalign .47 zoom 0.9
                    imagebutton auto "images/safe_i/dwn_%s.png" focus_mask True xalign .5 yalign .59 action If(numb3 > 0, SetVariable("numb3", numb3 - 1), SetVariable("numb3", 9))

                vbox:
                    imagebutton auto "images/safe_i/up_%s.png" focus_mask True xalign .5 yalign .365 action If(numb4 < 9, SetVariable("numb4", numb4 + 1), SetVariable("numb4", 0))
                    add "images/safe_i/cl_%s.png" % (numb4) xalign .5 yalign .47 zoom 0.9
                    imagebutton auto "images/safe_i/dwn_%s.png" focus_mask True xalign .5 yalign .59 action If(numb4 > 0, SetVariable("numb4", numb4 - 1), SetVariable("numb4", 9))

# Afficher le bouton image
    imagebutton:
        idle "images/safe_i/button_idle.png"  # Image pour l'état normal
        hover "images/safe_i/button_hover.png"  # Image pour l'état survolé
        hover_sound "audio/bouton.wav" # bouton de mécanisme
        xalign 0.5
        yalign 0.32
        action If(numb1 == 1 and numb2 == 2 and numb3 == 2 and numb4 == 5,
                    [Hide("inventory_screen"), Jump("coffre_ouvert")], # en cas de réussite : on cache le screen du coffe et le screen de l'inventaire et on saut vers coffre ouvert
                    Show("access_denied")) # en cas de mauvais code, on affiche le screen access_denied

#acces refusé pour l'acces au 1er coffre
screen access_denied():
    modal True
    frame:
        background "#524d4dcc"
        align (0.5, 0.5)  # Centrer la fenêtre à l'écran
        vbox:
            text "Mauvaise combinaison !" size 50 xalign 0.5 yalign 0.32
            textbutton "✖" xalign 0.5 yalign 0.45 action Hide("access_denied") # affiche une croix pour fermer la fenetre


        
#######################################################################################################################################################################################
###############CRYPTEX
screen cryptex():
    modal True
    frame:
        background None
        align (0.5, 0.5)  # Centre le frame à l'écran
        add "images/items/cryptex.png"

    frame:
        background None
        align (0.5, 0.5)  # Centre le frame à l'écran
        #xpos 650
        #ypos 450
        vbox:
            hbox:
                spacing 10
                #on affiche d'abord le bouton fleche qui increment la lettre, puis l'image, puis le bouton pour décrémenter
                vbox:
                    imagebutton auto "images/safe_i/up_%s.png" focus_mask True xalign .5 yalign .365 action If(lettre1 < 26, SetVariable("lettre1", lettre1 + 1), SetVariable("lettre1", 1))
                    add "images/safe_i/l_%s.png" % (lettre1) xalign .5 yalign .47 zoom 0.9
                    imagebutton auto "images/safe_i/dwn_%s.png" focus_mask True xalign .5 yalign .59 action If(lettre1 > 1, SetVariable("lettre1", lettre1 - 1), SetVariable("lettre1", 26))

                vbox:
                    imagebutton auto "images/safe_i/up_%s.png" focus_mask True xalign .5 yalign .365 action If(lettre2 < 26, SetVariable("lettre2", lettre2 + 1), SetVariable("lettre2", 1))
                    add "images/safe_i/l_%s.png" % (lettre2) xalign .5 yalign .47 zoom 0.9
                    imagebutton auto "images/safe_i/dwn_%s.png" focus_mask True xalign .5 yalign .59 action If(lettre2 > 1, SetVariable("lettre2", lettre2 - 1), SetVariable("lettre2", 26))

                vbox:
                    imagebutton auto "images/safe_i/up_%s.png" focus_mask True xalign .5 yalign .365 action If(lettre3 < 26, SetVariable("lettre3", lettre3 + 1), SetVariable("lettre3", 1))
                    add "images/safe_i/l_%s.png" % (lettre3) xalign .5 yalign .47 zoom 0.9
                    imagebutton auto "images/safe_i/dwn_%s.png" focus_mask True xalign .5 yalign .59 action If(lettre3 > 1, SetVariable("lettre3", lettre3 - 1), SetVariable("lettre3", 26))

                vbox:
                    imagebutton auto "images/safe_i/up_%s.png" focus_mask True xalign .5 yalign .365 action If(lettre4 < 26, SetVariable("lettre4", lettre4 + 1), SetVariable("lettre4", 1))
                    add "images/safe_i/l_%s.png" % (lettre4) xalign .5 yalign .47 zoom 0.9
                    imagebutton auto "images/safe_i/dwn_%s.png" focus_mask True xalign .5 yalign .59 action If(lettre4 > 1, SetVariable("lettre4", lettre4 - 1), SetVariable("lettre4", 26))
                    
                vbox:
                    imagebutton auto "images/safe_i/up_%s.png" focus_mask True xalign .5 yalign .365 action If(lettre5 < 26, SetVariable("lettre5", lettre5 + 1), SetVariable("lettre5", 1))
                    add "images/safe_i/l_%s.png" % (lettre5) xalign .5 yalign .47 zoom 0.9
                    imagebutton auto "images/safe_i/dwn_%s.png" focus_mask True xalign .5 yalign .59 action If(lettre5 > 1, SetVariable("lettre5", lettre5 - 1), SetVariable("lettre5", 26))
    # Afficher les boutons images
    imagebutton:
        idle "images/safe_i/cryptg_idle.png"  # Image pour l'état normal
        hover "images/safe_i/cryptg_hover.png"  # Image pour l'état survolé
        hover_sound "audio/bouton.wav" # bouton de mécanisme
        xalign 0.365
        yalign 0.49
        action If(lettre1 == 2 and lettre2 == 1 and lettre3 == 2 and lettre4 == 5 and lettre5 == 12,
                    Jump("Horloge"),
                    Show("access_denied2"))
    imagebutton:
        idle "images/safe_i/cryptd_idle.png"  # Image pour l'état normal
        hover "images/safe_i/cryptd_hover.png"  # Image pour l'état survolé
        hover_sound "audio/bouton.wav" # bouton de mécanisme
        xalign 0.62
        yalign 0.49
        action If(lettre1 == 2 and lettre2 == 1 and lettre3 == 2 and lettre4 == 5 and lettre5 == 12,
                    Jump("Horloge"),
                    Show("access_denied2"))

#############COFFRE
screen coffre:
    imagebutton:
        xpos 325
        ypos 810
        idle "images/items/coffre-mini.png"
        hover "images/items/coffre-mini-UP.png"
        action Jump("coffre_recupere")
        
#############PARCHEMIN dans la main de l'eveque
#############PARCHEMIN dans la main de l'eveque
screen parchemin:
    imagebutton:
        xpos 325
        ypos 810
        idle "images/items/parchemin.png"
        hover "images/items/parchemin-up.png"
        action Jump("parchemin_recupere")


#############PARCHEMIN affiché
screen parchemin_recupere:
    imagebutton:
        xpos 1000
        ypos 200
        idle "images/items/parchemin1.png"
        action Jump("coffre")

#############Grille horloge
screen grille_horloge:
    if not clef_horloge:
        imagebutton:
            xpos 0.37
            ypos 0.551
            idle "images/gui/open_image.png"  # Image de l'état normal du bouton
            hover "images/gui/open_image_hover.png"  # Image de l'état survolé du bouton     
            action ShowMenu("message_screen")  # Action à exécuter
            #action Function(afficher_dialogue) #Appel le dialogue définir dans script.rpy
    else:
        imagebutton:
            xpos 0.37
            ypos 0.551 #hauteur
            idle "images/gui/open_image.png"  # Image de l'état normal du bouton
            hover "images/gui/open_image_hover.png"  # Image de l'état survolé du bouton     
            action Jump("grille_horloge_ouvert")  # Action à exécuter

#######################################################################################################################################################################################
##############INVENTAIRE
# Icône d'inventaire en haut à droite de l'écran.
screen inventory_icon():
    imagebutton:
        idle "images/gui/backpack.png"
        hover "images/gui/backpack-hover.png"
        action [SetVariable("selected_item", None), Show("inventory_screen")]
        xpos 0.05
        ypos 0.05
        xanchor 1.0
        yanchor 0.0

# Screen pour afficher l'inventaire.
screen inventory_screen():
    modal True
    tag inventory

    # Fond semi-transparent pour l'inventaire
    add "images/gui/inventory_bg.png"
    
    # Grid pour afficher les objets (4 col, 3 lignes).
    $ inventaire_items = player_inventory.get_items()
    grid 4 3 spacing 25 xalign 0.5 yalign 0.35:
        for i in range(12):
            if i < len(inventaire_items):
                $ item = inventaire_items[i]
                # Le conteneur de chaque objet
                button:
                    action SetVariable("selected_item", item)
                    xysize (180, 180)
                    background None # Fond transparent
                    hover_background Solid("#ffffff22") # Léger survol
                    
                    # Image contenue et redimensionnée sans déformer pour ne pas déborder
                    add Transform(item.image, fit="contain", xysize=(160, 160), align=(0.5, 0.5))
            else:
                # Cellule vide
                frame:
                    xysize (180, 180)
                    background None
    
    # Zone d'information sur l'objet sélectionné.
    frame:
        xalign 0.5
        yalign 0.8
        background "#aa690841" #fond transparent
        vbox:
            xalign 0.5 #alignement du contenu au centre
            if selected_item:
                text "[selected_item.name]" size 54 xalign 0.5 font "OldLondon.ttf"
                text "[selected_item.description]\n" size 30 xalign 0.5 font "OldLondon.ttf"
                
                # Bouton de craft
                textbutton "Combiner" action [SetVariable("crafting_selected_item", selected_item), Show("crafting_selection_screen")] xalign 0.5
                
                for action in selected_item.actions:
                    textbutton action["label"] action action["action"] xalign 0.5
            else:
                text "Sélectionnez un objet pour voir les détails." size 50 xalign 0.5 font "OldLondon.ttf"

    # Bouton Debug (visible seulement en mode dev)
    if config.developer:
        textbutton "Debug Carte" action [SetVariable("selected_item", None), Hide("inventory_screen"), Show("debug_map_locations")]:
            xalign 0.95
            yalign 0.05
            text_color "#ff0000"

    # Bouton Mini-Jeux (visible seulement en mode dev)
    if config.developer:
        textbutton "Debug Jeux" action [SetVariable("selected_item", None), Hide("inventory_screen"), ShowMenu("debug_minigames")]:
            xalign 0.95
            yalign 0.1
            text_color "#00ff00"

    # Bouton pour fermer l'inventaire
    #textbutton "Fermer" action Hide("inventory_screen"):
    textbutton "Fermer" action [
        SetVariable("selected_item", None),  # Réinitialiser la sélection
        Hide("inventory_screen")
    ]:
        xalign 0.5
        yalign 0.1

# Screen pour afficher le  parchemin dans l'inventaire.
screen inventory_parchemin():
    modal True
    tag inventory_parchemin

    # Fond semi-transparent pour l'inventaire
    add "images/gui/inventory_bg.png"
    add "images/items/parchemin1.png" xalign 0.5 yalign 0.5

    # Bouton pour fermer l'inventaire
    #textbutton "Fermer" action Return():
    textbutton "Fermer" action Hide("inventory_parchemin"):
        xalign 0.5
        yalign 0.1
##############################################################################################
#AFFICHAGE DE LA CARTE ##################
screen plan_icon():
    imagebutton:
        idle "images/gui/minimap.png"
        hover "images/gui/minimap-hover.png"
        action [SetVariable("selected_item", None), Show("plan_screen")]
        xpos 0.99
        ypos 0.05
        xanchor 1.0
        yanchor 0.0

screen plan_screen():
    modal True
    tag plan
    frame:
    # affichage du fond du plan 
        xalign 0.5
        yalign 0.8
        add "images/items/plan_cathedrale_grand_fond.png"
    #affichage du plan interactif
    frame:
        xalign 0.5
        yalign 0.8
        background None
        imagemap:
            ground "images/items/plan_cathedrale.png"
            
            if location_cloitre_active:
                hotspot (279, 90, 271, 245) action [Hide ("plan_screen"), Jump("eveque_cloitre")] #cloitre
            
            if location_accueil_active:
                hotspot (645, 315, 137, 62) action [Hide ("plan_screen"), Jump("Accueil")] #Accueil
            
            if location_basse_oeuvre_active:
                hotspot (277, 354, 131, 185) action [Hide ("plan_screen"), Jump("basse_oeuvre")] #basse oeuvre

            if location_orgue_active:
                hotspot (522, 439, 84, 153) action [Hide ("plan_screen"), Jump("orgues")] #orgue
            
            if location_croisee_active:
                hotspot (97, 82, 24, 24) action [Hide ("plan_screen"), Jump("map_classe")] #croisée
            
            if location_horloge_active:
                hotspot (776, 246, 78, 98) action [Hide ("plan_screen"), Jump("Horloge")] #horloge
            
            if location_choeur_active:
                hotspot (786, 442, 75, 146) action [Hide ("plan_screen"), Jump("choeur")] #choeur

        # Ajout de boutons visuels cliquables par-dessus le fond
        if location_orgue_active:
            textbutton "Orgue" action [Hide ("plan_screen"), Jump("orgues")] xpos 522 ypos 439 text_size 30 text_color "#FFF" background "#aa690841"
            
        if location_horloge_active:
            textbutton "Horloge" action [Hide ("plan_screen"), Jump("Horloge")] xpos 776 ypos 246 text_size 30 text_color "#FFF" background "#aa690841"
            
        if location_cloitre_active:
            textbutton "Cloître" action [Hide ("plan_screen"), Jump("eveque_cloitre")] xpos 279 ypos 90 text_size 30 text_color "#FFF" background "#aa690841"
            
        if location_accueil_active:
            textbutton "Accueil" action [Hide ("plan_screen"), Jump("Accueil")] xpos 645 ypos 315 text_size 30 text_color "#FFF" background "#aa690841"

        if location_basse_oeuvre_active:
            textbutton "Basse Oeuvre" action [Hide ("plan_screen"), Jump("basse_oeuvre")] xpos 277 ypos 354 text_size 30 text_color "#FFF" background "#aa690841"

        if location_choeur_active:
            textbutton "Chœur" action [Hide ("plan_screen"), Jump("choeur")] xpos 786 ypos 442 text_size 30 text_color "#FFF" background "#aa690841"

    # Bouton pour fermer la carte
    textbutton "Fermer" action [
        Hide("plan_screen")
    ]:
        xalign 0.5
        yalign 0.1


##############################################################################################
# Screen pour afficher le Coffre 1 dans l'inventaire.
screen inventory_coffre1():
    modal True
    tag inventory_coffre1

    # Fond semi-transparent pour l'inventaire
    add "images/gui/inventory_bg.png"
    frame:
        background None
        align (0.5, 0.5)  # Centre le frame à l'écran
        add "images/items/coffre-taille-normale.png"

    frame:
        background None
        align (0.5, 0.5)  # Centre le frame à l'écran
        #xpos 650
        #ypos 450
        vbox:
            hbox:
                spacing 10

                vbox:
                    imagebutton auto "images/safe_i/up_%s.png" focus_mask True xalign .5 yalign .365 action If(numb1 < 9, SetVariable("numb1", numb1 + 1), SetVariable("numb1", 0))
                    add "images/safe_i/cl_%s.png" % (numb1) xalign .5 yalign .47 zoom 0.9
                    imagebutton auto "images/safe_i/dwn_%s.png" focus_mask True xalign .5 yalign .59 action If(numb1 > 0, SetVariable("numb1", numb1 - 1), SetVariable("numb1", 9))

                vbox:
                    imagebutton auto "images/safe_i/up_%s.png" focus_mask True xalign .5 yalign .365 action If(numb2 < 9, SetVariable("numb2", numb2 + 1), SetVariable("numb2", 0))
                    add "images/safe_i/cl_%s.png" % (numb2) xalign .5 yalign .47 zoom 0.9
                    imagebutton auto "images/safe_i/dwn_%s.png" focus_mask True xalign .5 yalign .59 action If(numb2 > 0, SetVariable("numb2", numb2 - 1), SetVariable("numb2", 9))

                vbox:
                    imagebutton auto "images/safe_i/up_%s.png" focus_mask True xalign .5 yalign .365 action If(numb3 < 9, SetVariable("numb3", numb3 + 1), SetVariable("numb3", 0))
                    add "images/safe_i/cl_%s.png" % (numb3) xalign .5 yalign .47 zoom 0.9
                    imagebutton auto "images/safe_i/dwn_%s.png" focus_mask True xalign .5 yalign .59 action If(numb3 > 0, SetVariable("numb3", numb3 - 1), SetVariable("numb3", 9))

                vbox:
                    imagebutton auto "images/safe_i/up_%s.png" focus_mask True xalign .5 yalign .365 action If(numb4 < 9, SetVariable("numb4", numb4 + 1), SetVariable("numb4", 0))
                    add "images/safe_i/cl_%s.png" % (numb4) xalign .5 yalign .47 zoom 0.9
                    imagebutton auto "images/safe_i/dwn_%s.png" focus_mask True xalign .5 yalign .59 action If(numb4 > 0, SetVariable("numb4", numb4 - 1), SetVariable("numb4", 9))

# Afficher le bouton image
    imagebutton:
        idle "images/safe_i/button_idle.png"  # Image pour l'état normal
        hover "images/safe_i/button_hover.png"  # Image pour l'état survolé
        hover_sound "audio/bouton.wav" # bouton de mécanisme
        xalign 0.5
        yalign 0.32
        action If(numb1 == 1 and numb2 == 2 and numb3 == 2 and numb4 == 5,
                    If(debug_minigame_mode,
                        [Hide("inventory_coffre1"), Notify("Mini-jeu Coffre réussi")],
                        [Hide("inventory_screen"), Jump("coffre_ouvert")]),
                    Show("access_denied"))

    # Bouton pour fermer l'inventaire
    textbutton "Fermer" action Hide("inventory_coffre1"):
        xalign 0.5
        yalign 0.1

##############################################################################################
# Screen pour afficher le CRYPTEX dans l'inventaire.
screen inventory_cryptex():
    modal True
    tag inventory_cryptex
    add "images/gui/inventory_bg.png"
    frame:
        background None
        align (0.5, 0.5)  # Centre le frame à l'écran
        add "images/items/cryptex.png"

    frame:
        background None
        align (0.5, 0.5)  # Centre le frame à l'écran
        #xpos 650
        #ypos 450
        vbox:
            hbox:
                spacing 10
                #on affiche d'abord le bouton fleche qui increment la lettre, puis l'image, puis le bouton pour décrémenter
                vbox:
                    imagebutton auto "images/safe_i/up_%s.png" focus_mask True xalign .5 yalign .365 action If(lettre1 < 26, SetVariable("lettre1", lettre1 + 1), SetVariable("lettre1", 1))
                    add "images/safe_i/l_%s.png" % (lettre1) xalign .5 yalign .47 zoom 0.9
                    imagebutton auto "images/safe_i/dwn_%s.png" focus_mask True xalign .5 yalign .59 action If(lettre1 > 1, SetVariable("lettre1", lettre1 - 1), SetVariable("lettre1", 26))

                vbox:
                    imagebutton auto "images/safe_i/up_%s.png" focus_mask True xalign .5 yalign .365 action If(lettre2 < 26, SetVariable("lettre2", lettre2 + 1), SetVariable("lettre2", 1))
                    add "images/safe_i/l_%s.png" % (lettre2) xalign .5 yalign .47 zoom 0.9
                    imagebutton auto "images/safe_i/dwn_%s.png" focus_mask True xalign .5 yalign .59 action If(lettre2 > 1, SetVariable("lettre2", lettre2 - 1), SetVariable("lettre2", 26))

                vbox:
                    imagebutton auto "images/safe_i/up_%s.png" focus_mask True xalign .5 yalign .365 action If(lettre3 < 26, SetVariable("lettre3", lettre3 + 1), SetVariable("lettre3", 1))
                    add "images/safe_i/l_%s.png" % (lettre3) xalign .5 yalign .47 zoom 0.9
                    imagebutton auto "images/safe_i/dwn_%s.png" focus_mask True xalign .5 yalign .59 action If(lettre3 > 1, SetVariable("lettre3", lettre3 - 1), SetVariable("lettre3", 26))

                vbox:
                    imagebutton auto "images/safe_i/up_%s.png" focus_mask True xalign .5 yalign .365 action If(lettre4 < 26, SetVariable("lettre4", lettre4 + 1), SetVariable("lettre4", 1))
                    add "images/safe_i/l_%s.png" % (lettre4) xalign .5 yalign .47 zoom 0.9
                    imagebutton auto "images/safe_i/dwn_%s.png" focus_mask True xalign .5 yalign .59 action If(lettre4 > 1, SetVariable("lettre4", lettre4 - 1), SetVariable("lettre4", 26))
                    
                vbox:
                    imagebutton auto "images/safe_i/up_%s.png" focus_mask True xalign .5 yalign .365 action If(lettre5 < 26, SetVariable("lettre5", lettre5 + 1), SetVariable("lettre5", 1))
                    add "images/safe_i/l_%s.png" % (lettre5) xalign .5 yalign .47 zoom 0.9
                    imagebutton auto "images/safe_i/dwn_%s.png" focus_mask True xalign .5 yalign .59 action If(lettre5 > 1, SetVariable("lettre5", lettre5 - 1), SetVariable("lettre5", 26))
    # Afficher les boutons images
    imagebutton:
        idle "images/safe_i/cryptg_idle.png"  # Image pour l'état normal
        hover "images/safe_i/cryptg_hover.png"  # Image pour l'état survolé
        hover_sound "audio/bouton.wav" # bouton de mécanisme
        xalign 0.365
        yalign 0.49
        action If(lettre1 == 2 and lettre2 == 1 and lettre3 == 2 and lettre4 == 5 and lettre5 == 12,
                    If(debug_minigame_mode,
                        [Hide("inventory_cryptex"), Notify("Mini-jeu Cryptex réussi")],
                        Jump("Horloge")),
                    Show("access_denied2"))
    imagebutton:
        idle "images/safe_i/cryptd_idle.png"  # Image pour l'état normal
        hover "images/safe_i/cryptd_hover.png"  # Image pour l'état survolé
        hover_sound "audio/bouton.wav" # bouton de mécanisme
        xalign 0.62
        yalign 0.49
        action If(lettre1 == 2 and lettre2 == 1 and lettre3 == 2 and lettre4 == 5 and lettre5 == 12,
                    If(debug_minigame_mode,
                        [Hide("inventory_cryptex"), Notify("Mini-jeu Cryptex réussi")],
                        Jump("Horloge")),
                    Show("access_denied2"))
        # Bouton pour fermer l'inventaire
    textbutton "Fermer" action Hide("inventory_cryptex"):
        xalign 0.5
        yalign 0.1

screen access_denied2():
    modal True
    frame:
        xpos 150
        ypos 150
        vbox:
            text "Mauvaise combinaison!" size 50 xalign 0.5 yalign 0.32
            textbutton "Essaie encore" xalign 0.5 yalign 0.45 action Hide("access_denied2")

    # Bouton pour fermer l'inventaire
    #textbutton "Fermer" action Return():
    textbutton "Fermer" action Hide("inventory_coffre1"):
        xalign 0.5
        yalign 0.1

#########COFFRE OUVERT

screen coffre_ouvert:
    modal True  # Empêche l'interaction avec d'autres éléments pendant que ce screen est affiché
    tag coffre_ouvert  # Ajout d'un tag pour permettre de cacher le screen avec le bouton "fermer"
    add "images/items/coffre-taille-normale-ouvert.png" xalign 0.5 yalign 0.5 # affiche l'image du coffre ouvert
    # Si le cryptex n'a pas été pris, on affiche un bouton dessus
    if not cryptex_taken:
        imagebutton:
            idle "images/items/cryptex-mini.png"  # Image du cryptex
            hover "images/items/cryptex-mini-hover.png"
            xpos 0.4  # Position x
            ypos 0.65  # Position y
            action [SetVariable("cryptex_taken", True), Function(player_inventory.add_item, cryptex)]

    # Si le plan n'a pas été pris, on affiche un bouton dessus
    if not plan_taken:
        imagebutton:
            idle "plan-parchemin.png"  # Image du plan
            hover "plan-parchemin-hover.png"
            xpos 0.5  # Position x
            ypos 0.65  # Position y
            action [SetVariable("plan_taken", True), Function(player_inventory.add_item, plan_parchemin)]
    
    # Si le morceau n'a pas été pris, on affiche un bouton dessus
    if not morceau_taken:
        imagebutton:
            idle "morceau_1.png"  # Image du morceau
            hover "morceau_1-hover.png"
            xpos 0.45  # Position x
            ypos 0.75  # Position y
            action [SetVariable("morceau_taken", True), Function(player_inventory.add_item, morceau_1)]

    # Bouton "fermer" qui n'apparaît que si tous les objets sont récupérés
    if cryptex_taken and plan_taken and morceau_taken:
        textbutton "Refermer le coffre":
            xpos 0.42  # Centré horizontalement
            ypos 0.3  # Placé sous les objets
            action Hide("coffre_ouvert")


# Définir l'écran pour afficher le message
screen message_screen:
    modal True

    # Boîte de dialogue pour le message
    frame:
        style_group "pref"
        xalign 0.5
        yalign 0.5

        vbox:
            text "Il vous faut une clef pour ouvrir la grille !"
            textbutton "X" action [Hide("message_screen")]

##################################################################################### images qui tournent :
screen rotating_image():
    # Afficher l'image rosace au centre
    add "images/scenes/rosace.png" xpos 0.5 ypos 0.5 anchor (0.5, 0.5)

    # Afficher l'image horloge par-dessus l'image rosace, avec rotation
    add Transform("/images/horloge.png", xpos=0.5, ypos=0.5, anchor=(0.5, 0.5), rotate=angle)

    # Bouton pour faire pivoter l'image dans le sens horaire
    textbutton "↻" action Function(rotate_clockwise) xpos 0.8 ypos 0.5 anchor (0.5, 0.5)

    # Bouton pour faire pivoter l'image dans le sens antihoraire
    textbutton "↺" action Function(rotate_counterclockwise) xpos 0.2 ypos 0.5 anchor (0.5, 0.5)


screen puzzle2_timer():
    zorder 200

    frame:
        xalign 0.97
        yalign 0.03
        xpadding 14
        ypadding 8
        background "#0009"
        $ min_left = puzzle2_time_left // 60
        $ sec_left = puzzle2_time_left % 60
        text ("Temps restant : %02d:%02d" % (min_left, sec_left)) size 28

    timer 1.0 repeat True action [
        SetVariable("puzzle2_time_left", max(0, puzzle2_time_left - 1)),
        If(puzzle2_time_left <= 1, [Hide("puzzle2_timer"), Jump("lose_2")], NullAction()),
    ]

################################# PUZZLE (ne fonctionne pas)
screen puzzle():
    modal True
    tag inventory_cryptex
    add "images/gui/inventory_bg.png"
    python:
        k = Puzzle()
        k.set_sensitive(False)
        k.show()    
    # Bouton pour fermer l'inventaire
    textbutton "Fermer" action Hide("puzzle"):
        xalign 0.5
        yalign 0.1
####################################### MORCEAU 1
screen inventory_morceau_1():
    modal True
    tag inventory_morceau_1
    add "images/gui/inventory_bg.png"
    frame:
        background None
        align (0.5, 0.5)  # Centre le frame à l'écran
        add "card/room-3-0.jpg"
    # Zone d'information
    frame:
        xalign 0.5
        yalign 0.8
        background "#aa690841" #fond transparent
        vbox:
            xalign 0.5 #alignement du contenu au centre
            text "Ceci est un morceau de parchemin, \n pour le comprendre, il va falloir en trouver d'autres."
            textbutton "+x+xTESTER LE JEUx+x+" action Jump("puzzle") xalign 0.5
    # Bouton pour fermer l'inventaire
    textbutton "Fermer" action Hide("inventory_morceau_1"):
        xalign 0.5
        yalign 0.1
screen image_viewer_screen(img):
    modal True
    zorder 100
    
    add "#000000cc"
    
    add img xalign 0.5 yalign 0.5
    
    textbutton "Fermer" action Hide("image_viewer_screen") xalign 0.5 yalign 0.9 text_size 40
