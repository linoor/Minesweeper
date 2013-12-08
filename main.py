import pygame, sys
from pygame.locals import *

pygame.init()
fps = pygame.time.Clock()

# ustawianie okna
window = pygame.display.set_mode((640, 480))

# glowna petla
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()