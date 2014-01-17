# -*- coding: utf-8 -*-
""" Moduł zawierający globalne zmienne używane przez wszystkie klasy """
import pygame
import os
import colors

screen_height = 700
screen_width = 615
# ustawianie wielkosci okna
global screen
screen = pygame.display.set_mode([screen_width, screen_height])

# czcionka
counter_and_clock_font = os.path.join('ikonki', "Kenzo.otf")

# ustawienia tla
global background
background = pygame.Surface(screen.get_size())
background = background.convert()

saper_logo = pygame.image.load(os.path.join('ikonki', 'saper_logo.png'))
logo_pos = saper_logo.get_rect()
logo_pos.centerx = background.get_rect().centerx
logo_pos.y += 30

# event odliczania czasu
UPDATECLOCKEVENT = pygame.USEREVENT + 1


def main():
    pass

if __name__ == "__main__":
    main()
