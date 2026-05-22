# Trame de l'escape game — Cathédrale Saint-Pierre de Beauvais

## Contexte

L'escape game Ren'Py est déjà partiellement construit : la trame existante met en scène
**Milon de Nanteuil**, évêque historique de Beauvais qui lança la nouvelle cathédrale en
1225, projeté à notre époque par une faille temporelle. Le jeu dispose déjà de toutes les
mécaniques nécessaires (navigation, inventaire, crafting, cadenas, cryptex, mini-jeux).

Ce document est la **trame du scénario expliquée point par point**, d'une durée d'environ
**1 heure**, pour un **public scolaire (collège/lycée)** avec un **chrono global d'1 h**.
Le scénario complète la trame existante, réutilise uniquement les mécaniques déjà codées,
et **n'invente aucun fait historique** : chaque énigme et chaque solution s'appuie sur
`histore.txt` (les numéros de ligne sont indiqués pour vérification).

---

## Règle d'or : « on n'invente rien »

- Le **cadre fictif** (faille temporelle, Milon de Nanteuil revenu de 1225) existe déjà
  dans le jeu et est conservé. Milon de Nanteuil est un personnage **réel** (`histore.txt`
  l.48).
- Tous les **faits, dates, chiffres, noms et indices** des énigmes proviennent de
  `histore.txt`. Aucune date ni anecdote n'est ajoutée.
- Les **solutions** des cadenas/cryptex sont des données historiques vérifiables.
- Les mini-jeux (mélodie, reconstitution, assemblage) sont des *mécaniques* : le jeu ne
  prétend jamais que la mélodie ou le motif assemblé est « historique ». En revanche, le
  fait enseigné autour de chaque mini-jeu, lui, est sourcé.

---

## Trame narrative globale

> En 1225, Milon de Nanteuil décide de bâtir « la plus grande et la plus audacieuse
> cathédrale de toute la chrétienté » (`histore.txt` l.48). Huit siècles plus tard, une
> faille temporelle l'arrache à son chantier et le dépose dans le cloître d'aujourd'hui.
>
> La cathédrale est un édifice qui **mesure le temps** : deux horloges astronomiques et un
> grand orgue en rythment la vie. La faille a déréglé ces « gardiens du temps » — l'horloge
> est arrêtée, l'orgue est muet, la sacristie est scellée. Tant qu'ils restent déréglés, le
> passage reste instable.
>
> Le joueur doit **réveiller les trois gardiens du temps**, puis reconstituer la **clé de
> la sacristie** (en deux morceaux) pour atteindre la faille et **renvoyer Milon en 1225**
> — avant que l'horloge médiévale, dite du *Chanoine Musique*, ne sonne l'heure et ne
> referme définitivement le passage.

---

## Le chrono global d'1 heure

- **Diégèse :** l'horloge médiévale du Chanoine Musique — « la plus ancienne horloge à
  carillon encore en fonctionnement » (`histore.txt` l.307, l.366) — sonnera l'heure dans
  60 minutes. À ce carillon, la faille se referme. Le joueur a donc une heure pour renvoyer
  Milon.
- **Affichage :** compte à rebours visible en permanence (réutilise le principe du
  `puzzle2_timer` de `screens_jeu.rpy`, étendu à toute la partie).
- **Déclenchement :** le chrono démarre à la fin de l'Étape 3 (briefing d'Alexandre), une
  fois que le joueur maîtrise la carte et l'inventaire — pour ne pas pénaliser la phase de
  prise en main.
- **Fin de temps :** scène de « game over » douce → proposition de recommencer (cohérent
  avec le ton scolaire, pas de punition sèche).

---

## Déroulé point par point

Chaque étape précise : durée, lieu, mécanique **déjà existante** utilisée, faits
historiques enseignés (avec lignes `histore.txt`), énigme + solution, indices, récompense.

### Étape 0 — L'irruption de la faille  (~2 min)
- **Lieu / mécanique :** vidéo d'intro `cloitre_faille.webm` puis `label start` →
  `exterieur_parvis` (déjà codé).
- **But :** poser l'ambiance ; le joueur arrive sur le parvis.
- **Pédagogie :** aucune énigme — immersion.

### Étape 1 — Le parvis et le tour extérieur  (~8 min)
- **Lieu :** parvis (portail Sud), chevet Est, portail Nord, façade Ouest de la
  Basse-Œuvre — navigation par flèches (`exterieurs.rpy`, déjà codé).
- **Mécaniques existantes :** navigation extérieure ; hotspot « ❗ » ; mini-jeu
  **mosaïque** selon l'heure (`puzzle_mosaique.rpy`).
- **Faits enseignés :**
  - Portail Sud = chef-d'œuvre du 16ᵉ s. de **Martin Chambiges** ; rose de la Création ;
    vantaux de **Jean Le Pot** v.1540 (`histore.txt` l.157, l.161, l.165-168).
  - Portail Nord = début 16ᵉ s. ; **arbre de Jessé** (l.187, l.189-191).
  - La **Basse-Œuvre** est l'ancienne cathédrale carolingienne du **10ᵉ siècle**
    (l.3, l.6).
- **Énigme 1A — La clé du cloître :** l'hôtesse refuse l'entrée principale (« la
  cathédrale n'est pas encore ouverte », déjà codé `entrer_cathedrale_garde`). Le joueur
  doit **contourner** : côté Est, le hotspot « ❗ » révèle une vieille clé cachée
  (`trouver_cle_cloitre`, déjà codé) → ouvre la porte du cloître.
- **Énigme 1B — La mosaïque (optionnelle, indice) :** la mosaïque ne révèle son motif
  qu'à la bonne heure (mécanique `time_of_day` : matin/midi/soir/nuit). Réglée sur
  **soir**, elle montre le motif du couchant côté Ouest — clin d'œil pédagogique au fait
  que la lumière, « symbole de la lumière divine », est au cœur de l'art gothique, et que
  l'abside s'illumine « au soleil couchant » (`histore.txt` l.380, l.399, l.403).
- **Récompense :** Clé du Cloître (objet d'inventaire, déjà codé) → accès Étape 2.

### Étape 2 — Le cloître, Milon de Nanteuil et le coffre  (~12 min)
- **Lieu :** cloître. PNJ : le Moine puis l'**Évêque Milon de Nanteuil** (dialogues à
  menu déjà écrits dans `script.rpy`).
- **Mécaniques existantes :** dialogues à menu ; remise d'objets (parchemin + coffre) ;
  **cadenas 4 chiffres** (`inventory_coffre1`) ; **cryptex 5 lettres**
  (`inventory_cryptex`).
- **Faits enseignés (via les dialogues déjà codés) :**
  - Milon parle en **vieux français** ; il est chanoine dès 1206, prévôt en 1207, évêque
    en 1217 (l.364-365 du script ; cohérent avec le rôle historique de Milon).
  - L'ancienne cathédrale est **carolingienne**, du 10ᵉ s. (`histore.txt` l.3, l.6).
  - L'**art français** (« gothique ») est né à Saint-Denis grâce à l'**abbé Suger**
    (`histore.txt` l.383 ; rappelé par Milon dans le label `artfrancais`).
  - **1225** = année où l'ancienne cathédrale est détruite **et** où l'on décide de bâtir
    la nouvelle (`histore.txt` l.11, l.48, l.51).
- **Énigme 2A — Le coffre (cadenas 4 chiffres) :** Milon remet un coffre verrouillé.
  Indice donné dans le dialogue : « chaque date que je vous ai mentionnée est importante…
  et surtout **1225** » (déjà dans le script). Le joueur déduit que 1225 est *la* date
  fondatrice.
  - **Solution : `1225`** (déjà la solution codée du coffre).
  - **Récompense :** la brochure-plan (débloque la navigation par carte), le **cryptex**,
    et un **vieux parchemin scellé** (« parchemin mystère ») trouvé par Milon.
- **Énigme 2B — Le cryptex (5 lettres) :** le cryptex s'ouvre avec le **nom du « père »
  de l'art français**, en 5 lettres. Le dialogue de Milon a déjà donné la réponse : c'est
  l'abbé qui a mis en œuvre cet art à Saint-Denis.
  - **Solution : `SUGER`** (`histore.txt` l.383). *Remplace la solution de test
    actuelle ; voir Note d'implémentation.*
  - **Effet :** le cryptex ouvert mène à l'horloge astronomique (déjà : `Jump("Horloge")`).

### Étape 3 — L'accueil et le briefing  (~4 min)
- **Lieu :** kiosque d'accueil. PNJ : **Alexandre** (dialogue déjà codé).
- **Mécanique existante :** dialogue à menu ; carte/plan interactif (`plan_screen`).
- **Rôle :** Alexandre énonce les **trois gardiens du temps** à réveiller (déjà dans le
  script) — *« L'horloge astronomique ne fonctionne plus, l'orgue est complètement
  bloqué, et impossible d'entrer dans la sacristie ! »* Il explique que la clé de la
  sacristie a été « perdue dans le temps » en **deux morceaux**.
- **Déclenchement du chrono global d'1 h** à la sortie de ce dialogue.

### Étape 4 — 1ᵉʳ gardien : l'horloge astronomique  (~11 min)
- **Lieu :** scène de l'horloge astronomique. **Mécanique existante :** mini-jeu
  **Puzzle2** (reconstitution des pièces de l'horloge) + **minuteur 300 s** déjà présents
  (`puzzle.rpy`, `puzzle2_timer`).
- **Accès :** la grille de l'horloge exige une clé → fournie par le cryptex ouvert à
  l'Étape 2B (déjà : `cryptex → Jump("Horloge")`).
- **Faits enseignés (dialogue d'Alexandre + écran) :**
  - L'horloge astronomique a été construite par **Auguste-Lucien Vérité** entre **1865 et
    1868**, installée à partir de **1876** (`histore.txt` l.324-325).
  - Elle compte près de **90 000 pièces** et **52 cadrans** (l.307, l.325).
  - Le **coq chante 3 fois** aux heures, pour rappeler le reniement de saint Pierre ;
    il symbolise la **vigilance** (l.341).
- **Énigme 4 :** reconstituer le mécanisme déréglé de l'horloge (Puzzle2 — replacer et
  réorienter les pièces) **avant la fin du minuteur**.
- **Récompense :** le **1ᵉʳ morceau de la clé de la sacristie** (`morceau_cle_2`) se
  détache d'un cadran remis en place. (La vidéo « Découvrez l'horloge astronomique »,
  déjà présente dans `win_2`, sert de récompense pédagogique.)

### Étape 5 — 2ᵉ gardien : le grand orgue  (~9 min)
- **Lieu :** salle de l'orgue. **Mécanique existante :** mini-jeu de la **mélodie**
  (`minijeu_orgue.rpy` — jouer une séquence de notes au clavier).
- **Faits enseignés :**
  - Le grand orgue actuel a été **reconstruit après les bombardements de 1940** et
    **inauguré en 1979** (`histore.txt` l.103, l.272).
  - Il possède **77 jeux**, soit environ **5 500 tuyaux** ; les plus longs mesurent
    **11,70 m** (l.288).
  - Des orgues existaient déjà à Beauvais dès **1530** (l.275).
- **Énigme 5 :** l'orgue est « bloqué » ; seule une mélodie précise réveille ses rouages
  (déjà annoncé par Alexandre). La **partition** (séquence de 3 notes) est inscrite sur un
  objet trouvé en chemin — par ex. au dos de la brochure-plan obtenue au coffre.
  - **Mécanique :** jouer la séquence → `orgue_partition_1` (déjà codé).
- **Récompense :** un compartiment caché s'ouvre sur le pupitre (déjà :
  `orgue_melodie_secrete`) et délivre une **bougie** — objet nécessaire à l'Étape 6.

### Étape 6 — La Basse-Œuvre, le chœur et le message caché  (~13 min)
- **Lieux :** Basse-Œuvre (PNJ **Sœur Agnès**) et **chœur**.
- **Mécaniques existantes :** quête de PNJ (`quete_basse_oeuvre.rpy`) ; objet cliquable
  dans un décor (`salle_choeur`) ; mini-jeu **assemblage** (4 fragments) ; mini-jeu
  **message caché** (bougie + parchemin → encre invisible révélée à la flamme) ;
  **crafting**.
- **Faits enseignés :**
  - Basse-Œuvre : ancienne cathédrale du 10ᵉ s. préservée parce que la nef de la nouvelle
    ne fut jamais bâtie ; il ne reste que **3 travées sur 9** (`histore.txt` l.22, l.99).
  - Chœur : **voûte gothique la plus haute du monde** (~46,7 m) ; **effondrement en
    1284**, un **vendredi de novembre** ; reconstruction avec piliers intermédiaires
    (voûtes sexpartites) achevée vers 1347 (`histore.txt` l.61, l.65, l.71, l.123).
  - Vitraux du transept Sud : 16ᵉ s., **ateliers Le Prince**, **rose de la Création**
    (l.209, l.211).
- **Énigme 6A — La quête de Sœur Agnès :** Agnès a perdu ses lunettes (déjà codé). Le
  joueur va au **chœur**, trouve les lunettes sous un banc de prière (`trouver_lunettes`,
  déjà codé), les rapporte → Agnès remet le **2ᵉ morceau de clé** (`morceau_cle_1`).
- **Énigme 6B — La rose de la Création (assemblage) :** au chœur, un vitrail brisé en
  **4 fragments** doit être recomposé (mini-jeu `assemblage`). Réussite → indice
  pédagogique sur les ateliers Le Prince et l'art du vitrail « à son apogée » (l.462-463).
- **Énigme 6C — Le message caché :** le joueur **combine** (crafting) la **bougie**
  (Étape 5) avec le **parchemin mystère** (Étape 2). La recette
  `bougie + parchemin_mystere → parchemin_revele` est **déjà définie**
  (`crafting_system.rpy`) et lance le mini-jeu d'**encre invisible** : en promenant la
  flamme, le message apparaît.
  - **Message révélé :** la dernière catastrophe de la cathédrale — la **chute de la
    flèche en 1573** (`histore.txt` l.89) — qui donne le **code final** de la sacristie.

### Étape 7 — La clé, la sacristie et le départ de Milon  (~6 min)
- **Mécaniques existantes :** **crafting** ; **cadenas 4 chiffres**.
- **Énigme 7A — Reforger la clé :** combiner `morceau_cle_1` + `morceau_cle_2` →
  **`cle_rouillee`**. La recette est **déjà définie** dans `craft_recipes`.
- **Énigme 7B — Le cadenas de la sacristie :** la `cle_rouillee` donne accès à la
  sacristie, scellée par un dernier cadenas 4 chiffres.
  - **Indice :** le message caché de l'Étape 6C.
  - **Solution : `1573`** — année de l'effondrement de la flèche / tour-lanterne
    (`histore.txt` l.89).
- **Faits enseignés :** la tour-lanterne, achevée en 1569, culminait à **150 m** ; elle
  s'effondre **4 ans plus tard** (1573). C'est la dernière grande épreuve de l'édifice.
- **Finale :** dans la sacristie, le joueur atteint la faille. L'horloge médiévale du
  *Chanoine Musique* — « la plus ancienne horloge à carillon » (l.307, l.366) — sonne
  l'heure : la faille se referme et **Milon repart en 1225**. Le joueur a « gagné sa
  sortie » du présent avant la fin du chrono. Épilogue pédagogique : si la nef n'a jamais
  été achevée, c'est ce qui a permis de conserver la cathédrale carolingienne du 10ᵉ s.
  (`histore.txt` l.99).

---

## Récapitulatif des énigmes et solutions

| # | Lieu | Mécanique existante | Solution | Source `histore.txt` |
|---|------|--------------------|----------|----------------------|
| 1A | Extérieur Est | Hotspot caché | Trouver la clé du cloître | — (mécanique) |
| 1B | Mosaïque | `time_of_day` | Régler sur « soir » | l.380, l.399, l.403 |
| 2A | Cloître — coffre | Cadenas 4 chiffres | **1225** | l.11, l.48, l.51 |
| 2B | Cloître — cryptex | Cryptex 5 lettres | **SUGER** | l.383 |
| 4 | Horloge astronomique | Puzzle2 + minuteur | Reconstituer le mécanisme | l.307, l.324-325, l.341 |
| 5 | Orgue | Mélodie | Jouer la partition (3 notes) | l.103, l.272, l.288 |
| 6A | Basse-Œuvre / Chœur | Quête PNJ + objet décor | Rendre les lunettes | l.22, l.99 |
| 6B | Chœur | Assemblage 4 fragments | Recomposer la rose | l.209, l.211, l.462 |
| 6C | Inventaire | Crafting + encre invisible | bougie + parchemin | l.89 |
| 7A | Inventaire | Crafting | morceau_cle_1 + morceau_cle_2 | — (mécanique) |
| 7B | Sacristie | Cadenas 4 chiffres | **1573** | l.89 |

---

## Minutage indicatif (~60 min)

| Étape | Contenu | Durée |
|-------|---------|-------|
| 0 | Intro / faille | 2 min |
| 1 | Extérieurs + mosaïque | 8 min |
| 2 | Cloître + Milon + coffre + cryptex | 12 min |
| 3 | Accueil + briefing (départ du chrono) | 4 min |
| 4 | Horloge astronomique | 11 min |
| 5 | Orgue | 9 min |
| 6 | Basse-Œuvre + chœur + message caché | 13 min |
| 7 | Clé + sacristie + final | 6 min |
| **Total** | | **~65 min** (marge pour l'objectif d'1 h) |

---

## Chaîne de progression des objets

```
Clé du cloître ──> accès cloître
Coffre (1225) ──> Brochure-plan + Cryptex + Parchemin mystère
Cryptex (SUGER) ──> accès Horloge
Horloge (Puzzle2) ──> morceau_cle_2
Orgue (mélodie) ──> Bougie
Chœur (lunettes) ──> rendues à Agnès ──> morceau_cle_1
Bougie + Parchemin mystère ──> Message caché ──> code 1573
morceau_cle_1 + morceau_cle_2 ──> Clé rouillée ──> Sacristie
Sacristie (1573) ──> Final : départ de Milon
```

Chaque gardien réveillé (horloge, orgue, sacristie) correspond à l'un des trois problèmes
annoncés par Alexandre à l'Étape 3 — la boucle narrative est ainsi complète.

---

## Note d'implémentation (à réaliser dans un second temps)

Le scénario tient **presque entièrement** avec le code existant. Les seuls écarts à prévoir
lorsqu'on passera à la réalisation :

1. **Cryptex** : remplacer la solution de test actuelle par `SUGER` dans `screens_jeu.rpy`
   (`inventory_cryptex`) et `script.rpy`.
2. **Chrono global d'1 h** : généraliser le principe de `puzzle2_timer` en un compte à
   rebours permanent, démarré à l'Étape 3.
3. **Récompenses de clé** : faire délivrer `morceau_cle_2` par l'énigme de l'horloge et
   `morceau_cle_1` par Sœur Agnès (la quête remet déjà un « morceau de clé » :
   harmoniser les `item_id` avec la recette `craft_recipes`).
4. **Sacristie** : ajouter le lieu (scène + label) et son cadenas final `1573`.
5. **Parchemin mystère / bougie** : faire remettre `parchemin_mystere` par le coffre et
   `bougie` par le compartiment de l'orgue (recette `parchemin_revele` déjà définie).

Aucune mécanique nouvelle n'est nécessaire : tout repose sur du code déjà présent.
