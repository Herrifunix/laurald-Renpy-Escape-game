# game/exterieurs.rpy

screen exterieur_parvis_screen():
    text "Parvis Ouest" size 50 xalign 0.5 ypos 50 font "OldLondon.ttf"
    
    # Navigation
    textbutton "Aller au Portail Nord" action Jump("exterieur_nord") xalign 0.1 yalign 0.5 text_size 30 background "#333b"
    textbutton "Aller au Portail Sud" action Jump("exterieur_sud") xalign 0.9 yalign 0.5 text_size 30 background "#333b"
    
    # Entrée
    textbutton "Entrer dans le Cloître" action Jump("rencontre_moine") xalign 0.5 yalign 0.8 text_size 40 background "#632b"

screen exterieur_nord_screen():
    text "Portail Nord" size 50 xalign 0.5 ypos 50 font "OldLondon.ttf"
    
    textbutton "Aller au Parvis Ouest" action Jump("exterieur_parvis") xalign 0.1 yalign 0.5 text_size 30 background "#333b"
    textbutton "Aller au Chevet Est" action Jump("exterieur_chevet") xalign 0.9 yalign 0.5 text_size 30 background "#333b"

screen exterieur_sud_screen():
    text "Portail Sud" size 50 xalign 0.5 ypos 50 font "OldLondon.ttf"
    
    textbutton "Aller au Chevet Est" action Jump("exterieur_chevet") xalign 0.1 yalign 0.5 text_size 30 background "#333b"
    textbutton "Aller au Parvis Ouest" action Jump("exterieur_parvis") xalign 0.9 yalign 0.5 text_size 30 background "#333b"

screen exterieur_chevet_screen():
    text "Chevet Est" size 50 xalign 0.5 ypos 50 font "OldLondon.ttf"
    
    textbutton "Aller au Portail Nord" action Jump("exterieur_nord") xalign 0.1 yalign 0.5 text_size 30 background "#333b"
    textbutton "Aller au Portail Sud" action Jump("exterieur_sud") xalign 0.9 yalign 0.5 text_size 30 background "#333b"


label exterieur_parvis:
    hide screen exterieur_nord_screen
    hide screen exterieur_sud_screen
    hide screen exterieur_chevet_screen
    scene bg accueil
    play music "audio/Solas-InnOfGoodFortune.mp3" fadein 1.0 if_changed
    show screen exterieur_parvis_screen
    pause
    jump exterieur_parvis

label exterieur_nord:
    hide screen exterieur_parvis_screen
    hide screen exterieur_chevet_screen
    scene bg accueil
    play music "audio/Solas-InnOfGoodFortune.mp3" fadein 1.0 if_changed
    show screen exterieur_nord_screen
    pause
    jump exterieur_nord

label exterieur_sud:
    hide screen exterieur_parvis_screen
    hide screen exterieur_chevet_screen
    scene bg portail_sud
    play music "audio/Solas-InnOfGoodFortune.mp3" fadein 1.0 if_changed
    show screen exterieur_sud_screen
    pause
    jump exterieur_sud

label exterieur_chevet:
    hide screen exterieur_nord_screen
    hide screen exterieur_sud_screen
    # on utilise portail_sud ou une autre image en attendant mieux
    scene bg portail_sud
    play music "audio/Solas-InnOfGoodFortune.mp3" fadein 1.0 if_changed
    show screen exterieur_chevet_screen
    pause
    jump exterieur_chevet
