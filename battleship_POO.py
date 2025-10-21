#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ships import Ship, GRID_SIZE, LETTERS
from grid import Grid

# ==============================
#   CLASSE GAME (JEU PRINCIPAL)
# ==============================

class Game:
    """Classe principale qui gère le déroulement de la partie."""

    def __init__(self):
        self.grid = Grid()  # création d’une nouvelle grille de jeu
        self.setup_ships()  # placement initial des navires

    def setup_ships(self):
        """Place les navires selon la disposition fixe de l’exercice."""
        self.grid.add_ship(Ship("Aircraft Carrier", [(2, 2), (2, 3), (2, 4), (2, 5), (2, 6)]))
        self.grid.add_ship(Ship("Cruiser", [(4, 1), (5, 1), (6, 1), (7, 1)]))
        self.grid.add_ship(Ship("Destroyer", [(5, 3), (6, 3), (7, 3)]))
        self.grid.add_ship(Ship("Submarine", [(5, 8), (5, 9), (5, 10)]))
        self.grid.add_ship(Ship("Torpedo Boat", [(9, 5), (9, 6)]))

    def ask_for_coord(self):
        """Demande à l’utilisateur une coordonnée de tir (ex : A1, H8)."""
        valid_coord = False
        coord = None
        user_input = input("Enter your shot coordinates (ex: 'A1', 'H8') : ")

        # Vérifie la validité de l’entrée (2 ou 3 caractères)
        if 2 <= len(user_input) <= 3:
            letter, number = user_input[0].upper(), user_input[1:]
            if letter in LETTERS:
                try:
                    row = int(number)
                    column = ord(letter) - ord('A') + 1
                    if 1 <= row <= GRID_SIZE:
                        valid_coord = True
                        coord = (row, column)
                except ValueError:
                    pass  # si l’utilisateur saisit autre chose qu’un nombre
        if not valid_coord:
            print("Invalid coordinates, please try again.")
            return self.ask_for_coord()  # appel récursif si erreur
        return coord

    def play(self):
        """Boucle principale du jeu : tirs successifs jusqu’à ce que tous les navires soient coulés."""
        print("=== Welcome to the Object-Oriented Battleship Game! ===")

        while not self.grid.all_sunk():  # tant qu’il reste des navires
            self.grid.display()  # affiche la grille
            shot = self.ask_for_coord()  # demande la position du tir
            self.grid.fire(shot)  # exécute le tir
            print()

        # Fin de partie
        self.grid.display()
        print(" Congratulations! You sank all enemy ships! ")


# ==============================
#   EXÉCUTION DU PROGRAMME
# ==============================

if __name__ == "__main__":
    game = Game()  # création du jeu
    game.play()    # lancement de la partie

