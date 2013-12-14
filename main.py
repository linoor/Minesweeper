import pygame, sys
from pygame.locals import *

from minefield import *
from colors import *
from game import *
from difficulty import *
from globals import *

def main():
	pygame.init()
	pygame.display.set_caption('Saper')
	
	# Menu
	font = pygame.font.Font(None, 36)
	text = font.render("Saper!", 1, (10, 10, 10))
	textpos = text.get_rect()
	textpos.centerx = background.get_rect().centerx
	background.blit(text, textpos)

	#ustawianie planszy
	normal = Difficulty(20*25+26, 16*25+17, 100, "normal")
	easy = Difficulty(20*25+21, 16*25+17, 40, "easy")
	game = Game(Minefield(easy))
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
			if event.type == MOUSEBUTTONDOWN: #handler poruszania myszka
				if event.button == 1:
					print(event.pos)
					game.left_click(event.pos)
				if event.button == 3:
					print(event.pos)
					game.right_click(event.pos)

			screen.blit(background, (0,0))
			pygame.display.flip()

if __name__ == '__main__':
	main()