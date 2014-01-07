import pygame
import colors

screen_height = 600
screen_width = 500
# ustawianie wielkosci okna
global screen
screen = pygame.display.set_mode([screen_width, screen_height])

#czcionka
font = "Kenzo.otf"
counter_and_clock_font = "Kenzo.otf"

# ustawienia tla
global background
background = pygame.Surface(screen.get_size())
background = background.convert()

# event odliczania czasu
UPDATECLOCKEVENT = pygame.USEREVENT + 1