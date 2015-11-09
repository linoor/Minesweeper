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

        self.flagged_state = FlaggedState(self)
        self.question_state = QuestionState(self)
        self.covered_state = CoveredState(self)
        self.state = self.covered_state

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
        self.state = self.flagged_state.update()

    def question(self):
        """ metoda ustawiająca pytajnik jako tło """
        self.state = self.question_state.update()

    def cover(self):
        """ metoda zasłaniająca pole"""
        self.state = self.covered_state.update()

    def mine(self):
        """ metoda ustawiająca bombę na polu """
        self.mined = True

    def showMine(self):
        if self.mined:
            self.image = pygame.image.load(os.path.join(ikonki_directory, 'mina.png'))


class BlockState(object):
    def update(self):
        self.block.image = pygame.image.load(os.path.join(ikonki_directory, self.ikonka))
        return self


class FlaggedState(BlockState):
    def __init__(self, block):
        self.block = block
        self.ikonka = 'flag.png'

    def update(self):
        print("updating!")
        super(FlaggedState, self).update()
        self.block.flagged = True
        return self


class CoveredState(BlockState):
    def __init__(self, block):
        self.block = block
        self.ikonka = 'aktywne.png'

    def update(self):
        super(CoveredState, self).update()
        self.block.flagged = False
        self.block.question = False
        return self

class QuestionState(BlockState):
    def __init__(self, block):
        self.block = block
        self.ikonka = 'mark.png'

    def update(self):
        super(QuestionState, self).update()
        self.block.flagged = False
        self.block.question = True
        return self

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
