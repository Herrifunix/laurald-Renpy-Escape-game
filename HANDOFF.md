# Reprise du projet — Faille temporelle à la Cathédrale de Beauvais

Document de passation pour le développeur qui reprend le projet. Il complète
`TUTORIAL.md` : ce dernier explique **l'architecture** (comment le jeu marche),
celui-ci décrit **l'état du projet**, les conventions et ce qui reste à faire.

## Par où commencer

1. Lire `TUTORIAL.md` (architecture, systèmes de jeu, inventaire, mini-jeux).
2. Lire ce fichier.
3. Ouvrir le projet dans le launcher Ren'Py et lancer le jeu une fois.
4. Lancer `renpy.py laurald-Renpy-Escape-game lint` pour vérifier la santé du code.

## Structure du projet

| Dossier | Rôle |
|---|---|
| `game/core/` | Moteur : `script.rpy` (point d'entrée, classes `Item`/`Inventory`, `label start`), `options.rpy` (nom, version, build), `gui.rpy`, `keymap.rpy`, `functions.rpy`, `map_logic.rpy`, `00warper.rpy`. |
| `game/core/screens.rpy` | Écrans **standards** de Ren'Py (say, menus, préférences, save/load…). |
| `game/core/screens_jeu.rpy` | Écrans **spécifiques au jeu** (inventaire, plan, coffre, cryptex, cadenas…). |
| `game/minigames/` | Moteurs des puzzles et mini-jeux. |
| `game/quests/` | Trame scénaristique (`exterieurs.rpy`, `quete_basse_oeuvre.rpy`). |
| `game/ui/`, `game/plugins/` | **Code tiers (Action Editor)** — ne pas modifier (voir ci-dessous). |
| `game/images/` | Images, triées en sous-dossiers : `scenes/`, `items/`, `gui/`, `personnages/`, `horloge/`, `puzzle/`, `safe_i/`, `message_cache/`. |

## Conventions

- **Code tiers à ne pas toucher** : `game/ui/` et `game/plugins/` (la
  bibliothèque *Action Editor*, outil de développement). Ne les modifier que
  pour mettre à jour cette bibliothèque.
- **`00warper.rpy`** : le préfixe `00` force son chargement en premier (les
  warpers ATL doivent exister avant les animations). Ne pas renommer.
- **Langue** : le projet mélange français et anglais. Convention visée pour le
  nouveau code : identifiants/labels/noms de fichiers **du domaine du jeu en
  français** ; noms du moteur Ren'Py (`config.*`, `gui.*`, API des écrans)
  **inchangés**. L'existant n'est pas uniformisé — l'harmoniser au fil des
  modifications, jamais en bloc (les labels/écrans sont référencés par chaîne).
- **Images** : Ren'Py résout les fichiers image par **nom de base**, quel que
  soit le sous-dossier. Garder les noms de fichiers **uniques** dans
  `game/images/`.
- Ren'Py charge automatiquement tous les `.rpy` sous `game/` : un fichier peut
  être déplacé ou renommé sans casser les `jump`/`call`.

## Construction (build Android)

`creer_apk.ps1` et `build_android.bat` contiennent en dur le chemin
`JAVA_HOME` (`C:\Program Files\Java\jdk-21.0.11`) et le chemin du SDK Ren'Py.
**Sur une autre machine, mettre ces chemins à jour.**

## Checklist avant une version publique (décisions à prendre)

- [ ] **`config.developer`** est à `True` dans `game/core/options.rpy` : cela
      expose les outils de debug (Shift+P, Shift+U) aux joueurs. Le passer à
      `False` pour les builds de sortie.
- [ ] **Clés de signature dans Git** : `android.keystore` et `bundle.keystore`
      sont versionnés — risque de sécurité. Décider de les retirer de
      l'historique et, le cas échéant, de régénérer les clés.
- [ ] **Fichiers compilés versionnés** : ~42 fichiers `.rpyc`/`.rpyb` sont
      suivis par Git bien qu'ils soient régénérables. `.gitignore` les ignore
      désormais ; les retirer du suivi avec `git rm --cached`.
- [ ] **`renpy-graphviz-linux-amd64`** : binaire Linux de 5 Mo versionné, inutile
      sous Windows — à supprimer si non utilisé.

## Problèmes connus à investiguer

- **Fichier audio manquant** : `script.rpy` joue
  `audio/04-petit_pantin_au_coeur_de_glace-eponyme_I-laei-copyleft.mp3`, qui
  n'existe pas dans `game/audio/`. Ajouter le fichier ou corriger la référence.
- **Images obsolètes** : `accueil.png`, `choeur.png`, `cloitre.png`,
  `horloge.png` sont restées à la racine de `game/images/` ; elles font doublon
  (insensible à la casse) avec les versions de `scenes/` et ne sont plus
  référencées. À vérifier puis supprimer.
- **`cardgame.rpy`** (bibliothèque solitaire tierce) : bug possible dans
  `__contains__` (~ligne 523, variable `card` au lieu de `item`). Vérifier
  avant d'y toucher — ce fichier est du code tiers.
- **`minijeu_message_cache.rpy`** : après un craft raté, le résultat de
  `create_item_by_id()` n'est pas vérifié contre `None` — risque de plantage.
- **Nom de fichier non-ASCII** : la vidéo `Découvrez-l'horloge-astronomique-…`
  contient des accents ; les distributions ZIP n'acceptent de façon fiable que
  l'ASCII. À renommer avant un build de distribution.

## Vérifier le code

```
renpy.py laurald-Renpy-Escape-game lint
```
Avertissements pré-existants sans gravité : priorités d'init hors plage dans
`game/plugins/` (code tiers) et le nom de fichier vidéo non-ASCII ci-dessus.
