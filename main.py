#!/usr/bin/python
# -*- coding: utf-8 -*-
# Michał Pomarański
# grupa nr 3

# -*- coding: utf-8 -*-

import sys
from pygame.locals import *

from minefield import *
from game import *
from difficulty import *


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

    if not X_is_running():
        print("By móc uruchomić tę grę potrzebujesz środowiska graficznego (X Window System).")
        exit()

    pygame.font.init()
    pygame.init()

    pygame.display.set_caption('Saper')

    # ustawianie ikony
    pygame.display.set_icon(icon.convert_alpha())

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
                # kody do debugowania
                if event.key == K_q:
                    game.turn_on_cheats()

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


def help_text():
    help_message = """
Jest to główny skrypt, za pomocą którego możemy uruchomić grę (python main.py).

Saper napisany w Pygame.

Autor: Michał Pomarański

Aby rozpocząć nową grę należy wcisnąć klawisz 'n' na klawiaturze lub kliknąć na napis 'SAPER'.

Saper korzysta z Pythona 2.7 oraz PyGame 1.9.1 dla Pythona 2.7

Aby zainstalować pygame pod Linuksem:
sudo apt-get install python-pygame

Aby gra działała X Window System powinien być włączony.

Aby uruchomić grę:
python main.py
"""
    print(help_message)


if __name__ == '__main__':

    parser = OptionParser()
    parser.print_help = help_text
    (options, args) = parser.parse_args()

    main()
