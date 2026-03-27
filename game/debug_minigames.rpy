# debug_minigames.rpy

# Active a la demande pour tester les mini-jeux sans avancer l'histoire.
default debug_minigame_mode = False

# Ajouter de nouveaux mini-jeux ici au format (Nom, Label).
default debug_minigame_registry = [
    ("Coffre (code 1225)", "debug_test_coffre"),
    ("Cryptex (mot BABYL)", "debug_test_cryptex"),
    ("Puzzle (pieces a remettre)", "puzzle"),
    ("Puzzle 2 (Tour lanterne)", "debug_test_puzzle_2"),
    ("Trouver les objets", "debug_test_find_objects"),
]

default debug_find_objects_state = {
    "coffre": False,
    "cryptex": False,
    "rosace": False,
}

# Donnees du mini-jeu "trouver les objets".
default debug_find_objects_data = [
    {
        "key": "coffre",
        "label": "Coffre",
        "image": "images/coffre-mini.png",
        "xpos": 730,
        "ypos": 470,
        "zoom": 0.35,
    },
    {
        "key": "cryptex",
        "label": "Cryptex",
        "image": "images/cryptex-mini.png",
        "xpos": 280,
        "ypos": 535,
        "zoom": 0.28,
    },
    {
        "key": "rosace",
        "label": "Rosace",
        "image": "images/rosace.png",
        "xpos": 980,
        "ypos": 130,
        "zoom": 0.12,
    },
]

screen debug_minigames():
    tag menu

    use game_menu(_("Debug mini-jeux"), scroll="viewport"):

        vbox:
            spacing 12

            text "Lancer un mini-jeu pour test :"

            for minigame_name, minigame_label in debug_minigame_registry:
                textbutton minigame_name action Call(minigame_label)

screen debug_find_objects():
    modal True

    add "images/cloitre.png"

    $ remaining_objects = [obj["label"] for obj in debug_find_objects_data if not debug_find_objects_state[obj["key"]]]

    frame:
        xalign 0.5
        yalign 0.03
        xpadding 20
        ypadding 10
        background "#0009"
        text "Trouve les objets caches dans l'image"

    frame:
        xalign 0.02
        yalign 0.12
        xpadding 20
        ypadding 20
        background "#0009"
        vbox:
            spacing 8
            text "Objets restants : [len(remaining_objects)]"
            if remaining_objects:
                for object_name in remaining_objects:
                    text "- [object_name]"
            else:
                text "Tous les objets ont ete trouves."

    for obj in debug_find_objects_data:
        imagebutton:
            idle Transform(obj["image"], zoom=obj["zoom"], alpha=0.20)
            hover Transform(obj["image"], zoom=obj["zoom"], alpha=1.0)
            xpos obj["xpos"]
            ypos obj["ypos"]
            action If(debug_find_objects_state[obj["key"]], NullAction(), [SetDict(debug_find_objects_state, obj["key"], True), Notify("[obj['label']] trouve")])

    if all(debug_find_objects_state.values()):
        frame:
            xalign 0.5
            yalign 0.92
            xpadding 18
            ypadding 10
            background "#0009"
            hbox:
                spacing 12
                text "Bravo, tous les objets ont ete trouves !"
                textbutton "Terminer" action Return(True)

    textbutton "Quitter":
        xalign 0.98
        yalign 0.03
        action Return(False)

label debug_test_coffre:
    $ debug_minigame_mode = True
    $ numb1 = 0
    $ numb2 = 0
    $ numb3 = 0
    $ numb4 = 0
    call screen inventory_coffre1
    $ debug_minigame_mode = False
    return

label debug_test_cryptex:
    $ debug_minigame_mode = True
    $ lettre1 = 1
    $ lettre2 = 1
    $ lettre3 = 1
    $ lettre4 = 1
    $ lettre5 = 1
    call screen inventory_cryptex
    $ debug_minigame_mode = False
    return

label debug_test_find_objects:
    $ debug_find_objects_state = {
        "coffre": False,
        "cryptex": False,
        "rosace": False,
    }

    $ _found_all_objects = renpy.call_screen("debug_find_objects")

    if _found_all_objects:
        $ renpy.notify("Mini-jeu Trouver les objets reussi")

    return

label debug_test_puzzle_2:
    call puzzle_2
    return
