import pygame
import colors

screen_height = 650
screen_width = 550
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

saper_logo = pygame.image.load('ikonki/saper_logo.png')
logo_pos = saper_logo.get_rect()
logo_pos.centerx = background.get_rect().centerx
logo_pos.y += 30

# event odliczania czasu
UPDATECLOCKEVENT = pygame.USEREVENT + 1