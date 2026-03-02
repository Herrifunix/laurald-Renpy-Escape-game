# Dans le fichier script.rpy

define e = Character("Eve")

# Fonction pour calculer la rotation
init python:
    def rotate_image(degrees):
        global rotation_angle
        rotation_angle += degrees
        return True

# L'écran pour afficher les images et permettre la rotation
screen rotating_images():
    default rotation_angle = 0
    
    frame:
        xalign 0.5
        yalign 0.5
        
        add "image_below.png" # Remplacez par le nom de votre image du dessous
        add "image_above.png" at Transform(rotate=rotation_angle, anchor=(0.5, 0.5)) # Remplacez par le nom de votre image du dessus

    vbox:
        xalign 0.5
        yalign 0.95
        
        textbutton "Rotate Left" action Function(rotate_image, -10)
        textbutton "Rotate Right" action Function(rotate_image, 10)

label start:
    $ rotation_angle = 0
    e "Bienvenue dans l'outil de rotation d'images."
    show screen rotating_images
    e "Utilisez les boutons pour faire pivoter l'image du dessus."
    return

