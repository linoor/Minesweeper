#!/usr/bin/python
# -*- coding: utf-8 -*-
# Michał Pomarański
# grupa nr 3

# -*- coding: utf-8 -*-
""" główna klasa obsługująca całą grę"""
from optparse import OptionParser

from Block import Block
from counter import Counter
import pygame
import os
import globals
from clock import *
import colors

# DEBUG MODE
DEBUG = False


class Game:

    def __init__(self, minefield):
        self.clock = 0
        self.minefield = minefield
        self.clickable = True
        self.clock = None
        self.first_click = True

        # ustawienia licznika
        self.counter = None

        # napis wygranej/przegranej
        self.text = None

    def init_counter(self):
    	""" inicjalizacja licznika"""
        rect = self.minefield.game_area_pos
        size = 27
        pos = pygame.Rect(rect)
        pos.x = rect.right - 20
        pos.y -= (10 + size)
        self.counter = Counter(self.minefield.difficulty.mines_number, pos)

    def init_clock(self):
    	""" inicjalizacja zegara"""
        rect = self.minefield.game_area_pos
        size = 27
        # pozycja zegara
        pos = pygame.Rect(rect)
        pos.x = rect.left
        pos.y -= (10 + size)
        # ustawianie sprite'a zegara
        return Clock(pos)

    def find_collide_rect(self, pos):
    	""" metoda sprawdzająca które pole zostało kliknięte """
        for b in self.minefield.get_blocks():
            if b.rect.collidepoint(pos):
                return b

    def left_click(self, pos):
    	""" metoda obsługująca lewe kliknięcie myszki """
        if self.clickable:

            # znajdujemy kliniete pole
            b = self.find_collide_rect(pos)

            if b:
                 # jesli pierwsze klikniecie, to rozpoczynamy odliczenie zegara
                if self.first_click:
                    self.first_click = False
                    self.minefield.set_mines(b)
                    self.clock.start_clock()

                if b.covered and not b.flagged and not b.question:
                    if b.mines_surrounding == 0:
                        self.minefield.ripple_effect(b)
                    else:
                        b.uncover()

            if self.is_game_over():
                self.end_game(b)
            self.minefield.update()

    def right_click(self, pos):
    	""" metoda obsługująca prawe kliknięcie myszki """
        if self.clickable:
            b = self.find_collide_rect(pos)
            if b:
                if b.covered:
                    if not b.flagged and not b.question and self.counter.mines > 0:
                        b.flag()
                        # update counter
                        self.counter.mines -= 1
                        self.counter.update()
                    elif b.flagged:
                        Block.question(b)
                        # update counter
                        self.counter.mines += 1
                        self.counter.update()
                    elif b.question:
                        b.cover()
                # print(b.rect)
                # print(pos)

            if self.is_game_over():
                self.end_game(b)
            self.minefield.update()

    def is_game_over(self):
    	""" metoda sprawdzająca czy gra została zakonczona (wygrana lub przegrana gracza)"""
        # jesli miny jeszcze nie sa ustawione
        if not self.minefield.are_mines_set:
            return False
        # jesli trafimy na mine
        if any(not b.covered and b.mined for b in self.minefield.get_blocks()):
            return True
        # jesli oflagujemy wszystkie miny
        # wszystkie pola ktore sa zaminowane musza byc oflagowane
        if all(b.flagged for b in self.minefield.get_blocks() if b.mined):
            return True
        # jesli odkryjemy wszystkie niezaminowane pola
        if all(not b.covered for b in self.minefield.get_blocks() if not b.mined):
            return True

        return False

    def end_game(self, clicked_block):
    	""" metoda koncząca grę (pokazanie wszystkich min, pokazanie napisu wygranej/przegranej, zatrzymanie zegara)"""
        # wygrana
        if self.check_win():
            self.text = pygame.image.load(os.path.join(globals.ikonki_directory, 'won.png'))
        # przegrana
        else:
            self.text = pygame.image.load(os.path.join(globals.ikonki_directory, 'lose.png'))
        # odkrywanie wszystkich min
        self.minefield.uncover_mines(clicked_block)
        # umiejscowienie napisu
        textpos = self.text.get_rect()
        textpos.centerx = self.minefield.game_area_pos.centerx
        textpos.y = self.minefield.game_area_pos.top - 27 - 10
        globals.background.blit(self.text, textpos)
        # wylaczenie mozliwosci odkrywania pol
        self.clickable = False
        # wylaczenie zegara
        self.clock.stop_clock()

    def new_game(self):
    	""" Metoda rozpoczynająca nową grę. """
        self.minefield.draw()
        if not self.clock:
            self.clock = self.init_clock()
        # czyszczenie grafik
        self.clock.clear_clock()
        self.clock.stop_clock()
        self.clock.show_clock()
        self.init_counter()
        self.counter.clear_counter()
        self.counter.show_counter()
        self.clear_win_lose()

    def check_win(self):
    	""" Metoda sprawdzająca czy gracz wygrał """
        # jesli trafimy na mine - przegrana
        if any(b.mined and not b.covered for b in self.minefield.get_blocks()):
            return False
        return True

    def update_clock(self):
        self.minefield.update()
        self.clock.update()

    def clear_win_lose(self):
    	""" metoda usuwająca napis wygranej/przegranej """
        tmp = pygame.Surface((110, 30))
        tmp.fill(colors.backgroundColor)
        tmp_pos = tmp.get_rect()
        tmp_pos.centerx = self.minefield.game_area_pos.centerx
        tmp_pos.y = self.minefield.game_area_pos.top - 27 - 10
        globals.background.blit(tmp, tmp_pos)

    def turn_on_cheats(self):
        for b in self.minefield.get_blocks():
            b.showMine()


def main():
    pass

def help_text():
    help_message = """
Jest to klasa, której instancja jest odpowiedzialna za sterowanie przebiegiem gry (np. rozpoczynanie nowej gry).

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

