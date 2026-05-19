# game/minigames/minijeu_message_cache.rpy

init python:
    import pygame
    import math

    class InvisibleInk(renpy.Displayable):
        """
        Parchemin interactif : la flamme (le curseur) chauffe le papier.
        La chaleur s'accumule pixel par pixel dans un masque, ce qui revele
        l'encre invisible en douceur et laisse une trace de brulure brune.
        """

        SCORE_COLS = 32
        SCORE_ROWS = 24
        SCORE_HEAT_THRESHOLD = 120.0   # chaleur a partir de laquelle une case compte
        WIN_FRACTION = 0.60            # parite avec l'ancien seuil de victoire
        FLAME_REDRAW = 1.0 / 30.0      # rafraichissement continu pour le scintillement

        def __init__(self, empty_img, revealed_img, brush_radius=60, brush_strength=120, **kwargs):
            super(InvisibleInk, self).__init__(**kwargs)
            self.empty_path = empty_img
            self.revealed_path = revealed_img
            self.brush_radius = brush_radius
            self.brush_strength = brush_strength

            # Ressources chargees paresseusement au premier rendu.
            self.loaded = False
            self.size = None
            self.empty_surf = None
            self.message_surf = None
            self.heat_surf = None
            self.brush_stamp = None

            # Composite mis en cache, recalcule seulement quand la chaleur change.
            self.parchment_cache = None
            self.heat_dirty = True

            # Progression : chaleur accumulee par case d'une grille invisible.
            self.cell_heat = {}
            self.revealed_count = 0
            self.win_count = self.SCORE_COLS * self.SCORE_ROWS * self.WIN_FRACTION

            self.is_completed = False
            self.cursor_xy = None

        def _ensure_loaded(self):
            if self.loaded:
                return

            self.empty_surf = renpy.load_surface(self.empty_path)
            self.message_surf = renpy.load_surface(self.revealed_path)
            self.size = self.empty_surf.get_size()

            # Masque de chaleur : son canal alpha contient la chaleur (0-255).
            self.heat_surf = pygame.Surface(self.size, pygame.SRCALPHA)
            self.heat_surf.fill((255, 255, 255, 0))

            self.brush_stamp = self._build_brush(self.brush_radius, self.brush_strength)
            self.loaded = True

        def _build_brush(self, radius, strength):
            # Tampon radial doux : alpha fort au centre, nul sur les bords.
            size = radius * 2
            stamp = pygame.Surface((size, size), pygame.SRCALPHA)
            stamp.fill((255, 255, 255, 0))
            for i in range(radius, 0, -1):
                t = i / float(radius)
                a = int(strength * (1.0 - t * t))
                if a > 0:
                    pygame.draw.circle(stamp, (255, 255, 255, a), (radius, radius), i)
            return stamp

        def _stamp_heat(self, x, y):
            r = self.brush_radius
            self.heat_surf.blit(self.brush_stamp, (x - r, y - r),
                                special_flags=pygame.BLEND_RGBA_ADD)
            self._mark_score(x, y)

        def _mark_score(self, x, y):
            # Grille invisible de progression : aucune lecture de pixels.
            w, h = self.size
            cw = w / float(self.SCORE_COLS)
            ch = h / float(self.SCORE_ROWS)
            r = self.brush_radius
            r2 = r * r
            strength = self.brush_strength
            threshold = self.SCORE_HEAT_THRESHOLD

            for gx in range(self.SCORE_COLS):
                ccx = (gx + 0.5) * cw
                if abs(ccx - x) > r:
                    continue
                for gy in range(self.SCORE_ROWS):
                    ccy = (gy + 0.5) * ch
                    d2 = (ccx - x) ** 2 + (ccy - y) ** 2
                    if d2 > r2:
                        continue
                    t = (d2 ** 0.5) / r
                    contrib = strength * (1.0 - t * t)
                    key = (gx, gy)
                    prev = self.cell_heat.get(key, 0.0)
                    new = min(255.0, prev + contrib)
                    self.cell_heat[key] = new
                    if prev < threshold <= new:
                        self.revealed_count += 1

        def _composite_parchment(self):
            # BLEND_RGBA_MULT contre le masque blanc/chaleur : alpha *= chaleur/255.
            mult = pygame.BLEND_RGBA_MULT

            cache = pygame.Surface(self.size, pygame.SRCALPHA)
            cache.blit(self.empty_surf, (0, 0))

            # Message cache, revele proportionnellement a la chaleur.
            revealed = pygame.Surface(self.size, pygame.SRCALPHA)
            revealed.blit(self.message_surf, (0, 0))
            revealed.blit(self.heat_surf, (0, 0), special_flags=mult)
            cache.blit(revealed, (0, 0))

            # Trace de brulure brune par-dessus : teinte la zone chauffee.
            scorch = pygame.Surface(self.size, pygame.SRCALPHA)
            scorch.fill((92, 50, 22, 130))
            scorch.blit(self.heat_surf, (0, 0), special_flags=mult)
            cache.blit(scorch, (0, 0))

            return cache

        def _render_flame(self, st):
            fw, fh = 96, 140
            cx = fw // 2
            base_y = fh - 16
            surf = pygame.Surface((fw, fh), pygame.SRCALPHA)

            # Halo de lumiere chaude (degrade radial doux).
            glow_pulse = 0.85 + 0.15 * math.sin(st * 6.5)
            glow_r = max(1, int(46 * glow_pulse))
            glow_cy = base_y - 30
            for gr in range(glow_r, 0, -1):
                t = gr / float(glow_r)
                a = int(70 * (1.0 - t) * (1.0 - t))
                if a > 0:
                    pygame.draw.circle(surf, (255, 150, 60, a), (cx, glow_cy), gr)

            # Scintillement de la flamme.
            sway = math.sin(st * 11.0) * 3.2 + math.sin(st * 23.0) * 1.4
            stretch = 1.0 + 0.16 * math.sin(st * 17.0)
            flick = 0.92 + 0.08 * math.sin(st * 31.0)

            # Corps : trois gouttes empilees, de l'exterieur vers le coeur.
            layers = [
                ((240, 115, 25, 220), 18.0, 76.0),
                ((252, 205, 60, 240), 12.0, 56.0),
                ((255, 252, 222, 255), 6.0, 32.0),
            ]
            for color, half_w, height in layers:
                hw = half_w * flick
                hgt = height * stretch
                mid_y = base_y - hgt * 0.52
                pts = [
                    (int(cx - hw), base_y),
                    (int(cx - hw * 0.5), int(mid_y + sway * 0.25)),
                    (int(cx + sway), int(base_y - hgt)),
                    (int(cx + hw * 0.5), int(mid_y + sway * 0.25)),
                    (int(cx + hw), base_y),
                ]
                pygame.draw.polygon(surf, color, pts)

            return surf, fw, fh, base_y

        def render(self, width, height, st, at):
            self._ensure_loaded()
            w, h = self.size

            if self.heat_dirty or self.parchment_cache is None:
                self.parchment_cache = self._composite_parchment()
                self.heat_dirty = False

            rv = renpy.Render(w, h)
            out = rv.canvas().get_surface()
            out.blit(self.parchment_cache, (0, 0))

            if self.cursor_xy is not None:
                flame, fw, fh, base_y = self._render_flame(st)
                mx, my = self.cursor_xy
                out.blit(flame, (mx - fw // 2, my - base_y))

            # Rafraichissement continu : la flamme scintille meme curseur immobile.
            renpy.redraw(self, self.FLAME_REDRAW)
            return rv

        def event(self, ev, x, y, st):
            if self.size is None:
                return None

            w, h = self.size
            inside = (0 <= x < w) and (0 <= y < h)

            if ev.type == pygame.MOUSEMOTION:
                if inside:
                    ix, iy = int(x), int(y)
                    self.cursor_xy = (ix, iy)
                    self._stamp_heat(ix, iy)
                    self.heat_dirty = True
                    renpy.redraw(self, 0)

                    # Victoire quand 60% de la zone est suffisamment chauffee.
                    if not self.is_completed and self.revealed_count >= self.win_count:
                        self.is_completed = True
                        return True
                elif self.cursor_xy is not None:
                    self.cursor_xy = None
                    renpy.redraw(self, 0)

            return None


screen minijeu_message_cache():
    modal True
    tag minijeu_message

    add "#000e" # Fond sombre

    text "Révélation à la bougie" size 50 xalign 0.5 ypos 30 font "OldLondon.ttf" color "#ffcc00"
    text "Promenez lentement la flamme sur le parchemin : la chaleur révèle l'encre et laisse une trace de brûlure." size 24 xalign 0.5 ypos 90 font "OldLondon.ttf" color "#aaa"

    # L'affichage de notre Custom Displayable (le parchemin interactif)
    frame:
        xalign 0.5
        yalign 0.5
        background None
        # On définit une taille fixe si besoin ou on laisse s'adapter à l'image
        add InvisibleInk("images/message_cache/parchemin vide.png", "images/message_cache/parchemin avec le message.png", brush_radius=60, brush_strength=120)

    textbutton "Quitter" action Return(False):
        xalign 0.5
        yalign 0.95
        text_color "#ff0000"

label start_message_cache(item_a_id=None, item_b_id=None, result_id=None):
    call screen minijeu_message_cache

    if _return == True:
        $ renpy.notify("Le message complet est apparu !")
        if result_id:
            # On donne le parchemin finalement révélé
            python:
                new_item = create_item_by_id(result_id)
                player_inventory.add_item(new_item)
    else:
        $ renpy.notify("Vous avez arrêté de chauffer le parchemin.")
        if item_a_id and item_b_id:
            # Le joueur a annulé le craft, on remet les objets dans l'inventaire
            python:
                item_1 = create_item_by_id(item_a_id)
                item_2 = create_item_by_id(item_b_id)
                player_inventory.add_item(item_1)
                player_inventory.add_item(item_2)

    return
