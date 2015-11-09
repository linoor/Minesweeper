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

        self.flagged_state = FlaggedState(self)
        self.question_state = QuestionState(self)
        self.covered_state = CoveredState(self)
        self.mined_state = MinedState(self)
        self.exploded_state = ExplodedState(self)
        self.not_mined_uncovered_state = NotMinedUncoveredState(self)
        self.state = self.covered_state
        
        self.init_image()
        self.rect = self.image.get_rect()

    def init_image(self):
        """ inicjalizacja tła"""
        self.state = self.covered_state.update()
        # self.image = pygame.image.load(os.path.join(ikonki_directory, 'aktywne.png'))
        self.image = self.image.convert()

    def uncover(self, exploded=False):
        """ metoda obsługująca kliknięcie lewym przyciskiem myszy na pole"""
        if self.mined and not exploded:
            self.state = self.mined_state.update()
        elif self.mined and exploded:
            self.state = self.exploded_state.update()
        else:
            self.state = self.not_mined_uncovered_state.update()

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
            self.state = self.mined_state.update()


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


class MinedState(BlockState):
    def __init__(self, block):
        self.block = block
        self.ikonka = 'mina.png'

    def update(self):
        super(MinedState, self).update()
        self.block.covered = False
        return self


class ExplodedState(BlockState):
    def __init__(self, block):
        self.block = block
        self.ikonka = 'exploded.png'

    def update(self):
        super(ExplodedState, self).update()
        self.block.covered = False
        return self


class NotMinedUncoveredState(BlockState):
    def __init__(self, block):
        self.block = block
        self.ikonka = 'nieaktywne.png'

    def update(self):
        mines_surrounding = self.block.mines_surrounding
        if mines_surrounding != 0:
            self.ikonka = '%d.png' % mines_surrounding
        super(NotMinedUncoveredState, self).update()
        self.block.covered = False
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