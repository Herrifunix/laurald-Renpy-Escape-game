# crafting_system.rpy

# Définition des recettes de craft
# Format: (nom_objet_A, nom_objet_B): nom_objet_resultat
# Les noms doivent correspondre exactement à l'attribut .name des objets Item
define craft_recipes = {
    ("Morceau de plan 1", "Morceau de plan 2"): "Plan complet",
    ("Manche en bois", "Tête de marteau"): "Marteau",
    ("Morceau de clé 1", "Morceau de clé 2"): "Clé rouillée",
    ("Lentille en verre", "Tube en laiton"): "Longue-vue",
}

# Fonction pour tenter de combiner deux objets
init python:
    def try_combine_items(item_a, item_b):
        if not item_a or not item_b:
            return
            
        # Créer les clés possibles (l'ordre ne doit pas importer)
        key1 = (item_a.name, item_b.name)
        key2 = (item_b.name, item_a.name)
        
        result_name = None
        
        if key1 in craft_recipes:
            result_name = craft_recipes[key1]
        elif key2 in craft_recipes:
            result_name = craft_recipes[key2]
            
        if result_name:
            # Succès : retirer les ingrédients et ajouter le résultat
            player_inventory.remove_item(item_a)
            player_inventory.remove_item(item_b)
            
            # Création de l'objet résultat (à adapter selon vos besoins d'image/desc)
            # Ici on fait une recherche simplifiée ou une création générique
            # Idéalement, vous devriez avoir une base de données d'objets ou une fonction factory
            new_item = create_item_by_name(result_name) 
            
            if new_item:
                player_inventory.add_item(new_item)
                renpy.notify("Objets combinés avec succès : %s créé !" % result_name)
                return True
        else:
            renpy.notify("Ces deux objets ne semblent pas aller ensemble.")
            
        return False

    # Fonction auxiliaire pour créer l'objet résultat (Exemple à personnaliser)
    def create_item_by_name(name):
        if name == "Plan complet":
            return Item("Plan complet", "Un plan reconstituÃ©.", "plan-parchemin.png", actions=[{"label": "Voir", "action": [Hide(),Jump("plan_cathedrale")]}])
        elif name == "Marteau":
            return Item("Marteau", "Un marteau solide. Utile pour briser quelque chose.", "coffre-mini.png")
        elif name == "Clé rouillée":
            return Item("Clé rouillée", "Une clé ancienne reconstituée à partir de deux bouts.", "cryptex-mini.png")
        elif name == "Longue-vue":
            return Item("Longue-vue", "Une longue-vue en laiton. Permet de voir au loin.", "morceau_1.png")
        return None

# Variable pour stocker le premier objet sélectionné pour le craft
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
            
            textbutton "Annuler" action [SetVariable("crafting_selected_item", None), Hide("crafting_selection_screen")] xalign 0.5
