init python:
    # Variables globales pour le mini-jeu de l'orgue
    orgue_sequence = []
    orgue_melodies = {
        "melodie_secrete": ["Do", "Re", "Mi", "Do"],
        "melodie_magique": ["Mi", "Fa", "Sol", "Do", "Re"]
    }
    orgue_max_notes = 5

    def jouer_note(note):
        global orgue_sequence
        
        # Ajoute la note à la séquence
        orgue_sequence.append(note)
        
        # Garde seulement les dernières notes pour correspondre à la séquence la plus longue
        if len(orgue_sequence) > orgue_max_notes:
            orgue_sequence.pop(0)
            
        # Jouer un son ici (si des sons de notes sont disponibles)
        # renpy.play("audio/notes/" + note + ".ogg")
        
        # Vérifie si une mélodie correspond à la fin de la séquence actuelle
        for nom_melodie, melodie_secrete in orgue_melodies.items():
            longueur = len(melodie_secrete)
            if len(orgue_sequence) >= longueur:
                # Vérifie si les dernières notes correspondent
                if orgue_sequence[-longueur:] == melodie_secrete:
                    # Mélodie trouvée !
                    orgue_sequence = [] # Réinitialise
                    renpy.jump("orgue_" + nom_melodie)

screen salle_orgue():
    # Affiche la pièce de l'orgue. Cliquez sur le bouton central pour jouer
    # Ou un grand bouton transparent sur la zone du clavier si vous avez les coordonnées
    textbutton "Jouer de l'orgue" action Jump("jouer_orgue") text_size 40 xalign 0.5 yalign 0.5
    textbutton "Retour à la map" action Jump("map_retour") xalign 0.5 yalign 0.95

screen orgue_jouable():
    # Fond ou image de l'orgue
    add "orgues"
    
    # Variable pour stocker la note en train d'être pressée (pour le feedback visuel)
    default active_note = None

    if active_note is not None:
        timer 0.2 action SetScreenVariable("active_note", None)

    # Boutons textuels pour les touches du clavier (à ajuster visuellement plus tard)
    hbox:
        xalign 0.5
        yalign 0.8
        spacing 10
        
        # On allume le bouton en jaune clair ("#aa0") quand il est pressé, sinon fond foncé ("#333")
        textbutton "Do" action [SetScreenVariable("active_note", "Do"), Function(jouer_note, "Do")] text_size 30 text_color "#FFF" background (Solid("#aa0") if active_note == "Do" else Solid("#333")) hover_background (Solid("#aa0") if active_note == "Do" else Solid("#555")) padding (20, 40)
        textbutton "Re" action [SetScreenVariable("active_note", "Re"), Function(jouer_note, "Re")] text_size 30 text_color "#FFF" background (Solid("#aa0") if active_note == "Re" else Solid("#333")) hover_background (Solid("#aa0") if active_note == "Re" else Solid("#555")) padding (20, 40)
        textbutton "Mi" action [SetScreenVariable("active_note", "Mi"), Function(jouer_note, "Mi")] text_size 30 text_color "#FFF" background (Solid("#aa0") if active_note == "Mi" else Solid("#333")) hover_background (Solid("#aa0") if active_note == "Mi" else Solid("#555")) padding (20, 40)
        textbutton "Fa" action [SetScreenVariable("active_note", "Fa"), Function(jouer_note, "Fa")] text_size 30 text_color "#FFF" background (Solid("#aa0") if active_note == "Fa" else Solid("#333")) hover_background (Solid("#aa0") if active_note == "Fa" else Solid("#555")) padding (20, 40)
        textbutton "Sol" action [SetScreenVariable("active_note", "Sol"), Function(jouer_note, "Sol")] text_size 30 text_color "#FFF" background (Solid("#aa0") if active_note == "Sol" else Solid("#333")) hover_background (Solid("#aa0") if active_note == "Sol" else Solid("#555")) padding (20, 40)
        textbutton "La" action [SetScreenVariable("active_note", "La"), Function(jouer_note, "La")] text_size 30 text_color "#FFF" background (Solid("#aa0") if active_note == "La" else Solid("#333")) hover_background (Solid("#aa0") if active_note == "La" else Solid("#555")) padding (20, 40)
        textbutton "Si" action [SetScreenVariable("active_note", "Si"), Function(jouer_note, "Si")] text_size 30 text_color "#FFF" background (Solid("#aa0") if active_note == "Si" else Solid("#333")) hover_background (Solid("#aa0") if active_note == "Si" else Solid("#555")) padding (20, 40)
        
    textbutton "Quitter le clavier" action Jump("orgues") xalign 0.5 yalign 0.95

label orgue_melodie_secrete:
    "Vous avez joué la mélodie secrète !"
    "Un compartiment caché s'ouvre sur le pupitre de l'orgue."
    # Ajouter ici l'acquisition d'un item, ex: add_item("cle_secrete")
    jump jouer_orgue

label orgue_melodie_magique:
    "Vous avez joué la mélodie magique !"
    "Les tuyaux de l'orgue résonnent d'une lueur étrange..."
    # Autre événement
    jump jouer_orgue

label map_retour:
    hide screen orgue_jouable
    hide screen salle_orgue
    # Revenir à la vue initiale ou rouvrir la map :
    show screen plan_screen
    jump boucle_orgues
