# -*- coding: utf-8 -*-
"""klasa odwzwierciedląjaca jedno konkretne pole na planszy"""

import pygame
import os
import colors
from globals import *


class Block(pygame.sprite.Sprite):

    def __init__(self, posx, posy, size, i, j):
        """ inicjalizacja stanow pola, ustawianie tła itd."""
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.covered = True
        self.mined = False
        self.flagged = False
        self.question = False
        self.mines_surrounding = 0
        self.posx = posx
        self.posy = posy
        self.indexes = i, j
        self.init_image()
        self.rect = self.image.get_rect()

    def init_image(self):
        """ inicjalizacja tła"""
        self.image = pygame.image.load(os.path.join('ikonki', 'aktywne.png'))
        self.image = self.image.convert()

    def uncover(self, exploded=False):
        """ metoda obsługująca kliknięcie lewym przyciskiem myszy na pole"""
        if self.mined and not exploded:
            self.image = pygame.image.load(os.path.join('ikonki', 'mina.png'))
        elif self.mined and exploded:
            self.image = pygame.image.load(os.path.join('ikonki', 'mina1.png'))
        else:
            # jesli dookola nie ma min, nie ustawiamy cyfry "0"
            self.image = pygame.image.load(os.path.join('ikonki', 'nieaktywne.png'))
            # ustawianie napisu na polach
            if self.mines_surrounding != 0:
                self.image = pygame.image.load(
                    os.path.join('ikonki', '%d.png') % self.mines_surrounding)
        self.covered = False

    def flag(self):
        """ metoda ustawiająca flagę jako tło """
        self.image = pygame.image.load(os.path.join('ikonki', 'flag.png'))
        self.flagged = True

    def question(self):
        """ metoda ustawiająca pytajnik jako tło """
        self.flagged = False
        self.question = True
        self.image = pygame.image.load(os.path.join('ikonki', 'mark.png'))

    def cover(self):
        """ metoda zasłaniająca pole"""
        self.flagged = False
        self.question = False
        self.image = pygame.image.load(os.path.join('ikonki', 'aktywne.png'))

    def mine(self):
    	""" metoda ustawiająca bombę na polu """
        self.mined = True


def main():
    pass

if __name__ == "__main__":
    main()
