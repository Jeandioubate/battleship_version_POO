#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ships import GRID_SIZE, LETTERS, SEA, MISSED_SHOT, HIT_SHOT, SUNK_SHOT, SQUARE_STATE_REPR

# ==============================
#   CLASSE GRID (GRILLE)
# ==============================

class Grid:
    """Représente la grille de jeu (10x10) et gère les tirs et les navires."""

    def __init__(self):
        self.ships = []  # liste des navires
        self.played_shots = set()  # ensemble des tirs effectués (coordonnées)

    def add_ship(self, ship):
        """Ajoute un navire sur la grille."""
        self.ships.append(ship)

    def get_ship_by_coord(self, coord):
        """Retourne le navire présent à une coordonnée donnée (ou None)."""
        for ship in self.ships:
            if ship.is_hit(coord):
                return ship
        return None

    def fire(self, coord):
        """Effectue un tir à la coordonnée donnée et affiche le résultat."""
        self.played_shots.add(coord)  # on ajoute la coordonnée aux tirs joués
        ship = self.get_ship_by_coord(coord)  # on cherche s’il y a un navire ici

        if ship:
            ship.record_shot(coord)  # on enregistre le tir sur le navire
            if ship.is_sunk():
                self.ships.remove(ship)  # le navire coulé est retiré de la flotte
        else:
            print("Your shot missed... It’s water!")

    def get_square_state(self, coord):
        """Retourne l’état actuel d’une case (mer, raté, touché, coulé)."""
        if coord not in self.played_shots:
            return SEA  # pas encore tiré ici

        ship = self.get_ship_by_coord(coord)
        if ship:
            return SUNK_SHOT if ship.is_sunk() else HIT_SHOT  # coulé ou simplement touché
        return MISSED_SHOT  # tir raté

    def display(self):
        """Affiche la grille du jeu mise à jour."""
        print('    ', end='')
        for x in range(GRID_SIZE):
            print(f' {LETTERS[x]}  ', end='')  # affichage des lettres de colonnes
        print()
        print('  ', '+---' * GRID_SIZE + '+')

        for row in range(1, GRID_SIZE + 1):
            print(f'{row:>2} |', end='')  # affichage du numéro de ligne
            for col in range(1, GRID_SIZE + 1):
                coord = (row, col)
                state = self.get_square_state(coord)
                print(f' {SQUARE_STATE_REPR[state]} |', end='')  # symbole selon l’état
            print()
            print('  ', '+---' * GRID_SIZE + '+')

    def all_sunk(self):
        """Retourne True si tous les navires sont coulés."""
        return len(self.ships) == 0
