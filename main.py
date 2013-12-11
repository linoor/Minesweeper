import pygame, sys
from pygame.locals import *

from minefield import *
from colors import *
from game import *

def main():
	pygame.init()
	pygame.display.set_caption('Saper')

	# ustawianie wielkosci okna
	global screen
	screen = pygame.display.set_mode((600, 500))

	# ustawienia tla
	global background
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill(orangeColor)

	# ustawianie napisów
	font = pygame.font.Font(None, 36)
	text = font.render("Saper!", 1, (10, 10, 10))
	textpos = text.get_rect()
	textpos.centerx = background.get_rect().centerx
	background.blit(text, textpos)

	#ustawianie planszy
	game = Game(Minefield(screen, background, screen.get_size()[0], screen.get_size()[1]))
	game.new_game()

	screen.blit(background, (0,0))
	pygame.display.flip()

	# glowna petla
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()

			screen.blit(background, (0,0))
			pygame.display.flip()

if __name__ == '__main__':
	main()