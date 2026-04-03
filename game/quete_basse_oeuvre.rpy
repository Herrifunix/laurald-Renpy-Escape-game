# Définition du NPC "Agnès" (utilise l'image de moine par défaut si pas d'image)
image agnes = "images/Le_moine.webp"
define agnes_char = Character("Sœur Agnès",
                        image="agnes",
                        color="#4a7a8c",
                        ctc="click_indicator",
                        ctc_position="fixed")

default quete_clef_acceptee = False
default morceau_cle_donne = False

label basse_oeuvre:
    scene carolingienne with fade
    
    # Si le joueur n'a pas encore le morceau
    if not morceau_cle_donne:
        show agnes at center
        
        if not quete_clef_acceptee:
            agnes_char "Oh, bonjour [nom_du_perso]. Je cherche désespérément mes lunettes."
            agnes_char "Sans elles, je ne peux plus déchiffrer les manuscrits de la Basse Œuvre."
            agnes_char "Pourriez-vous me les ramener ? On dit qu'elles auraient été perdues près du Chœur."
            menu:
                "Je vais vous aider à les chercher.":
                    $ quete_clef_acceptee = True
                    agnes_char "Oh merci ! Que Dieu vous garde."
                "Je n'ai pas le temps, désolé.":
                    agnes_char "Je comprends... le temps de cette cathédrale est compté."
        else:
            # On vérifie si les lunettes sont dans l'inventaire
            python:
                has_lunettes = any(item.item_id == "lunettes_agnes" for item in player_inventory.get_items())

            if has_lunettes:
                agnes_char "Oh ! Mes lunettes ! Je n'y croyais plus."
                $ player_inventory.remove_item(next(item for item in player_inventory.get_items() if item.item_id == "lunettes_agnes"))
                agnes_char "Tenez, prenez ceci. C'est la moitié d'une vieille clé que j'ai trouvée dans les archives."
                agnes_char "Je n'ai jamais trouvé la seconde moitié, ni la serrure d'ailleurs..."
                
                python:
                    morceau_cle_1 = Item("Morceau de Clé 1", "La première moitié d'une ancienne clé.", "morceau_1.png", item_id="morceau_cle_1")
                    player_inventory.add_item(morceau_cle_1)
                
                $ morceau_cle_donne = True
                $ renpy.notify("Vous avez reçu 'Morceau de Clé 1'")
                
            else:
                agnes_char "Avez-vous retrouvé mes lunettes perdues près du chœur ?"
                agnes_char "Elles doivent être là-bas..."
    else:
        # Dialogue post-quête
        show agnes at center
        agnes_char "Merci encore pour mes lunettes. J'espère que cette moitié de clé vous sera utile."
    
    # On reste dans la pièce
    $ _game_menu_screen = None
label boucle_basse_oeuvre:
    pause
    jump boucle_basse_oeuvre

# Ecran permettant d'interagir avec le choeur et trouver les lunettes
screen salle_choeur():
    # Affichage des boutons d'interaction
    if quete_clef_acceptee and not morceau_cle_donne:
        # On vérifie si on n'a pas déjà les lunettes
        python:
            has_lunettes = any(item.item_id == "lunettes_agnes" for item in player_inventory.get_items())

        if not has_lunettes:
            # Un bouton presque caché (style hidden object ou texte simple pour l'exemple)
            textbutton "Ramasser de fines lunettes" action Jump("trouver_lunettes") xpos 0.6 ypos 0.8 text_size 20 text_color "#FFF" background "#aa6908"

    # Bouton vers d'autres salles ou ouverture directe de map si on veut

label trouver_lunettes:
    "Vous trouvez une paire de fines lunettes de lecture sous un banc de prière du chœur."
    python:
        lunettes_agnes = Item("Lunettes", "Des lunettes de lecture anciennes.", "morceau_1.png", item_id="lunettes_agnes")
        player_inventory.add_item(lunettes_agnes)
    $ renpy.notify("Objet ajouté : Lunettes")
    # On renvoie le joueur à la vue normale
    call screen salle_choeur
    jump boucle_choeur

