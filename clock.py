import globals
import colors
import pygame

class Clock:
	def __init__(self, pos):
		self.time = 0
		self.pos = 	pos	
		self.running = True
	def show_clock(self):
		clock_font = pygame.font.Font(None, 36)
		text = clock_font.render(str(self.time).zfill(2), 1, (10, 10, 10))
		globals.background.blit(text, self.pos)
	def update(self):
		# jesli gra sie zakonczyla, zatrzymaj zegar
		if not self.running:
			return
		self.time += 1
		self.clear_clock()	
		self.show_clock()
	def clear_clock(self):
		tmp = pygame.Surface((3*36+2, 40))
		tmp.fill(colors.orangeColor)
		globals.background.blit(tmp, self.pos)
	def start_clock(self):
		pygame.time.set_timer(globals.UPDATECLOCKEVENT, 1000)
		self.running = True
	def stop_clock(self):
		self.running = False