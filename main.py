import pygame, sys
from pygame.locals import *

# kolory 
whiteColor = pygame.Color(250, 250, 250)
blueColor = pygame.Color(0, 107, 255)
orangeColor = pygame.Color(255, 201, 0)

def main():
	pygame.init()
	pygame.display.set_caption('Saper')

	# ustawianie wielkosci okna
	screen = pygame.display.set_mode((640, 480))

	# ustawienia tla
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
	size = screen.get_size()
	game_area = pygame.Surface((size[0]*0.9, size[1]*0.7))
	game_area = game_area.convert()
	game_area.fill(blueColor)
	game_area_pos = game_area.get_rect()
	game_area_pos.centerx = background.get_rect().centerx
	game_area_pos.centery = background.get_rect().centery
	background.blit(game_area, (game_area_pos))

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