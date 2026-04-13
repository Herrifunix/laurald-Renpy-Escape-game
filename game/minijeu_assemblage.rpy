# game/minijeu_assemblage.rpy

init -1 python:
    # Fonction appelée à chaque fois qu'on lâche une pièce
    def check_assemblage_drag(drags, drop):
        if not drop:
            return

        piece = drags[0]
        # La zone de dépôt correspondante doit avoir le nom "zone_" + nom de la pièce
        if drop.drag_name == "zone_" + piece.drag_name:
            # Snapper la pièce au bon endroit
            piece.snap(drop.x, drop.y)
            piece.draggable = False # On la bloque pour signifier qu'elle est bien placée
            
            # Ajouter la pièce dans la globale traceuse
            store.pieces_placed.add(piece.drag_name)
            
            # Si toutes les pièces sont placées
            if len(store.pieces_placed) >= store.total_pieces:
                return True # Ça retourne True pour valider la victoire
        return

screen assemblage_screen():
    modal True
    tag minijeu_assemblage

    # Fond noir translucide
    add "#000c"

    frame:
        xalign 0.5
        yalign 0.5
        # zone de 1000 x 700 pixels
        xysize (1000, 700)
        background "#222" # on peut remplacer par une image de plateau
        
        text "Assemblez les fragments" xalign 0.5 ypos 20 size 40 font "OldLondon.ttf" color "#fff"
        text "Faites glisser les formes de couleur au bon emplacement gris." xalign 0.5 ypos 70 size 20 font "OldLondon.ttf" color "#aaa"
        
        draggroup:
            # ==== Les 4 Zones de Dépôt ====
            # Forme un carré 2x2 centré
            drag:
                drag_name "zone_piece_1"
                draggable False
                droppable True
                xpos 300 ypos 200
                child Solid("#ffffff33", xysize=(150, 150))
            drag:
                drag_name "zone_piece_2"
                draggable False
                droppable True
                xpos 470 ypos 200
                child Solid("#ffffff33", xysize=(150, 150))
            drag:
                drag_name "zone_piece_3"
                draggable False
                droppable True
                xpos 300 ypos 370
                child Solid("#ffffff33", xysize=(150, 150))
            drag:
                drag_name "zone_piece_4"
                draggable False
                droppable True
                xpos 470 ypos 370
                child Solid("#ffffff33", xysize=(150, 150))
                
            # ==== Les 4 Pièces à glisser ====
            drag:
                drag_name "piece_1"
                draggable True
                droppable False
                dragged check_assemblage_drag
                xpos 80 ypos 150
                child Solid("#e74c3c", xysize=(150, 150))
            drag:
                drag_name "piece_2"
                draggable True
                droppable False
                dragged check_assemblage_drag
                xpos 750 ypos 250
                child Solid("#3498db", xysize=(150, 150))
            drag:
                drag_name "piece_3"
                draggable True
                droppable False
                dragged check_assemblage_drag
                xpos 100 ypos 450
                child Solid("#2ecc71", xysize=(150, 150))
            drag:
                drag_name "piece_4"
                draggable True
                droppable False
                dragged check_assemblage_drag
                xpos 780 ypos 450
                child Solid("#f1c40f", xysize=(150, 150))

        textbutton "Fermer" action Return(False):
            xalign 0.5
            yalign 0.95
            text_color "#ff0000"

label start_assemblage(item_to_repair_id, repaired_item_id):
    # Désélectionner l'item
    $ selected_item = None
    
    # Inititalisation du minijeu
    $ store.pieces_placed = set()
    $ store.total_pieces = 4
    
    call screen assemblage_screen()
    
    if _return == True:
        # Succès : retirer l'item brisé et ajouter le réparé
        python:
            for it in player_inventory.get_items():
                if it.item_id == item_to_repair_id:
                    player_inventory.remove_item(it)
                    break
            
            repaired_item = create_item_by_id(repaired_item_id)
            if repaired_item:
                player_inventory.add_item(repaired_item)
                renpy.notify("Objet réparé avec succès !")
    else:
        # Annulé, on renvoie à l'accueil ou on remet l'inventaire
        $ renpy.notify("Assemblage annulé.")
    
    # Redonner la main
    return
