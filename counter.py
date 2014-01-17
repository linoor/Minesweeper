# -*- coding: utf-8 -*-
""" klasas obsługująca licznik pozostałych nieznalezionych jeszcze min"""
import globals
import colors
import pygame
import os


class Counter:

    def __init__(self, mines, pos):
        self.mines = mines
        self.pos = pos
        self.show_counter()

    def show_counter(self):
        """ metoda wyświetlająca licznik """
        ikona_bomby = pygame.image.load(os.path.join('ikonki', 'bomba.png'))
        counter_font = pygame.font.Font(globals.counter_and_clock_font, 27)
        text = counter_font.render(
            str(self.mines).zfill(2), 1, colors.napisyColor)

        # ustawianie cienia
        counter_shadow = counter_font.render(
            str(self.mines).zfill(2), 1, colors.shadowColor)
        shadow_pos = pygame.Rect(self.pos)
        shadow_pos.x += 2
        shadow_pos.y += 2

        globals.background.blit(counter_shadow, shadow_pos)
        globals.background.blit(text, self.pos)
        pos2 = pygame.Rect(self.pos)
        pos2.right -= 25
        pos2.y -= 1

        globals.background.blit(ikona_bomby, pos2)

    def update(self):
    	""" metoda zmieniająca licznik """
        # jesli gra sie zakonczyla, zatrzymaj zegar
        if self.mines < 0:
            return
        self.clear_counter()
        self.show_counter()

    def clear_counter(self):
    	""" metoda usuwająca licznik """
        tmp = pygame.Surface((3 * 36 + 2, 30))
        tmp.fill(colors.backgroundColor)
        globals.background.blit(tmp, self.pos)


def main():
    pass

if __name__ == "__main__":
    main()
