# Le jeu de la bataille navale, version Programmation Orientée Objet

## 1. Description

Ce projet est une implémentation orientée objet du jeu de la Bataille Navale.

## 2. Structure du projet

```bash

Battleship_POO/    
| 
ships.py            # Contient la classe Ship et les constantes globales (grille, états, symboles)
|
grid.py             # Contient la classe Grid : gestion des tirs, navires et affichage
|
battleship_POO.py   # Fichier principal : contient la classe Game et la boucle de jeu
|
README.md           # Documentation du projet
```
## 3. Fonctionnalités principales

- Grille 10 x 10 avec colonnes A -> J et lignes 1 -> 10
- Placement fixe des navires selon le schéma fourni dans l'exo
- Gestion des tirs : raté, touché, coulé
- Affichage dynamique de la grille après chaque tir
- Détection automatique de fin de partie (tous les navires coulés)

## 4. Détails des fichiers

### ```ships.py```

Ce module contient :
- les constantes globales
- la classe ```Ship```, qui gère :
    - le nom du navire,
    - ses positions
    - son état
    - les méthodes :
        - ```is_hit()``` : vérifie si une coordonnée touche le navire,
        - ```record_shot()``` : enregistre un tir et affiche les messages correspondants,
        - ```is_sunk()``` : indique si le navire est entièrement coulé

### ```grid.py```

Ce module contient la classe ```Grid```, responsable de :
- gérer la liste des navires sur la grille,
- stocker les tirs déjà joués,
- déterminer si un tir touche ou rate un navire,
- afficher la grille actualisée après chaque tour,
- vérifier si tous les navires sont coulés (```all_sunk()```).

Méthodes principales :
- ```add_ship(ship)``` : ajoute un navire à la grille.
- ```fire(coord)``` : gère la logique d'un tir.
- ```get_square_state(coord)``` : retourne l'état d'une case (mer, raté, touché, coulé)
- ```display()``` : affiche la grille dans le terminal.

### ```battleship_POO.py```

C'est le fichier principal du projet.
Il contient la classe ```Game```, qui gère le déroulement complet du jeu.

Méthodes principales :

- ```setup_ships()``` : place les navires à leurs positions fixes.
- ```ask_for_coord()``` : demande au joueur une coordonnée de tir et la valide.
- ```play()``` : boucle principale du jeu :
    1. affiche la grille,
    2. demande une position au joueur,
    3. exécute le tir,
    4. vérifie si la partie est terminée
    
