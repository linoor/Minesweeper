#!/usr/bin/python
# -*- coding: utf-8 -*-
# Michał Pomarański
# grupa nr 3

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
        self.image = pygame.image.load(os.path.join(ikonki_directory, 'aktywne.png'))
        self.image = self.image.convert()

    def uncover(self, exploded=False):
        """ metoda obsługująca kliknięcie lewym przyciskiem myszy na pole"""
        if self.mined and not exploded:
            self.image = pygame.image.load(os.path.join(ikonki_directory, 'mina.png'))
        elif self.mined and exploded:
            self.image = pygame.image.load(os.path.join(ikonki_directory, 'mina1.png'))
        else:
            # jesli dookola nie ma min, nie ustawiamy cyfry "0"
            self.image = pygame.image.load(os.path.join(ikonki_directory, 'nieaktywne.png'))
            # ustawianie napisu na polach
            if self.mines_surrounding != 0:
                self.image = pygame.image.load(
                    os.path.join(ikonki_directory, '%d.png') % self.mines_surrounding)
        self.covered = False

    def flag(self):
        """ metoda ustawiająca flagę jako tło """
        self.image = pygame.image.load(os.path.join(ikonki_directory, 'flag.png'))
        self.flagged = True

    def question(self):
        """ metoda ustawiająca pytajnik jako tło """
        self.flagged = False
        self.question = True
        self.image = pygame.image.load(os.path.join(ikonki_directory, 'mark.png'))

    def cover(self):
        """ metoda zasłaniająca pole"""
        self.flagged = False
        self.question = False
        self.image = pygame.image.load(os.path.join(ikonki_directory, 'aktywne.png'))

    def mine(self):
    	""" metoda ustawiająca bombę na polu """
        self.mined = True

    def showMine(self):
        if self.mined:
            self.image = pygame.image.load(os.path.join(ikonki_directory, 'mina.png'))


def main():
    pass

def help_text():
    help_message = """
Jest to klasa, której instancje odzwierciedlają pojedyńcze bloki planszy.

Autor: Michał Pomarański

Aby rozpocząć nową grę należy wcisnąć klawisz 'n' na klawiaturze lub kliknąć na napis 'SAPER'.

Saper korzysta z Pythona 2.7 oraz PyGame 1.9.1 dla Pythona 2.7

Aby zainstalować pygame pod Linuksem:
sudo apt-get install python-pygame

Aby uruchomić grę:
python main.py
"""
    print(help_message)

if __name__ == '__main__':
    parser = OptionParser()
    parser.print_help = help_text
    (options, args) = parser.parse_args()
