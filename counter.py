import globals
import colors
import pygame

class Counter:
	def __init__(self, mines, pos):
		self.mines = mines
		self.pos = pos
		self.show_counter()

	def show_counter(self):
		ikona_bomby = pygame.image.load('ikonki/bomba.png')
		counter_font = pygame.font.Font(globals.counter_and_clock_font, 27)
		text = counter_font.render(str(self.mines).zfill(2), 1, colors.napisyColor)

		# shadow
		counter_shadow = counter_font.render(str(self.mines).zfill(2), 1, colors.shadowColor)
		shadow_pos = pygame.Rect(self.pos)
		shadow_pos.x += 2
		shadow_pos.y += 2

		globals.background.blit(counter_shadow, shadow_pos)
		globals.background.blit(text, self.pos)
		pos2 = pygame.Rect(self.pos)
		pos2.right -= 25
		pos2.y -= 1

		


		globals.background.blit(ikona_bomby, pos2)

	def update(self):
		# jesli gra sie zakonczyla, zatrzymaj zegar
		if self.mines < 0: return
		self.clear_counter()	
		self.show_counter()
	
	def clear_counter(self):
		tmp = pygame.Surface((3*36+2, 30))
		tmp.fill(colors.backgroundColor)
		globals.background.blit(tmp, self.pos)