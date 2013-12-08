import pygame, sys
from pygame.locals import *

pygame.init()
fps = pygame.time.Clock()

# ustawianie wielkosci okna
window = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Saper')

# glowna petla
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()