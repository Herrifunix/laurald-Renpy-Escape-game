# myscreens.rpy

# Définir l'écran pour le cadenas
screen lock_screen():
    modal True

    frame:
        xalign 0.5
        yalign 0.5
        has vbox

        text "Entrez le code pour déverrouiller :"
        
        # Input fields for the code
        hbox:
            spacing 10

            input id "digit1" length 1 allow "0123456789" default "0"
            input id "digit2" length 1 allow "0123456789" default "0"
            input id "digit3" length 1 allow "0123456789" default "0"
            input id "digit4" length 1 allow "0123456789" default "0"

        textbutton "Submit":
            action [Function(check_code), Hide("lock_screen")]

# Fonction pour vérifier le code
init python:
    def check_code():
        # Obtenir les valeurs des champs d'entrée
        digit1 = renpy.get_widget("lock_screen", "digit1").value
        digit2 = renpy.get_widget("lock_screen", "digit2").value
        digit3 = renpy.get_widget("lock_screen", "digit3").value
        digit4 = renpy.get_widget("lock_screen", "digit4").value
        
        # Combiner les chiffres en un seul code
        code = digit1 + digit2 + digit3 + digit4
        
        # Vérifier si le code est correct
        if code == "1225":
            renpy.say(e, "Le code est correct. Le cadenas est déverrouillé !")
        else:
            renpy.say(e, "Le code est incorrect. Veuillez réessayer.")

