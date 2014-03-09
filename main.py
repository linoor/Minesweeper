# -*- coding: utf-8 -*-

import pygame
import os
import sys
from pygame.locals import *

from minefield import *
from colors import *
from game import *
from difficulty import *
from globals import *


def start_new_game(difficulty):
    """ funkcja rozpoczynająca nową grę """
    game = Game(Minefield(difficulty))
    game.new_game()
    return game


def initialize_screen():
    """ funkcja ustawiająca okno oraz tło"""
    # menu
    background.fill(colors.backgroundColor)
    background.blit(saper_logo, logo_pos)
    background.blit(refresh, refresh_pos)


def main():
    """ główna funkcja programu """
    pygame.font.init()
    pygame.init()
    pygame.display.set_caption('Saper')

    # ustawianie ikony
    pygame.display.set_icon(icon)

    initialize_screen()

    # ustawianie planszy
    easy = Difficulty(20, 20, 40, 25, "easy")

    pygame.display.flip()

    # rozpoczynanie gry
    game = start_new_game(easy)

    # glowna petla
    while True:
        for event in pygame.event.get():
        	# obsługa kliknięcia przycisku zamykania programu
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # obsługa klawiszy
            if event.type == KEYDOWN:
            	# obsługa przycisku ESC
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                # obsługa przycisku 'n'
                if event.key == K_n:
                    game = start_new_game(easy)

            if event.type == MOUSEBUTTONDOWN:  # handler poruszania myszka
            	# jeżeli lewe kliknięcie myszki
                if event.button == 1:
                    # sprawdzamy czy gracz kliknął napis SAPER
                    if logo_pos.collidepoint(event.pos) or refresh_pos.collidepoint(event.pos):
                        game = start_new_game(easy)

                    # obsługa kliknięcia na pola
                    game.left_click(event.pos)
            	# obsługa prawego klikniecią myszki
                if event.button == 3:
                    game.right_click(event.pos)
            # obsługa zegara
            if event.type == UPDATECLOCKEVENT:
                game.update_clock()

            # update obrazków
            screen.blit(background, (0, 0))

            pygame.display.flip()

if __name__ == '__main__':
    main()
