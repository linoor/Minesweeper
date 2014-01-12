import pygame, sys
from pygame.locals import *

from minefield import *
from colors import *
from game import *
from difficulty import *
from globals import *

def start_new_game(difficulty):
	game = Game(Minefield(difficulty))
	game.new_game()
	return game

def initialize_screen():
	#menu
	background.fill(colors.backgroundColor)
	background.blit(saper_logo, logo_pos)

def main():
	pygame.font.init()
	pygame.init()
	pygame.display.set_caption('Saper')

	initialize_screen()

	#ustawianie planszy
	easy = Difficulty(20, 20, 40, 25, "easy")

	pygame.display.flip()

	#rozpoczynanie gry
	game = start_new_game(easy)

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
				if event.key == K_n:
					game = start_new_game(easy)

			if event.type == MOUSEBUTTONDOWN: #handler poruszania myszka
				if event.button == 1:
					print(event.pos)
					# sprawdzamy czy gracz kliknal logo
					if logo_pos.collidepoint(event.pos):
						game = start_new_game(easy)

					game.left_click(event.pos)
				if event.button == 3:
					print(event.pos)
					game.right_click(event.pos)
			if event.type == UPDATECLOCKEVENT:
					game.update_clock()

			screen.blit(background, (0,0))
			pygame.display.flip()

if __name__ == '__main__':
	main()