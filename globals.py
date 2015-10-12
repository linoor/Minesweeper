#!/usr/bin/python
# -*- coding: utf-8 -*-
# Michał Pomarański
# grupa nr 3

# -*- coding: utf-8 -*-
""" Moduł zawierający globalne zmienne używane przez wszystkie klasy """
from optparse import OptionParser
import pygame
import os
import sys
from difficulty import Difficulty


def X_is_running():
    from subprocess import Popen, PIPE
    p = Popen(["xset", "-q"], stdout=PIPE, stderr=PIPE)
    p.communicate()
    return p.returncode == 0

is_help = len(sys.argv) > 1 \
          and (
              sys.argv[1] == '--h' or sys.argv[1] == '--help' or sys.argv[1] == '-h'
          )

directory_path = os.path.dirname(os.path.abspath(__file__))
ikonki_directory = os.path.join(directory_path, 'ikonki')


difficulties = {
    "easy": Difficulty(20, 20, 40, 25, "easy", 615),
    "medium": Difficulty(30, 20, 60, 25, "medium", 815),
    "hard": Difficulty(40, 20, 80, 25, "hard", 1115)
}

chosen_difficulty = difficulties['easy']

if len(sys.argv) == 3 \
        and sys.argv[1] == '--difficulty' \
        and sys.argv[2] in difficulties.keys():
    chosen_difficulty = difficulties[sys.argv[2]]
else:
    chosen_difficulty = difficulties["easy"]

if X_is_running() and not is_help:
    screen_height = 700
    screen_width = chosen_difficulty.screen_width

    # ustawianie wielkosci okna
    global screen
    screen = pygame.display.set_mode([screen_width, screen_height])

    # ustawienia ikonki
    icon_path = os.path.join(ikonki_directory, 'icon_saper.png')
    icon = pygame.image.load(icon_path).convert_alpha()
    os.path.join(ikonki_directory, 'icon_saper.png')

    # czcionka
    counter_and_clock_font = os.path.join(ikonki_directory, "Kenzo.otf")

    # ustawienia tla
    global background
    background = pygame.Surface(screen.get_size())
    background = background.convert()

    # ustawienie logo
    saper_logo = pygame.image.load(os.path.join(ikonki_directory, 'saper_logo.png'))
    logo_pos = saper_logo.get_rect()
    logo_pos.centerx = background.get_rect().centerx
    logo_pos.y += 30

    # ustawienie ikonki refresh
    refresh = pygame.image.load(os.path.join(ikonki_directory, 'refresh_saper.png'))
    refresh_pos = refresh.get_rect()
    refresh_pos.topright = background.get_rect().topright
    refresh_pos.x -= 75
    refresh_pos.y += 35

    # event odliczania czasu
    UPDATECLOCKEVENT = pygame.USEREVENT + 1

def help_text():
    help_message = """
Skrypt, w których przechowywane są zmienne globalne.

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

