# Guide d'Architecture et d'édition Avancée - Les Secrets de la Cathédrale de Beauvais

Ce document détaille l'intégralité du système du jeu pour permettre à l'équipe de développement et au management de localiser, comprendre, et modifier facilement n'importe quel élément du projet.

---

## 🏗️ 1. Architecture Complémentaire du Système (Cartographie des Fichiers)

Tout le code logique du projet est segmenté au sein du dossier `game/`. Voici le rôle précis de **chaque script** majeur :

### 🗂️ Dossier `core/` (Bases Moteur & Configurations)
Ce répertoire est l'épine dorsale de votre projet Ren'Py. N'y touchez que pour des réglages globaux ou l'ajout d'objets permanents.
*   **`script.rpy`** : Démarre le jeu (`label start`). Il initialise les variables globales (ex: `clef_horloge`, `cryptex_taken`), initialise l'inventaire avec `player_inventory` (de classe `Inventory`) et instancie des objets via la classe Python `Item`.
*   **`map_logic.rpy`** : Le contrôleur d'accès de votre carte. Contient la liste des variables booléennes (ex: `location_cloitre_active`) et l'écran de debug (`screen debug_map_locations`) pour forcer les accès en cours de test.
*   **`gui.rpy`** et **`options.rpy`** : Configurations métadonnées du moteur (couleurs du texte `gui.accent_color`, police `gui.text_font`, nom du projet `config.name`, version).
*   **`functions.rpy`** : Utilitaires Python transversaux, comme la gestion du parcours des lettres `next_letter(letter)` et `prev_letter(letter)` (généralement utilisés pour vos cadenas/cryptex).
*   **`keymap.rpy`** : Assigne des touches spécifiques du clavier (ex: Shift+P, Shift+U) à des fonctions de triche ou de vue développeur (Action Editor, Image Viewer).
*   **`00warper.rpy`** : Définit des fonctions mathématiques avancées en Python (`@renpy.atl_warper`) pour fluidifier vos animations ATL (rebond, accélération, lissage).

### 🗂️ Dossier `minigames/` (Moteurs des Puzzles)
C'est ici que toute l'interactivité "hors-dialogues" est processée grâce aux "screens" (écrans).
*   **`minijeu_orgue.rpy`** : Simulateur musical. Écoute les touches cliquées via ses textbuttons, met à jour la liste `orgue_sequence` et vérifie si la séquence de la fin correspond avec l'une des entrées du dictionnaire cible `orgue_melodies`.
*   **`crafting_system.rpy`** : Système de fusion d'objets. Lit le dictionnaire `craft_recipes` liant deux items cliqués dans le menu pour en générer et retourner un nouveau.
*   **`puzzle_mosaique.rpy`** : Logique de manipulation d'éléments et d'interactivité temporelle (utilise la fonction scalaire `advance_time()` et la variable `time_of_day`).
*   **`puzzle.rpy`** et **`minijeu_assemblage.rpy`** : Mécaniques de puzzle basées sur DragGroup. Permet de glisser-déposer des fragments visuels (`check_assemblage_drag()`) vers des conteneurs (`droppable`).
*   **`cardgame.rpy`** : Le système de base fondateur (extrapolé de displayables PyTom) permettant de superposer, gérer la profondeur et glisser des cartes ou éléments sur un "plateau" interactif.
*   **`minijeu_message_cache.rpy`** : Le code complexe pour l'encrage/révélation invisible via le frottement de la souris. Repose sur une displayable customisée `InvisibleInk` avec gestion d'alpha de pygame.
*   **`debug_minigames.rpy`** : Un menu développeur super pratique listant toutes les scènes "jouables" pour un accès direct au test sans traverser l'histoire complète (via registre `debug_minigame_registry`).

### 🗂️ Dossier `quests/` (Structure Scénaristique)
C'est ici que l'auteur écrit la trame.
*   **`exterieurs.rpy`** : Gère les points and clicks "Hubs" sur le Parvis (Nord, Sud, Est, Ouest), les interactions simples à la porte du cloître et la détermination des variables comme `met_pnj_entree`.
*   **`quete_basse_oeuvre.rpy`** : Le script de la "Basse Œuvre", illustrant une boucle de quête complète : Rencontre de Sœur Agnès, acceptation via la variable `quete_clef_acceptee`, recherche visuelle (`screen salle_choeur()`), test d'inventaire pour récupérer les lunettes, et don de l'indice final en échange.

---

## 🛠️ 2. Gérer la Carte et Débloquer des Lieux (`map_logic.rpy`)
Le jeu gère les accès via des variables booléennes (`True` = accessible, `False` = inaccessible).

**A. Déclarer la nouvelle salle** (Dans `game/core/map_logic.rpy`) :
Ajoutez une ligne avec les variables existantes (par défaut cachée) :
```renpy
default location_crypte_active = False 
```

**B. Ajouter le bouton de carte** (Où vous gérez le visuel de la carte, ex: `plan_screen`) :
```renpy
if location_crypte_active:
    imagebutton:
        idle "images/bouton_crypte_normal.png"
        action Jump("visite_crypte_label") 
```

**C. Débloquer la pièce dans le scénario** :
Au moment de votre choix dans l'histoire, exécutez le code Python sur une seule ligne (grâce au symbole `$`) :
```renpy
"Génial ! J'ai repéré l'entrée vers la crypte !"
$ location_crypte_active = True
"La Crypte a été ajoutée à votre carte."
```

---

## 🎒 3. Utiliser le Système d'Inventaire Python (`script.rpy`)

L'inventaire est géré par la variable complexe `player_inventory`.

**Donner un objet au joueur :**
Par exemple, pour donner un parchemin :
```renpy
$ player_inventory.add_item(Item("parchemin_secret", "Parchemin", "Un parchemin ancien.", "parchemin.png"))
```

**Vérifier la possession d'un objet (et lui retirer si besoin) :**
C'est la partie un peu technique calquée sur `quete_basse_oeuvre.rpy`. 
Pour les dialogues où un personnage demande l'objet :
```renpy
label donner_objet_pnj:
    # 1. Scanner l'inventaire en Python
    python:
        possede_objet = any(item.item_id == "parchemin_secret" for item in player_inventory.get_items())

    # 2. Séparation Conditionnelle
    if possede_objet:
        npc "Oh merci, vous avez trouvé mon parchemin !"
        # 3. Supprimer l'item en relisant la même condition
        $ player_inventory.remove_item(next(item for item in player_inventory.get_items() if item.item_id == "parchemin_secret"))
        jump quete_reussie
    else:
        npc "N'hésitez pas à revenir me voir si vous l'avez."
```

---

## 🎹 4. Ajouter une Nouvelle Mélodie ou Récompense (L'Orgue)

Si vous voulez qu'une nouvelle musique ("Do, Fa, Sol") donne une clé secrète.
Allez dans `game/minigames/minijeu_orgue.rpy`.

**1. Définir la nouvelle partition :**
Cherchez le dictionnaire `orgue_melodies` (dans un bloc `init python`) et ajoutez-y la séquence.
```renpy
init python:
    orgue_melodies = {
        "partition_1": ["Sol", "Mi", "Re"],
        "melodie_secrete": ["Do", "Re", "Mi", "Do"],
        "melodie_magique": ["Mi", "Fa", "Sol", "Do", "Re"],
        "porte_cachee": ["Do", "Fa", "Sol"] # <-- AJOUT ICI, avec virgule au-dessus.
    }
```

**2. Créer la séquence à lancer en cas de victoire :**
Le script de l'orgue saute (`jump`) dynamiquement vers un point qui s'appelle TOUJOURS `orgue_` suivi de la clé de votre partition. Vous devez juste créer le label de réponse :
```renpy
label orgue_porte_cachee:
    "Vous jouez la suite de notes : Do, Fa, Sol..."
    "Un déclic se fait entendre ! Un panneau mural pivote."
    # Appliquez vos variables !
    $ location_salle_secrete = True
    jump retour_jeu
```

---

## 🪚 5. Ajouter une recette au Système de Craft

Le système d'artisanat/fouille combinée est piloté par un dictionnaire ultra-simple situé dans `game/minigames/crafting_system.rpy`.

**Créer une nouvelle combinaison :**
Trouvez l'objet `craft_recipes`. Le format est toujours clé : `("id_objet_1", "id_objet_2")` et valeur : `"id_objet_resultat"`.
```renpy
define craft_recipes = {
    ("morceau_carte_1", "morceau_carte_2"): "carte_complete",
    
    # AJOUT: Combiner Manche en Bois + Tête Acier = Marteau
    ("manche_bois", "tete_acier"): "marteau"
}
```
*Note système : Le moteur gèrera seul la suppression des objets 1 et 2 en injectant dynamiquement l'objet résultat.* Et l'ordre ("manche" puis "tête" ou l'inverse) n'a pas d'importance, le moteur vérifie dans les deux sens de manière automatique !

---
---

# Partie 2 : Handoff Développeur & Architecture Profonde

Cette section est strictement destinée aux développeurs Python / Ren'Py effectuant la reprise du projet (Handoff). Elle détaille l'ingénierie sous-jacente des mini-jeux complexes, la gestion d'interface custom (PyGame), et l'étendue des variables d'états (Stores).

## 🧰 A. Core System : Logique Transversale (`game/core/`)

Ces fichiers ne contiennent pas d'histoire, mais la configuration bas niveau du moteur.
*   **`functions.rpy`**
    Contient les fonctions scalaires Python globales, notamment pour la manipulation de chaînes de caractères (essentiel pour les cryptex ou mots de passe).
    - `def next_letter(letter):` Renvoie la lettre suivante de l'alphabet.
    - `def prev_letter(letter):` Renvoie la lettre précédente.
*   **`map_logic.rpy`**
    Gère les variables de type `default location_NOM_active`. Comprend également `screen debug_map_locations()` qui utilise `ToggleVariable()` pour forcer l'accès à n'importe quelle pièce pendant les tests.
*   **`script.rpy` (Le point de montage)**
    Point d'entrée principal (`label start`). Il configure non seulement `player_inventory` mais déclare d'innombrables checkpoints critiques via les labels : `rencontre_moine`, `coffre`, `eveque_cloitre`, etc. Contient les classes `Item` (id, description, actions) et l'objet de gestion `Inventory`.

## 🕯️ B. Ingénierie "Jeu de la bougie / Encre" (`minijeu_message_cache.rpy`)

Ce script intègre une logique avancée avec une manipulation d'Alpha via les interfaces PyGame (Displayable).
*   **Classe Python Custom `InvisibleInk(renpy.Displayable)`** :
    - Hérite de `renpy.Displayable` pour intercepter les évènements de souris.
    - La grille d'invisibilité est contrôlée par `grid_size` et l'épaisseur du pinceau par `brush_size`.
    - La méthode `render()` génère des fragments de cache pour ne pas saccader le jeu. Elle compose la transformation Alpha au survol.
    - **Condition de victoire** : Validée dans `event(ev, x, y, st)` lorsque `self.fully_revealed_count > (self.total_cells_approx * 0.6)` (C'est-à-dire quand le joueur a "gratté" 60% de l'écran).
*   **Contrôleur de Flux `start_message_cache(...)`** :
    Intercepte l'inventaire avant de lancer le `screen minijeu_message_cache()`. Vérifie la combinaison d'objets (par ex: la Bougie et le Parchemin) et déclenche l'injection de l'objet révélé une fois le displayable résolu.

## 🧩 C. Architecture Drag & Drop et Puzzles (`puzzle.rpy`, `assemblage.rpy`)

Contrairement à l'orgue qui est géré en GUI pure (boutons / écrans), ces éléments reposent sur le système interne de `DragGroup` et PyTom.
*   **Fichier `puzzle.rpy`** :
    - `class Puzzle(object)` : Classe matrice définissant les mécaniques d'un type de Solitaire. Gère les coordonnées absolues des fondations (`foundation_drag`), le système d'accroche, et la vérification des empilements (`card_click`).
    - `class Puzzle2(Puzzle)` : Type étendu spécifiquement pour le jeu de l'horloge astronomique. Surcharge le multiplicateur de taille via `card_zoom=0.40` et modifie la capture d'assets en formatant dynamiquement sur `/images/horloge/piece-%d-%d.png`.
*   **Fichier `minijeu_assemblage.rpy`** :
    - `def check_assemblage_drag(drags, drop)` : Moteur exclusif de Snap (accroche). Si l'objet glissé chevauche sa cible, il est aligné automatiquement si `drop.drag_name` équivaut à `"zone_" + piece.drag_name`.
    - Ce système modifie le set global `store.pieces_placed` et valide implicitement le puzzle lorsque le set est plein.

## 🐛 D. Registry et Outils Développeur (`debug_minigames.rpy`)

Pour éviter de jouer 20 minutes de visual novel pour tester un puzzle, un registre permet des sauts structurels directs.
*   **Data Models & Flags** :
    - `debug_minigame_mode` : Si True, court-circuite la trame narrative. Lors de la réussite d'un mini-jeu isolé, le `Return()` repointe vers le menu debug au lieu de continuer l'histoire.
    - `debug_minigame_registry` : Un dictionnaire Python mappant le nom lisible d'un jeu (ex: "Le Coffre") vers son endpoint de `label` (ex: `debug_test_coffre`).
    - Objets cachés (`debug_find_objects_data`) : Les variables d'états des jeux de type Objets Cachés. Ils modifient des index contenant `xpos`, `ypos` pour injecter des sprites cliquables en superposition.