#!/usr/bin/python
# -*- coding: utf-8 -*-
# Michał Pomarański
# grupa nr 3

# -*- coding: utf-8 -*-
""" Moduł zawierający globalne zmienne używane przez wszystkie klasy """
from optparse import OptionParser
import pygame
import os

def X_is_running():
    from subprocess import Popen, PIPE
    p = Popen(["xset", "-q"], stdout=PIPE, stderr=PIPE)
    p.communicate()
    return p.returncode == 0

if X_is_running():
    screen_height = 700
    screen_width = 615

    # ustawianie wielkosci okna
    global screen
    screen = pygame.display.set_mode([screen_width, screen_height])

    # ustawienia ikonki
    icon_path = os.path.join('ikonki', 'icon_saper.png')
    icon = pygame.image.load(icon_path).convert_alpha()
    os.path.join('ikonki', 'icon_saper.png')

    # czcionka
    counter_and_clock_font = os.path.join('ikonki', "Kenzo.otf")

    # ustawienia tla
    global background
    background = pygame.Surface(screen.get_size())
    background = background.convert()

    # ustawienie logo
    saper_logo = pygame.image.load(os.path.join('ikonki', 'saper_logo.png'))
    logo_pos = saper_logo.get_rect()
    logo_pos.centerx = background.get_rect().centerx
    logo_pos.y += 30

    # ustawienie ikonki refresh
    refresh = pygame.image.load(os.path.join('ikonki', 'refresh_saper.png'))
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

