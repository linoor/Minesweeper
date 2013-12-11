import pygame, sys
from pygame.locals import *

from minefield import *
from colors import *
from game import *
from difficulty import *

screen_size = 600, 500

def main():
	pygame.init()
	pygame.display.set_caption('Saper')

	# ustawianie wielkosci okna
	global screen
	screen = pygame.display.set_mode(screen_size)

	# ustawienia tla
	global background
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill(orangeColor)

	# Menu
	font = pygame.font.Font(None, 36)
	text = font.render("Saper!", 1, (10, 10, 10))
	textpos = text.get_rect()
	textpos.centerx = background.get_rect().centerx
	background.blit(text, textpos)

	#ustawianie planszy
	normal = Difficulty(550+29, 448+37*4, 10, "normal")
	game = Game(Minefield(screen, background, normal))
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