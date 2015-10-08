#!/usr/bin/python
# -*- coding: utf-8 -*-
# Michał Pomarański
# grupa nr 3

# -*- coding: utf-8 -*-
""" moduł ze wszystkimi kolorami użytymi w programie """
from optparse import OptionParser
import pygame
import os
# kolory
whiteColor = pygame.Color(250, 250, 250)
redColor = pygame.Color(255, 0, 0)
game_area_color = pygame.Color("#c4c4c4")
orangeColor = pygame.Color(255, 201, 0)
uncoveredColor = pygame.Color(0, 147, 191)
coveredColor = pygame.Color(41, 156, 0)
questionColor = pygame.Color(0, 255, 153)
bombColor = pygame.Color(200, 0, 255)
bombhint = pygame.Color(250, 192, 106)
backgroundColor = pygame.Color("#33A8E0")
napisyColor = pygame.Color("#FFFFFF")
shadowColor = pygame.Color("#298bcb")


def main():
    pass

def help_text():
    help_message = """
W tym skrypcie zapisane są zmienne, które przechowują kolory (pygame.Color).

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

