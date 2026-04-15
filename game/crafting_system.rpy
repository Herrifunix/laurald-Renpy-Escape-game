# crafting_system.rpy

# Définition des recettes de craft par ID
define craft_recipes = {
    ("morceau_carte_1", "morceau_carte_2"): "carte_complete",
    ("manche_bois", "tete_marteau"): "marteau",
    ("morceau_cle_1", "morceau_cle_2"): "cle_rouillee",
    ("lentille", "tube_laiton"): "longue_vue",
    ("bougie", "parchemin_mystere"): "parchemin_revele"
}

init python:
    def try_combine_items(item_a, item_b):
        if not item_a or not item_b:
            return

        # Utiliser les ID pour la combinaison
        key1 = (item_a.item_id, item_b.item_id)
        key2 = (item_b.item_id, item_a.item_id)

        result_id = None

        if key1 in craft_recipes:
            result_id = craft_recipes[key1]
        elif key2 in craft_recipes:
            result_id = craft_recipes[key2]

        if result_id:
            # Succès : retirer les ingrédients
            player_inventory.remove_item(item_a)
            player_inventory.remove_item(item_b)

            # Création du nouvel objet via ID
            new_item = create_item_by_id(result_id)

            if new_item:
                if result_id == "parchemin_revele":
                    # Lance le mini-jeu pour ce craft spécifique avant d'ajouter l'objet
                    renpy.call("start_message_cache", item_a.item_id, item_b.item_id, result_id)
                else:
                    player_inventory.add_item(new_item)
                    renpy.notify("Objets combinés avec succès : %s créé !" % new_item.name)
                return True
        else:
            renpy.notify("Ces deux objets ne semblent pas aller ensemble.")

        return False

    def create_item_by_id(item_id):
        if item_id == "carte_complete":
            return Item("Carte complète", "Une carte reconstituée à partir de deux morceaux.", "plan-parchemin.png", item_id="carte_complete", actions=[{"label": "Voir", "action": [Hide(),Jump("plan_cathedrale")]}])
        elif item_id == "marteau":
            return Item("Marteau", "Un marteau solide. Utile pour briser quelque chose.", Transform("marteau.png", zoom=0.5), item_id="marteau")
        elif item_id == "cle_rouillee":
            return Item("Clé rouillée", "Une clé ancienne reconstituée à partir de deux bouts.", "cryptex-mini.png", item_id="cle_rouillee")
        elif item_id == "longue_vue":
            return Item("Longue-vue", "Une longue-vue en laiton. Permet de voir au loin.", Transform("lunettes.png", zoom=0.33), item_id="longue_vue")
        elif item_id == "fragments_mystere":
            return Item("Fragments mystères", "Des morceaux d'un objet ancien. Il semble possible de les assembler.", "morceau_1.png", item_id="fragments_mystere", actions=[{"label": "Assembler", "action": [Hide("inventory_screen"), Call("start_assemblage", item_to_repair_id="fragments_mystere", repaired_item_id="artefact_repare")]}])
        elif item_id == "artefact_repare":
            return Item("Artefact réparé", "Un artefact ancien reconstitué avec succès à l'aide des fragments.", "coffre-mini.png", item_id="artefact_repare")
        elif item_id == "bougie":
            return Item("Bougie", "Une petite bougie allumée dégageant une douce chaleur.", "morceau_1.png", item_id="bougie")
        elif item_id == "parchemin_mystere":
            return Item("Parchemin vide", "Un vieux parchemin sans aucune écriture visible... à moins que ?", "images/message_cache/parchemin vide.png", item_id="parchemin_mystere")
        elif item_id == "parchemin_revele":
            return Item("Parchemin révélé", "Le message secret est désormais visible !", "images/message_cache/parchemin avec le message.png", item_id="parchemin_revele", actions=[{"label": "Lire", "action": [Hide("inventory_screen"), Show("image_viewer_screen", img="images/message_cache/parchemin avec le message.png")]}])
        return None

default crafting_selected_item = None

screen crafting_button_screen(item):
    textbutton "Combiner" action [SetVariable("crafting_selected_item", item), Show("crafting_selection_screen")]

screen crafting_selection_screen():
    modal True
    tag crafting_overlay

    add "#000a" # Fond assombri

    frame:
        xalign 0.5
        yalign 0.5
        padding (20, 20)

        vbox:
            spacing 20
            label "Sélectionnez un deuxième objet à combiner avec [crafting_selected_item.name]" xalign 0.5

            grid 4 3:
                spacing 10
                for item in player_inventory.get_items():
                    if item != crafting_selected_item:
                        imagebutton:
                            idle item.image
                            action [
                                Function(try_combine_items, crafting_selected_item, item),
                                SetVariable("crafting_selected_item", None),
                                Hide("crafting_selection_screen")
                            ]
                # Fill empty grid cells securely if length is < 12 based on RenPy requirement
                for i in range(12 - len([it for it in player_inventory.get_items() if it != crafting_selected_item])):
                    null

            textbutton "Annuler" action [SetVariable("crafting_selected_item", None), Hide("crafting_selection_screen")] xalign 0.5

