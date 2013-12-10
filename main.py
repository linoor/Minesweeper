import pygame, sys
from pygame.locals import *

# kolory 
whiteColor = pygame.Color(250, 250, 250)

def main():
	pygame.init()
	pygame.display.set_caption('Saper')

	# ustawianie wielkosci okna
	screen = pygame.display.set_mode((640, 480))

	# ustawienia tla
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill(whiteColor)

	screen.blit(background, (0,0))
	pygame.display.flip()

	# glowna petla
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			screen.blit(background, (0,0))
			pygame.display.flip()

if __name__ == '__main__':
	main()