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
	game.clock.show_clock()
	return game

def main():
	pygame.font.init()
	pygame.init()
	pygame.display.set_caption('Saper')
	
	# Menu
	font = pygame.font.Font(None, 36)
	text = font.render("Saper!", 1, (10, 10, 10))
	textpos = text.get_rect()
	textpos.centerx = background.get_rect().centerx
	background.blit(text, textpos)

	#napis nowej gry
	font = pygame.font.Font(None, 20)
	text = font.render("press 'n' to start new game", 1, (0, 0, 0))
	textpos = text.get_rect()
	textpos.topright = background.get_rect().topright
	background.blit(text, textpos)

	#ustawianie planszy
	normal = Difficulty(20*25+26, 16*25+17, 100, "normal")
	easy = Difficulty(20*25+21, 16*25+17, 40, "easy")
	start_new_game(normal)

	screen.blit(background, (0,0))
	pygame.display.flip()

	#rozpoczynanie gry
	game = start_new_game(normal)

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
					game = start_new_game(normal)
					game.clock.clear_clock()
					game.clock.stop_clock()
					game.clock.show_clock()

			if event.type == MOUSEBUTTONDOWN: #handler poruszania myszka
				if event.button == 1:
					print(event.pos)
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