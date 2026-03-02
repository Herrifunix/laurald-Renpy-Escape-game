# Ce script montre comment créer un projet de base dans Ren'Py

# Définir le nom du jeu et les informations de base
define config.name = "Les Secrets de la Cathédrale de Beauvais"
define config.version = "1.0"

# Création du type d'objet Item
init python:
    class Item:
        def __init__(self, name, image):
            self.name = name
            self.image = image
            
# définir les polices de caractères
init:
$ font_eveque = "OldLondon.ttf"

# Charger des images
image bg accueil = "images/portail-nord.png"
image bg perso = "images/perso.png"
image MOINE = "images/Le_moine.webp"
image EVEQUE = "images/eveque.png"
image bg cloitre = "images/cloitre.png"
image bg coffre = "images/coffre.png"
image parchemin1 = "images/parchemin1.png"

# Déclarer les variables globales pour le cadenas
default numb1 = 0
default numb2 = 0
default numb3 = 0
default numb4 = 0

# Initialisation de la variable
default dialeveque = False

# Déclarer les variables globales pour le criptext
default lettre1 = 1
default lettre2 = 1
define solution = [1, 2]  # Changez cela pour votre code de solution

# Définir des personnages
define a = Character("MOINE", color="#867f7d")
define b = Character("EVEQUE", color="#4c44c5", what_font="font_eveque")
#define b = Character("EVEQUE", color="#4c44c5")
define e = Character("NARRATEUR", color="#4c44c5")

# Charger les voix
define audio.voix_milon01 = "audio/milon1.ogg"
define audio.voix_milon02 = "audio/milon2.ogg"
define audio.voix_milon03 = "audio/milon3.ogg"

# Commencer le script principal
label start:

    # Jouer la musique de fond
    play music "audio/Solas-InnOfGoodFortune.mp3" fadein 1.0

    # Afficher l'arrière-plan et le personnage
    scene bg accueil
    show MOINE at right
    
    # Dialogue du personnage
    voice "audio/debut1.ogg"
    a "Ah, vous voilà enfin !" 
    voice "audio/debut2.ogg"
    a "Merci d'avoir répondu si rapidement à notre appel..."
    voice "audio/debut3.ogg"
    $ nom_du_perso = renpy.input("Rappelez-moi votre prénom s'il vous plaît")
    $ nom_du_perso = nom_du_perso.strip()
    define perso = Character("[nom_du_perso]", color="#000000")
    voice "audio/debut4.ogg"
    a "Merci [nom_du_perso]"
    voice "audio/debut5.ogg"
    a "Une situation des plus étranges nous préoccupe."
    voice "audio/debut6.ogg"
    a "Il y a un homme ici, vêtu comme un évêque, mais son identité nous échappe complètement !"
    voice "audio/debut7.ogg"
    a "Il est en proie à une grande agitation, comme si un tourment intérieur le rongeait."
    voice "audio/debut8.ogg"
    a "Il tourne sans cesse en rond dans le cloître, murmurant des paroles incompréhensibles."
    voice "audio/debut9.ogg"
    a "Malgré nos efforts, nous ne parvenons pas à apaiser son esprit troublé."
    voice "audio/debut10.ogg"
    a "Nous espérons que vous pourrez éclaircir ce mystère et ramener la paix en ces lieux."
    voice "audio/debut11.ogg"
    a "[nom_du_perso], ne perdez pas de temps, allez-y sans plus tarder et aidez-nous à résoudre cette énigme !"

    # Transition vers une autre scène
    scene bg cloitre with fade
    show EVEQUE at left
    voice "audio/milon1.ogg"
    b "Où sui-je ? Qui estes vos ?"
    e "Cet homme parle en vieux français !"
    perso "Je m'appelle [nom_du_perso], je suis venu pour vous aider. Vous êtes dans les jardins du cloître de la cathédrale Saint-Pierre de Beauvais."
    voice "audio/milon2.ogg"
    b "Ce n'est mie possible... J'estoie en train de travailler sur les plans de la cathédrale. Comment sui-je venu ci ?"
    perso "Il semble que vous ayez glissé dans une faille temporelle."

    # Réaction furieuse de Milon
    # show milon furious at left with dissolve

    # Transition pour la suite de l'histoire
    e "Milon de Nanteuil semble perplexe et furieux, mais il comprend qu'il doit coopérer pour trouver une solution à cette situation incroyable."
    voice "audio/milon3.ogg"
    b "Comment ? Une faille de temps ? Où est alée la somptueuse cathédralle qui devoit trespasser toutes les autres ?"    
    perso "Calmez-vous, Monseigneur. Nous devons comprendre ce qui s'est passé et comment vous ramener à votre époque."
    b "Certes, ce dont je me souviens est d'avoir trouvé ce parchemin..."
  
# Création de l'Item parchemin
    $ parchemin = Item("parchemin", "parchemin.png")
    call screen parchemin
    label parchemin_recupere:
    $ inventory = []
    show screen inventory
# Ajout du parchemin à la suite de la liste
    $ inventory.append(parchemin)
    show parchemin1 at center
    e "Les objets que vous récupérez, sont stockés dans votre inventaire, en haut de l'écran."
    b "et cest coffre."

    # Création de l'Item coffre
    $ coffre = Item("coffre", "coffre-mini.png")
    call screen coffre
    label coffre_recupere:

# Ajout du livre à la suite de la liste
    $ inventory.append(coffre)

    perso "Ce coffre est fermé, savez-vous comment l'ouvrir ?"
    b "Et comment le saurai-je ?"    

label dial_eveque:   
    menu:
        "Parlez-moi de la cathédrale.":
            jump cathedrale
        "Depuis combien de temps êtes-vous ici ?" :
            jump temps_ici
        "Pouvez-vous me rappeler les dates importantes ?" if dialeveque:
            jump dates_importantes
        "Je vais tenter de saisir un code." : 
            jump coffre1

label cathedrale:
    b "La cathédral karolingienne ere antiane, datant sanz doute de la seconde moitié du Xe siècle."
    perso "C'est-à-dire 950 ! Elle est vraiment très ancienne."
    b "C'est por ce que il faloit en edifier une novele, en le novel estil de l'art franceis"
    b "et nous avon lancé le chantier, cest an meïsme !"
    jump dial_eveque

label temps_ici:
    b "Je suis chanoine dès l'an mil deux cens et six, c'est à dire despuis dix et neuf ans."
    b "Puiz prévost du chapitre dès l'an mil deux cens et sept et esleu évesque de Beauvais en l'an mil deux cens et dis set."
    perso "Vous avez donc vu beaucoup de choses se passer ici."
    b "Oïl, et chascune année a aporté son lot de défis et de décisions importantes."
    b "Chascune date que je vos ai mentionée est importante. Peut-estre i trouverez-vos la clé por ouvrir le coffre."
    $ dialeveque = True
    jump dial_eveque

label dates_importantes:
    b "Bien sûr. 1206, 1207, 1217, et surtout, 1225."
    perso "Pourquoi surtout 1225?"
    b "Enfin, c'est en ceste année mil deux cens vingt et cinq, qu'avec le Chapitre nous avon décidé de reprendre la construction du nouvel ovre."
    perso "Cela semble être une année clé."
    jump dial_eveque

label coffre1:
    scene bg coffre with fade
    hide EVEQUE
    #call screen cryptex2
    call screen cadenas

#Coffre ouvert
    label coffre_ouvert:
    show EVEQUE
    b "BRAVO"

# Fin de la scène
    return

