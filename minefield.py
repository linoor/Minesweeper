#!/usr/bin/python
# -*- coding: utf-8 -*-
# Michał Pomarański
# grupa nr 3

# -*- coding: utf-8 -*-
""" Jedna z głównych klas obsługująca planszę """

import pygame
import os
import colors
from Block import *
import random
import globals
import itertools
import time

# DEBUG MODE
DEBUG = True
calls = 0


class Minefield:

    def __init__(self, difficulty):
        self.mines_left = difficulty.mines_number
        self.difficulty = difficulty
        self.blocks = []
        self.game_area = None
        self.are_mines_set = False
        self.rows = 0
        self.columns = 0

    def get_blocks(self):
    	""" Zwraca jednowymiarową tablicę wszystkich pól """
        return list(itertools.chain.from_iterable(self.blocks))

    def set_mines(self, block):
    	""" Losuje pola, które mają być zaminowane oraz ustawia na nich miny """
        random.seed()
        mines_set = 0
        mines_to_set = self.difficulty.mines_number
        
        while mines_set != mines_to_set:
            blocks = self.get_blocks()
            selected_block = blocks[random.randint(0, len(blocks) - 1)]
            if block != selected_block and not selected_block.mined:
                mines_set += 1
                selected_block.mine()
                blocks.remove(block)

        self.set_mines_surrounding()
        self.are_mines_set = True

    def set_mines_surrounding(self):
        for i in range(len(self.blocks)):
            for j in range(len(self.blocks[i])):
                if self.blocks[i][j].mined:
                    self.set_mines_around(i, j)

    def set_mines_around(self, i, j):
    	""" Metoda pomocnicza sprawdzająca ile min jest ustawionych dookoła każdego pola """

        for n in range(i - 1, i + 2):
            for m in range(j - 1, j + 2):
                if n < self.rows and m < self.columns and n >= 0 and m >= 0 and self.blocks[n][m]:
                    self.blocks[n][m].mines_surrounding += 1

    def ripple_effect(self, block):
    	""" Metoda odkrywa pola rekurencyjnie dopóki natrafia na pola nieotoczone minami """
        if not block.covered:
            return
        if block.mined or block.flagged or block.question:
            return
        block.uncover()
        if block.mines_surrounding != 0:
            return

        row_clicked, column_clicked = self.find(block)
        blocks = self.blocks
        for i in range(3):
            for j in range(3):
                current_row = row_clicked + i - 1
                current_column = column_clicked + j - 1
                try:
                    if current_row >= self.rows or current_column >= self.columns:
                        continue
                    if current_row < 0 or current_column < 0:
                        continue
                    if blocks[current_row][current_column].covered:
                        self.ripple_effect(blocks[current_row][current_column])
                except IndexError as e:
                    #print(current_row, current_column)
                    pass
        return

    def find(self, elem):
    	""" metoda znajdująca obiekt danego pola"""
        for row, i in enumerate(self.blocks):
            try:
                column = i.index(elem)
            except ValueError:
                continue
            return row, column
        return -1

    def draw(self):
    	""" metoda wyświetlająca planszę """
        self.init_game_area()
        self.init_blocks()
        self.update()

    def update(self):
    	""" metoda wyświetlająca planszę po kliknięciu myszki """
        for b in self.get_blocks():
            self.game_area.blit(b.image, (b.posx, b.posy))
        globals.background.blit(self.game_area, (self.game_area_pos))

    def init_blocks(self):
    	""" inicjalizacja planszy """
        size = 25
        padding = 1
        posx, posy = padding, padding
        tmp_block = []
        i, j = 0, 0
        while posy + size < self.difficulty.height:
            j += 1
            block = self.create_block(posx, posy, size, i, j)
            tmp_block.append(block)
            posx += size + padding
            # nowy rzad
            if posx + size > self.difficulty.width:
                i += 1
                j = 0
                posx = padding
                posy += size + padding
                self.blocks.append(tmp_block)
                tmp_block = []
        self.rows = len(self.blocks)
        self.columns = len(self.blocks[0])

    def create_block(self, posx, posy, size, i, j):
    	""" Metoda tworzy nowe pole """
        block = Block(posx, posy, size, i, j)
        offset = self.game_area_pos.topleft
        block.rect.topleft = (posx + offset[0], posy + offset[1])
        return block

    def init_game_area(self):
    	""" Metoda tworząca planszę """
        size = self.difficulty.width, self.difficulty.height
        self.game_area = pygame.Surface(size)
        self.game_area = self.game_area.convert()
        self.game_area.fill(colors.game_area_color)
        self.game_area_pos = self.game_area.get_rect()
        self.game_area_pos.centerx = globals.background.get_rect().centerx
        self.game_area_pos.bottom = globals.background.get_rect().height - 30

        # ustawianie cienia planszy
        left_bottom = self.game_area_pos.bottomleft
        bottom_right = self.game_area_pos.bottomright
        top_right = self.game_area_pos.topright
        screen_right = (globals.screen.get_rect().right, top_right[1] + 25)
        screen_rightbottom = globals.screen.get_rect().bottomright
        screen_leftbottom = (
            left_bottom[0] + 25, globals.screen.get_rect().bottom)

        pygame.draw.polygon(background, colors.shadowColor, [
            left_bottom,
            bottom_right,
            top_right,
            screen_right,
            screen_rightbottom,
            screen_leftbottom,
            left_bottom])

    def debug(self):
    	""" Metoda która pokazuje gdzie ukryte są miny (tylko dla trybu debugowania) """
        for b in self.get_blocks():
            if b.mined:
                b.image.fill(colors.bombhint)

    def uncover_mines(self, clicked_block):
    	""" Metoda odsłaniająca wszystkie pola """
        for b in self.get_blocks():
            if b.mined and b != clicked_block:
                b.uncover()
            if b.mined and b == clicked_block:
                b.uncover(exploded=True)


def main():
    pass

def help_text():
    help_message = """
Skrypt zawiera klasę, której instancja jest odpowiedzialna za tworzenie Planszy (zawiera instancje klasy Block).

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

