#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ---CONSTANTES GÉNÉRALES---#

GRID_SIZE = 10  # taille de la grille : 10 x 10
LETTERS = [chr(letter_code) for letter_code in range(ord('A'), ord('A') + GRID_SIZE)]  # colonnes A → J

# États possibles d’une case :
SEA, MISSED_SHOT, HIT_SHOT, SUNK_SHOT = 0, 1, 2, 3
# Représentation visuelle dans la grille
SQUARE_STATE_REPR = [' ', 'X', '#', '-']


# ==============================
#   CLASSE SHIP (NAVIRE)
# ==============================

class Ship:
    """Représente un navire avec ses positions et son état."""

    def __init__(self, name, positions):
        # name : nom du navire (ex : "Cruiser")
        # positions : liste de tuples (ligne, colonne)
        self.name = name
        self.positions = {pos: True for pos in positions}  # True = intact, False = touché

    def is_hit(self, coord):
        """Vérifie si le tir touche une des cases du navire."""
        return coord in self.positions

    def record_shot(self, coord):
        """Enregistre le tir sur le navire et indique s’il est coulé."""
        if self.is_hit(coord):
            self.positions[coord] = False  # la case est maintenant touchée
            print("A ship has been hit!")
            if self.is_sunk():
                print(f"The ship {self.name} has been sunk!")
            return True  # le tir a touché
        return False  # le tir n’a pas touché

    def is_sunk(self):
        """Retourne True si toutes les cases du navire sont touchées."""
        return not any(self.positions.values())  # si aucune partie n’est intacte → coulé