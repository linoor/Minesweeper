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

	def update(self):
		# jesli gra sie zakonczyla, zatrzymaj zegar
		if self.mines <= 0: return
		self.clear_counter()	
		self.show_counter()
	
	def clear_counter(self):
		tmp = pygame.Surface((3*36+2, 30))
		tmp.fill(colors.orangeColor)
		globals.background.blit(tmp, self.pos)