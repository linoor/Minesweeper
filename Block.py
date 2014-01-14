"""klasa odwzwierciedlajaca pole"""

import pygame
import colors
from globals import *


class Block(pygame.sprite.Sprite):

    def __init__(self, posx, posy, size, i, j):
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
        self.image = pygame.image.load('ikonki/aktywne.png')
        self.image = self.image.convert()

    def uncover(self, exploded=False):
        if self.mined and not exploded:
            self.image = pygame.image.load('ikonki/mina.png')
        elif self.mined and exploded:
            self.image = pygame.image.load('ikonki/mina1.png')
        else:
            # jesli dookola nie ma min, nie ustawiamy cyfry "0"
            self.image = pygame.image.load('ikonki/nieaktywne.png')
            # ustawianie napisu na polach
            if self.mines_surrounding != 0:
                self.image = pygame.image.load(
                    'ikonki/%d.png' % self.mines_surrounding)
        self.covered = False

    def flag(self):
        self.image = pygame.image.load('ikonki/flag.png')
        self.flagged = True

    def question(self):
        self.flagged = False
        self.question = True
        self.image = pygame.image.load('ikonki/mark.png')

    def cover(self):
        self.flagged = False
        self.question = False
        self.image = pygame.image.load('ikonki/aktywne.png')

    def mine(self):
        self.mined = True


def main():
    pass

if __name__ == "__main__":
    main()
