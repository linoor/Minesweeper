import globals
import colors
import pygame

class Counter:
	def __init__(self, mines, pos):
		self.mines = mines
		self.pos = pos
		self.show_counter()

	def show_counter(self):
		counter_font = pygame.font.Font(None, 36)
		text = counter_font.render(str(self.mines).zfill(2), 1, (10, 10, 10))
		globals.background.blit(text, self.pos)