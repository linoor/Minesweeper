import pygame
import colors

screen_size = 600, 500
# ustawianie wielkosci okna
global screen
screen = pygame.display.set_mode(screen_size)

# ustawienia tla
global background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(colors.orangeColor)

# event odliczania czasu
UPDATECLOCKEVENT = pygame.USEREVENT + 1
