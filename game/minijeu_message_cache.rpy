# game/minijeu_message_cache.rpy

init python:
    import pygame

    class InvisibleInk(renpy.Displayable):
        def __init__(self, empty_img, revealed_img, grid_size=40, brush_size=2, **kwargs):
            super(InvisibleInk, self).__init__(**kwargs)
            self.empty_img = renpy.displayable(empty_img)
            self.revealed_img = renpy.displayable(revealed_img)
            self.grid_size = grid_size
            self.brush_size = brush_size
            self.revealed_cells = set()
            self.is_completed = False
            self.total_cells_approx = 0

        def render(self, width, height, st, at):
            empty_r = renpy.render(self.empty_img, width, height, st, at)
            revealed_r = renpy.render(self.revealed_img, width, height, st, at)
            
            rv = renpy.Render(empty_r.width, empty_r.height)
            rv.blit(empty_r, (0, 0))
            
            # Draw revealed chunks
            grid = self.grid_size
            
            # Calculer le nombre total de cellules (approx) une seule fois
            if self.total_cells_approx == 0:
                self.total_cells_approx = (empty_r.width // grid) * (empty_r.height // grid)
                
            for (cx, cy) in self.revealed_cells:
                x = cx * grid
                y = cy * grid
                w = min(grid, revealed_r.width - x)
                h = min(grid, revealed_r.height - y)
                if w > 0 and h > 0:
                    chunk = revealed_r.subsurface((x, y, w, h))
                    rv.blit(chunk, (x, y))
                    
            return rv

        def event(self, ev, x, y, st):
            # Ne fait rien si la position de la souris est hors de la zone du parchemin
            if x < 0 or y < 0 or x > self.total_cells_approx * self.grid_size:
                return None
                
            grid = self.grid_size
            added = False
            
            cx = int(x) // grid
            cy = int(y) // grid
            
            # Révèle une zone autour de la souris en fonction de brush_size
            for dx in range(-self.brush_size, self.brush_size + 1):
                for dy in range(-self.brush_size, self.brush_size + 1):
                    # Forme grossièrement ronde/losange
                    if abs(dx) + abs(dy) <= self.brush_size + 1:
                        cell = (cx + dx, cy + dy)
                        # Pour éviter de stocker des cellules hors limites (moins de ressources)
                        if cell[0] >= 0 and cell[1] >= 0:
                            if cell not in self.revealed_cells:
                                self.revealed_cells.add(cell)
                                added = True
                        
            if added:
                renpy.redraw(self, 0)
                
                # Victoire si 60% de la zone est révélée
                if self.total_cells_approx > 0:
                    if len(self.revealed_cells) > (self.total_cells_approx * 0.6) and not self.is_completed:
                        self.is_completed = True
                        return True # Renvoie True à l'_return de l'écran

            return None


screen minijeu_message_cache():
    modal True
    tag minijeu_message

    add "#000e" # Fond sombre
    
    text "Révélation à la bougie" size 50 xalign 0.5 ypos 30 font "OldLondon.ttf" color "#ffcc00"
    text "Passez la flamme (votre souris) sur le parchemin pour faire apparaître l'encre invisible grâce à la chaleur." size 24 xalign 0.5 ypos 90 font "OldLondon.ttf" color "#aaa"

    # L'affichage de notre Custom Displayable (le parchemin interactif)
    frame:
        xalign 0.5
        yalign 0.5
        background None
        # On définit une taille fixe si besoin ou on laisse s'adapter à l'image
        add InvisibleInk("images/message_cache/parchemin vide.png", "images/message_cache/parchemin avec le message.png", grid_size=20, brush_size=3)

    textbutton "Quitter" action Return(False):
        xalign 0.5
        yalign 0.95
        text_color "#ff0000"

label start_message_cache(item_a_id=None, item_b_id=None, result_id=None):
    call screen minijeu_message_cache
    
    if _return == True:
        renpy.notify("Le message complet est apparu !")
        if result_id:
            # On donne le parchemin finalement révélé
            python:
                new_item = create_item_by_id(result_id)
                player_inventory.add_item(new_item)
    else:
        renpy.notify("Vous avez arrêté de chauffer le parchemin.")
        if item_a_id and item_b_id:
            # Le joueur a annulé le craft, on remet les objets dans l'inventaire
            python:
                item_1 = create_item_by_id(item_a_id)
                item_2 = create_item_by_id(item_b_id)
                player_inventory.add_item(item_1)
                player_inventory.add_item(item_2)
        
    return
