import globals
import pygame

class Clock:
	def __init__(self, pos):
		self.time = 0
		self.pos = 	pos	
	def show_clock(self):
		clock_font = pygame.font.Font(None, 36)
		text = clock_font.render(str(self.time).zfill(2), 1, (10, 10, 10))
		globals.background.blit(text, self.pos)
	def update(self):
		self.time += 1