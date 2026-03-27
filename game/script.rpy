# Ce script montre comment créer un projet de base dans Ren'Py

# Définir le nom du jeu et les informations de base
define config.name = "Les Secrets de la Cathédrale de Beauvais"
define config.version = "1.0"

# Création du type d'objet Item
# Inventaire test 2
# Déclaration de la classe pour les objets de l'inventaire
init python:
    class Item:
        def __init__(self, name, description, image, actions=[]):
            self.name = name
            self.description = description
            self.image = image
            self.actions = actions

# Classe pour gérer l'inventaire du joueur
init python:
    class Inventory:
        def __init__(self):
            self.items = []

        def add_item(self, item):
            self.items.append(item)

        def remove_item(self, item):
            if item in self.items:
                self.items.remove(item)

        def get_items(self):
            return self.items

# Variable globale pour l'inventaire du joueur
default player_inventory = Inventory()
default selected_item = None

# vbox  et frame transparentes
style transparent_vbox:
    background None
    xpadding 0
    ypadding 0
    xmargin 0
    ymargin 0
    
style transparent_frame:
    background None
    xpadding 0
    ypadding 0
    xmargin 0
    ymargin 0
# définir les polices de caractères
init:
    $ my_font = "germanica.ttf"
    $ font_eveque = "OldLondon.ttf"

# Charger des images
image bg bureau = "images/bureau.png"
image dim = "#0008"
image bg accueil = "images/portail-nord.png"
image bg perso = "images/perso.png"
image bg kiosque = "images/kiosque.png"
image MOINE = "images/Le_moine.webp"
image EVEQUE = "images/eveque.png"
image Alexandre = "images/alexandre.png"
image Alexandre etonne = "images/alexandre etonne.png"
image EVEQUEdonne = "images/eveque2.png"
image bg cloitre = "images/cloitre.png"
image bg coffre = "images/coffre.png"
image carolingienne = "images/carolingienne.png"
image artfrancais = "images/artfrancais.png"
image parchemin1 = "images/parchemin1.png"
image coffre-taille-normale = "images/coffre-taille-normale.png"
image rosace = "images/rosace.png"
image horloge = "images/horloge.png"
image horloge_astro = "images/horloge-astronomique.png"
image horloge_astro_ouvert = "images/horloge-astronomique-ouvert.png"
image orgues = "images/orgues.png"
image choeur = "images/choeur.png"
image cryptext_mini = "images/cryptex-mini.png"
image plan_parchemin = "images/plan-parchemin.png"
image morceau_1 = "images/morceau_1.png"
image coffre_ouvert = "/images/coffre-taille-normale-ouvert.png"
image plan_cathedrale_grand = "/images/plan_cathedrale_grand.png"
# Charger image Click to Continue
image click_indicator:
    yalign 0.925 xalign 0.81
    "images/click1.png"
    pause 0.25
    "images/click2.png"
    pause 0.25
    repeat

# Déclarer les variables globales pour le cadenas
default numb1 = 0
default numb2 = 0
default numb3 = 0
default numb4 = 0

# Initialisation de la variable
default dialeveque = False # Indicateur pour avoir plus d'action dans le dial avec l'éveque 1re scene A
default dialeveque0 = False # Indicateur pour avoir plus d'action dans le dial avec l'éveque 1re scene B
define clef_horloge = False # Indicateur de test pour la clef de l'horloge astronomique pour ouvrir la grille
define parchemin1_vu = 0
default cryptex_taken = False  # Indicateur si le cryptex a été pris
default plan_taken = False  # Indicateur si le plan a été pris
default morceau_taken = False  # Indicateur si le morceau a été pris
default morceaux_parchemin = 0 # Compteur pour la quantité de morceaux de parchemin
default puzzle2_time_limit = 300
default puzzle2_deadline = 0.0
default puzzle2_time_left = 0

# Action personnalisée pour permuter la valeur de clef_horloge
init python:
    def toggle_key():
        global clef_horloge
        clef_horloge = not clef_horloge


# Déclarer les variables globales pour le criptext
default lettre1 = 1
default lettre2 = 1
default lettre3 = 1
default lettre4 = 1
default lettre5 = 1

# Définir des personnages
define a = Character("Moine",
                    image="moine",
                    color="#775b26",
                    ctc="click_indicator",
                    ctc_position="fixed")

define b = Character("Évêque Milon de Nanteuil",
                    image="eveque",
                    color="#7b35a3",
                    ctc="click_indicator",
                    ctc_position="fixed")

define e = Character("Narrateur",
                    image="narrateur",
                    color="#18005a",
                    ctc="click_indicator",
                    ctc_position="fixed")

define alex = Character("Alexandre",
                    image="alexandre",
                    color="#cf1212",
                    ctc="click_indicator",
                    ctc_position="fixed")

#définir angle de rotation pour image
init python:
    # Variables pour gérer l'angle de rotation
    angle = 15

    # Fonction pour faire pivoter l'image
    def rotate_clockwise():
        global angle
        angle += 30
        if angle >= 360:
            angle -= 360

    def rotate_counterclockwise():
        global angle
        angle -= 30
        if angle < 0:
            angle += 360

# Dialogue d'action
# message d'alexandre pour dire qu'il faut une clef pour accéder à l'horloge :
# Fonction pour afficher le dialogue
init python:
    def afficher_dialogue():
        renpy.say(alex, "Désolé {nom_du_perso}, il faut une clef pour passer.")

# Commencer le script principal
label start:

    # introduire une vidéo d'introduction
    stop music
    play movie "images/cloitre_faille.webm"
    # Attend la fin de la vidéo avant de continuer
    window hide
    pause
    stop movie

    # Afficher l'arrière-plan et le personnage
    scene bg accueil
    show MOINE at right
    # Jouer la musique de fond
    play music "audio/Solas-InnOfGoodFortune.mp3" fadein 1.0

    # Dialogue du personnage
    voice "audio/debut1.ogg"
    a "Ah, vous voilà enfin !{nw}" 
    voice "audio/debut2.ogg"
    a "Merci d'avoir répondu si rapidement à notre appel...{nw}"
    voice "audio/debut3.ogg"
    $ nom_du_perso = renpy.input("Rappelez-moi votre prénom s'il vous plaît")
    $ nom_du_perso = nom_du_perso.strip()
    define perso = Character("[nom_du_perso]",
                            image="perso",
                            color="#000000",
                            ctc="click_indicator",
                            ctc_position="fixed")
    voice "audio/debut4.ogg"
    a "ah merci [nom_du_perso]{nw}"
    voice "audio/debut5.ogg"
    a "Une situation des plus étranges nous préoccupe.{nw}"
    voice "audio/debut6.ogg"
    a "Il y a un homme ici, vêtu comme un évêque, mais son identité nous échappe complètement !{nw}"
    voice "audio/debut7.ogg"
    a "Il est en proie à une grande agitation, comme si un tourment intérieur le rongeait.{nw}"
    voice "audio/debut8.ogg"
    a "Il tourne sans cesse en rond dans le cloître, murmurant des paroles incompréhensibles.{nw}"
    voice "audio/debut9.ogg"
    a "Malgré nos efforts, nous ne parvenons pas à apaiser son esprit troublé.{nw}"
    voice "audio/debut10.ogg"
    a "Nous espérons que vous pourrez éclaircir ce mystère et ramener la paix en ces lieux.{nw}"
    voice "audio/debut11.ogg"
    a "[nom_du_perso], ne perdez pas de temps, allez-y sans plus tarder et aidez-nous à résoudre cette énigme !"

    # Transition vers une autre scène
    scene bg cloitre with fade
    show EVEQUE at left
    voice "audio/milon1.ogg"
    b "{size=+10}{font=OldLondon.ttf}Où sui-je ? Qui estes vos ?{/font}\n{/size}{size=-7}{i}Où suis-je ? Qui êtes-vous ?{/i}{/size}"
    voice "audio/e-vieux-francais.mp3"
    e "Cet homme parle en vieux français !"
    perso "Je m'appelle [nom_du_perso], je suis venu pour vous aider. Vous êtes dans les jardins du cloître de la cathédrale Saint-Pierre de Beauvais."
    voice "audio/milon2.ogg"
    b "{size=+10}{font=OldLondon.ttf}J'estoie en train de travailler sur les plans de la cathédrale. Comment sui-je venu ci ?{/font}\n{/size}{size=-7} {i}J'étais en train de travailler sur les plans de la cathédrale. Comment suis-je venu ici ?{/i}{/size}{nw}"
    perso "Il semble que vous ayez glissé dans une faille temporelle."

    # Réaction furieuse de Milon
    # show milon furious at left with dissolve

    # Transition pour la suite de l'histoire
    voice "audio/e-2.mp3"
    e "Milon de Nanteuil semble perplexe et furieux, mais il comprend qu'il doit coopérer pour trouver une solution à cette situation incroyable."
    voice "audio/milon3.ogg"
    b "{size=+10}{font=OldLondon.ttf}Comment ? Une faille de temps ? Où est alée la somptueuse cathédralle qui devoit trespasser toutes les autres ?{/font}\n{/size}{size=-7} {i}Comment ? Une faille temporelle ? Où est passée la cathédrale qui devait dépasser toutes les autres ?{/i}"    
    perso "Calmez-vous, Monseigneur. Nous devons comprendre ce qui s'est passé et comment vous ramener à votre époque."
    voice "audio/milon4.ogg"
    b "{size=+10}{font=OldLondon.ttf}Certes, ce dont je me souviens est d'avoir trouvé ce parchemin...{/font}\n{/size}
    {size=-7} {i}Certes, ce dont je me souviens est d'avoir trouvé ce parchemin{/i}{nw}"
  
# Création de l'Item parchemin
    $ parchemin = Item("Parchemin", "Il vous a été donné par l'évêque \n il comporte un message enygmatique qui permet peut-être d'ouvrir le coffre.", "parchemin.png", actions=[{"label": "Lire", "action": Jump("parchemin")}])
    hide EVEQUE #cache l'image de l'éveque puis affiche l'image de celui-ci avec les mains ouvertes
    show EVEQUEdonne at left
    call screen parchemin #affiche le parchemin dans la main
    label parchemin_recupere:
    $ inventory = []
    hide EVEQUEdonne #cache l'eveque les mains ouvertes
    show EVEQUE at left
    show screen inventory_icon #fait apparaitre le sac à dos en haut de l'écran

# Ajout du parchemin à la suite de la liste
    $ player_inventory.add_item(parchemin)
    voice "audio/e-3.mp3"
    e "Les objets que vous récupérez, sont stockés dans votre inventaire, en haut de l'écran."

label coffre:
    hide EVEQUE 
    show EVEQUEdonne at left
    voice "audio/milon5.ogg"
    b "{size=+10}{font=OldLondon.ttf}et cest coffre.{/font}\n{/size}{size=-7} {i}et ce coffre.{/i}{nw}"
    # Création de l'Item coffre
    $ coffre = Item("Coffre", "Ce coffre vous a été remis par l'évêque, \n il est fermé par un code à 4 chiffres.", "coffre-mini.png", actions=[{"label": "Ouvrir", "action": Jump("coffre1")}])
    call screen coffre #affiche le coffre dans la main
    label coffre_recupere:
    hide parchemin1

# Ajout du livre à la suite de la liste
    $ player_inventory.add_item(coffre)

    hide EVEQUEdonne
    show EVEQUE at left
    voice "audio/e-4.mp3"
    e "le coffre est fermé par un code à 4 chiffres"
    perso "Ce coffre est fermé, savez-vous comment l'ouvrir ?"
    voice "audio/milon6.ogg"
    b "{size=+10}{font=OldLondon.ttf}Et comment le saurai-je ?{/font}\n{/size}{size=-7} {i}Et comment le saurai-je{/i}"

label eveque_cloitre:
    scene bg cloitre
    show EVEQUE at left
    call screen eveque_button #affiche un bouton sur l'éveque pour permettre de cliquer dessus pour amorcer le dialogue

label dial_eveque:
    scene bg cloitre
    show EVEQUE at left
    menu:
        "Depuis combien de temps êtes-vous ici ?" :
            jump temps_ici
        "> Pouvez-vous me rappeler les dates importantes ?" if dialeveque:
            jump dates_importantes
        "Parlez-moi de la cathédrale.":
            jump cathedrale
        "> Une cathédrale carolingienne ?" if dialeveque0:
            jump carolingienne
        "> Qu'est-ce que l'art français ?" if dialeveque0:
            jump artfrancais
        "> En quelle année pensez-vous être ?" if dialeveque0:
            jump quelleannée
        "Arrêter de parler à l'évêque." : 
            jump eveque_cloitre
            #jump coffre1

label quelleannée:
    voice "audio/milon7.ogg"
    b "{size=+10}{font=OldLondon.ttf}Certes, mon ami, nous sommes en l’an de grâce mil deux cens vingt et cinq.{/font}\n{/size}{size=-7} {i}Eh bien mon ami, nous sommes en l'an de grâce 1225{/i}"
    jump dial_eveque

label carolingienne:
    scene carolingienne with fade
    show EVEQUE at left
    voice "audio/milon8.ogg"
    b "{size=+10}{font=OldLondon.ttf}Oui, construicte soubz le règne de la descendence de Charles le Magne.{/font}\n{/size}
    {size=-7} {i}Oui construite sous le règne de la descendance de {b}Charlemagne{/b}{/i}{nw}"
    voice "audio/milon9.ogg"
    b "{size=+10}{font=OldLondon.ttf}Nous allons la destruire par degrez en commençant par le chœur pour y édifier la nouvelle.{/font}\n{/size}
    {size=-7} {i}Nous allons la détruire progressivement en commençant par le choeur pour construire la nouvelle.{/i}{nw}"
    jump dial_eveque

label artfrancais:
    scene artfrancais with fade
    show EVEQUE at left
    voice "audio/milon10.ogg"
    b "{size=+10}{font=OldLondon.ttf}Mon povre ami, en quel monde vivez-vous ?{/font}\n{/size}
    {size=-7} {i}Mon pauvre ami dans quel monde vivez-vous ?{/i}{nw}"
    voice "audio/milon11.ogg"
    b "{size=+10}{font=OldLondon.ttf}Cest art a esté mis en œuvre à Saint-Denis, près de la ville de Paris, par l’Abbé Suger.{/font}\n{/size}
    {nw}{size=-7} {i}Cet art a été mis en oeuvre à Saint-Denis, près de la ville de Paris, par l'Abbé Suger{nw}{/i}"
    voice "audio/milon12.ogg"
    b "{size=+10}{font=OldLondon.ttf}C’est une innovacion françoise qui permet d’eslever des voûtes à des haulteurs vertigineuses,{/font}\n{/size}
    {size=-7} {i}C'est une innovation française qui permet d'élever des voutes à des hauteurs vertigineuses{/i}{nw}"
    voice "audio/milon13.ogg"
    b "{size=+10}{font=OldLondon.ttf}grâce à l’arc brisié, la croisée d’ogive et l’usage d’arc-boutant.{/font}\n{/size}
    {size=-7} {i}grâce à l'arc brisé, la croisée d'ogive et l'usage d'arc-boutant !{/i}{nw}"
    jump dial_eveque

label cathedrale:
    b "{size=+10}{font=OldLondon.ttf}La cathédral karolingienne ere antiane, datant sanz doute de la seconde moitié du Xe siècle.{/font}\n{/size}
    {size=-7} {i}La cathédrale {b}carolingienne{/b} est ancienne, datant sans doute de la seconde moitié du 10e sicèle.{/i}"
    perso "C'est-à-dire 950 ! Elle est vraiment très ancienne."
    b "{size=+10}{font=OldLondon.ttf}C'est por ce que il faloit en edifier une novele, en le novel estil de l'art franceis{/font}\n{/size}
    {size=-7} {i}C'est pourquoi il fallait en édifier une nouvelle, dans le nouveau style de l'{b}art français{/b}.{/i}"
    b "{size=+10}{font=OldLondon.ttf}et nous avon lancé le chantier, cest an meïsme !{/font}\n{/size}
    {size=-7} {i}et nous avons lancé le chantier, cette {b}année même{/b} !{/i}"
    $ dialeveque0 = True
    jump dial_eveque

label temps_ici:
    b "{size=+10}{font=OldLondon.ttf}Je suis chanoine dès l'an mil deux cens et six, c'est à dire despuis dix et neuf ans.{/font}\n{/size}{size=-7} {i}Je suis {b}chanoine{/b} dès l'an 1206, c'est à dire depuis 19 ans..{/i}"
    b "{size=+10}{font=OldLondon.ttf}Puiz prévost du chapitre dès l'an mil deux cens et sept et esleu évesque de Beauvais en l'an mil deux cens et dis set.{/font}\n{/size}{size=-7} {i}Puis {b}prévôt{/b} du chapitre dès 1207 et élu {b}évêque{/b} de Beauvais en 1217.{/i}"
    perso "Vous avez donc vu beaucoup de choses se passer ici."
    b "{size=+10}{font=OldLondon.ttf}Oïl, et chascune année a aporté son lot de défis et de décisions importantes.{/font}\n{/size}{size=-7} {i}Oui et chaque année a apporté son lot de défis et de décisions importantes.{/i}"
    b "{size=+10}{font=OldLondon.ttf}Chascune date que je vos ai mentionée est importante. Peut-estre i trouverez-vos la clef por ouvrir le coffre.{/font}\n{/size}{size=-7} {i}Chaque date que je vous ai mentionnée est importante. Peut-être y trouverez-vous la clé pour ouvrir le coffre.{/i}"
    $ dialeveque = True
    jump dial_eveque

label dates_importantes:
    b "{size=+10}{font=OldLondon.ttf}Bien sûr. 1206, 1207, 1217, et surtout, 1225.{/font}"
    perso "Pourquoi surtout 1225?"
    b "{size=+10}{font=OldLondon.ttf}Enfin, c'est en ceste année mil deux cens vingt et cinq, qu'avec le Chapitre nous avon décidé de reprendre la construction du nouvel ovre.{/font}\n{/size}{size=-7}{i}Enfin, c'est en cette année 1225 qu'avec le Chapitre nous avons décidé de repondre la construction du nouvel oeuvre.{/i}"
    voice "audio/e-5.mp3"
    e "Cela semble être une année clef."
    jump dial_eveque

label coffre1:
    call screen inventory_coffre1 #affiche le coffre
    jump eveque_cloitre

label parchemin:
    call screen inventory_parchemin #affiche le parchemin
    jump dial_eveque

#Coffre ouvert
label coffre_ouvert:
    # Suppression du coffre et du parchemin de l'inventaire
    $ player_inventory.remove_item(coffre)
    $ player_inventory.remove_item(parchemin)
    # Ajout du compteur pour les morceaux de parchemin à 1
    $ morceaux_parchemin += 1

    #affiche l'éveque et joue la nouvelle musique
    show EVEQUE
    play music "audio/04-petit_pantin_au_coeur_de_glace-eponyme_I-laei-copyleft.mp3" fadein 1.0
    
    # Message de félicitation
    b "{size=+10}{font=OldLondon.ttf}Par ma foi, [nom_du_perso], tu es plus rusé que tu ne sembles !{/font}\n{/size}{size=-7}{i}Bravo, [nom_du_perso], tu es plus rusé que tu en as l'air !{/i}"

    # création des objets du coffre :
    $ plan_parchemin = Item("Brochure", "Cette brochure présente un plan de la cathédrale.", "plan-parchemin.png", actions=[{"label": "Voir", "action": [Hide(),Jump("plan_cathedrale")]}])
    # attention morceau_1 est dispo que pour l'exemple
    $ morceau_1 = Item("Morceau", "Ceci est un morceaux de quelque chose, il en manque.", "morceau_1.png", actions=[{"label": "Voir", "action": Show("inventory_morceau_1")}])
    $ cryptex = Item("Cryptex", "Un mystérieux tube, qui s'ouvre avec un mot de 5 lettres.", "cryptex-mini.png", actions=[{"label": "Ouvrir", "action": Jump("cryptex2")}])
    
    # Vérification si tous les objets ont été pris
    init python:
        def check_if_all_taken():
            if cryptex_taken and plan_taken and morceau_taken:
                renpy.hide_screen("coffre_ouvert")
                renpy.notify("Tous les objets ont été récupérés !")

    # Appelle la fonction pour vérifier si tous les objets ont été pris
    $ check_if_all_taken()

    # Appelle le screen pour afficher les objets du coffre
    call screen coffre_ouvert
    label coffre_ouvert_et_vide:
    call screen eveque_button2
    label dial_eveque2:
    menu:
        "Que dois-je faire maintenant ?" :
            jump quefaireensuite
        "Arrêter de parler à l'évêque." : 
            jump coffre_ouvert_et_vide
    label quefaireensuite:
    b "{size=+10}{font=OldLondon.ttf}À la fin, pas si fin ! Regarde donc ce que tu as amassé !{/font}\n{/size}{size=-7}{i}Finalement, pas si futé ! Consulte ton inventaire !{/i}"
    jump coffre_ouvert_et_vide

#label cryptex:
    call screen inventory_screen

label cryptex2:
    call screen inventory_cryptex

label plan_cathedrale:
    show plan_cathedrale_grand with fade
    voice "audio/e-6.mp3"
    e "Eh, ceci est un plan de la cathédrale actuelle{nw}"
    # supprime l'icone du plan dans l'inventaire
    $ player_inventory.remove_item(plan_parchemin)
    voice "audio/e-7.mp3"
    e "cela va nous êtes très utile pour circuler dans la cathédrale{nw}"
    voice "audio/e-8.mp3"
    e "je vais l'afficher en haut à droite de l'écran.{nw}"
    show screen plan_icon #fait apparaitre le plan
    voice "audio/e-9.mp3"
    e "Pour te déplacer, clique sur le plan pour l'afficher, puis sur la zone où tu veux te rendre.{nw}"
    voice "audio/e-10.mp3"
    e "Pour t'aider à te repérer, j'ajouterai des annotations{nw}"
    voice "audio/e-11.mp3"
    e "ici nous sommes dans le cloître, je vais l'ajouter, dès maintenant.{nw}"
    hide plan_cathedrale_grand
    show plan_cathedrale_grand_cloitre
    voice "audio/e-12.mp3"
    e "J'ai lu qu'il y a un accueil dans la cathédrale, je te conseille de t'y rendre.{nw}"
    voice "audio/e-13.mp3"
    e "Tu y en apprendras certainement plus.{nw}"
    hide plan_cathedrale_grand_cloitre
    voice "audio/e-14.mp3"
    e "Ouvre le plan pour aller à l'accueil de la cathédrale !"
    # Attendre une interaction du joueur
    $ _game_menu_screen = None  # Empêche l'affichage du menu du jeu
    window hide
    $ ui.interact()

label orgues:
    scene orgues
    # Attendre une interaction du joueur
    $ _game_menu_screen = None  # Empêche l'affichage du menu du jeu
    window hide
    $ ui.interact()

label choeur:
    scene choeur
    # Attendre une interaction du joueur
    $ _game_menu_screen = None  # Empêche l'affichage du menu du jeu
    window hide
    $ ui.interact()

label Accueil:
    #Montrer le guichet d'accueil
    scene bg kiosque with fade
    show Alexandre at center
    voice "/audio/alex-1.ogg"
    alex "Ah c'est donc vous [nom_du_perso], nous vous attendions avec impatience.{nw}"
    voice "/audio/alex-2.ogg"
    alex "Depuis que ce drôle de personnage traîne dans le cloître, rien ne va plus !"
    perso "Comment ça rien ne va plus ?"
    show Alexandre etonne at center
    alex "Comment ça ! Vous n'êtes donc pas au courant ?"
    show Alexandre at center
    alex "L'horloge astronomique ne fonctionne plus,"
    alex "l'orgue est complètement bloqué,"
    alex "et impossible d'entrer dans la sacristie !"
    menu:
        "Que se passe-t-il avec l'horloge ?" :
            jump Horloge
        "L'orgue est bloqué ?" : 
            jump coffre_ouvert_et_vide
        "Pourquoi est-il impossible d'entrer dans la sacristie ?" :
            jump Horloge
    # Attendre une interaction du joueur
    $ _game_menu_screen = None  # Empêche l'affichage du menu du jeu
    window hide
    $ ui.interact()

label Horloge:
    # Montrer la scène horloge_astro
    scene horloge_astro
    show Alexandre at right
    show screen toggle_button
    show screen grille_horloge
    alex "Bonjour [nom_du_perso]"
    # Attendre une interaction du joueur
    $ _game_menu_screen = None  # Empêche l'affichage du menu du jeu
    window hide
    $ ui.interact()

label grille_horloge_ouvert:

label continue:

label puzzle:
    #call screen puzzle
    scene bg bureau
    hide screen toggle_button
    hide screen grille_horloge

    python:
        k = Puzzle()
        k.set_sensitive(False)
        k.show()    


label quick_continue:
    
    while True:

        python:
        
            ui.textbutton("abandonner", ui.jumps("giveup"), xalign=.02, yalign=.98)
            k.set_sensitive(True)
            event = k.interact()

            if event:
                renpy.checkpoint()
            
            k.set_sensitive(False)
        # e "[event]"
        if event == "win":
            jump win

label giveup:

    $ k.set_sensitive(False)
    
    show dim
    with dissolve
    
    menu:
        e "Etes-vous sûr d'arrêter ?"

        "Yes":
            e "Très bien, on retentera plus tard."
            jump win

        "No":
            jump continue

label win:
    scene horloge_astro_ouvert
    #montrer une autre scène
    call screen rotating_image

# Fin de la scène
    return


label puzzle_2:
    scene bg bureau
    hide screen toggle_button
    hide screen grille_horloge
    $ puzzle2_time_left = puzzle2_time_limit
    show screen puzzle2_timer

    python:
        k2 = Puzzle2()
        k2.set_sensitive(False)
        k2.show()


label quick_continue_2:

    while True:

        python:

            ui.textbutton("abandonner", ui.jumps("giveup_2"), xalign=.02, yalign=.98)
            k2.set_sensitive(True)
            event2 = k2.interact()

            if event2:
                renpy.checkpoint()

            k2.set_sensitive(False)

        if event2 == "win":
            jump win_2


label giveup_2:

    $ k2.set_sensitive(False)
    hide screen puzzle2_timer

    show dim
    with dissolve

    menu:
        e "Etes-vous sûr d'arrêter ?"

        "Yes":
            e "Très bien, on retentera plus tard."
            jump lose_2

        "No":
            jump quick_continue_2


label win_2:
    hide screen puzzle2_timer
    scene horloge_astro_ouvert
    show Alexandre at right
    alex "Bravo ! Vous avez résolu le puzzle de la tour lanterne avec brio !"
    alex "Pour vous remercier, voici une petite présentation de l'association de la cathédrale de Beauvais."
    
    # Lancement de la vidéo de l'association. 
    $ renpy.movie_cutscene("video/Découvrez-l’horloge-astronomique-de-Beauvas_1.webm")
    scene horloge_astro
    show Alexandre at right
    alex "Le temps est écoulé pour ce puzzle de la tour lanterne."
    menu:
        alex "Voulez-vous réessayer de reconstituer le puzzle ?"
        "Oui, je veux retenter ma chance.":
            jump puzzle_2
        "Non, j'abandonne pour le moment.":
            alex "Très bien, vous pourrez réessayer plus tard."
            return