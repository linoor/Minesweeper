#!/usr/bin/python
# -*- coding: utf-8 -*-
# Michał Pomarański
# grupa nr 3

# -*- coding: utf-8 -*-
""" klasas obsługująca zegarek """
from optparse import OptionParser

import globals
import colors
import pygame
import os
import inspect


class Clock:

    def __init__(self, pos):
    	""" początkowe wartości"""
        self.time = 0
        self.pos = pos
        self.running = False

    def show_clock(self):
    	""" metoda wyświetlająca zegar """
        ikona_zegara = pygame.image.load(os.path.join('ikonki', 'zegarek.png'))
        clock_font = pygame.font.Font(globals.counter_and_clock_font, 27)
        text = clock_font.render(
            str(self.time).zfill(2), 1, colors.napisyColor)
        globals.background.blit(ikona_zegara, self.pos)
        # ustawianie pozycji
        pos2 = pygame.Rect(self.pos)
        pos2.x += 25
        pos2.y -= 2
        # ustawianie cienia
        clock_shadow = clock_font.render(
            str(self.time).zfill(2), 1, colors.shadowColor)
        shadow_pos = pygame.Rect(pos2)
        shadow_pos.x += 2
        shadow_pos.y += 2

        globals.background.blit(clock_shadow, shadow_pos)
        globals.background.blit(text, pos2)

    def update(self):
    	""" metoda zwiększająca czas """
        # jesli gra sie zakonczyla, zatrzymaj zegar
        if not self.running:
            return
        self.time += 1
        self.clear_clock()
        self.show_clock()

    def clear_clock(self):
    	""" metoda usuwająca zegar """
        tmp = pygame.Surface((3 * 36 + 2, 30))
        tmp.fill(colors.backgroundColor)
        globals.background.blit(tmp, self.pos)

    def start_clock(self):
    	""" metoda rozpoczynająca odliczanie zegara"""
        pygame.time.set_timer(globals.UPDATECLOCKEVENT, 1000)
        self.running = True

    def stop_clock(self):
    	""" metoda zatrzymująca odliczanie zegara """
        self.running = False


def main():
    pass

def help_text():
    help_message = """
Jest to klasa, której instancja jest odpowiedzialna, za mierzenie czasu gry.

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

