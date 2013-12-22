from Block import Block
import pygame
import globals
from clock import *

#DEBUG MODE
DEBUG = False

class Game:
	def __init__(self, minefield):
		self.clock = 0
		self.minefield = minefield
		self.clickable = True
		self.clock = self.init_clock()
		self.clock.show_clock()
		self.first_click = True

	def init_clock(self):
		rect = globals.screen.get_rect()
		pos = rect.left + 70, rect.top + 20
		return Clock(pos)

	def find_collide_rect(self, pos):
		for b in self.minefield.get_blocks():
			if b.rect.collidepoint(pos):
				return b
	def left_click(self, pos):
		if self.clickable:
			# jesli pierwsze klikniecie, to rozpoczynamy odliczenie zegara
			if self.first_click:
				self.first_click = False
				self.clock.start_clock()
				
			b = self.find_collide_rect(pos)
			if b:
				if b.covered and not b.flagged and not b.question:
					if b.mines_surrounding == 0:
						self.minefield.ripple_effect(b)
					else:
						b.uncover()
				print(b.rect)
				print(pos)

			if self.is_game_over():
				self.end_game()
			self.minefield.update()
			
	def right_click(self, pos):
		if self.clickable:
			b = self.find_collide_rect(pos)
			if b:
				if b.covered:
					if not b.flagged and not b.question:
						b.flag()
					elif b.flagged:
						Block.question(b)
					elif b.question:
						b.cover()
				print(b.rect)
				print(pos)

			if self.is_game_over():
				self.end_game()
			self.minefield.update()

	def is_game_over(self):
		# jesli trafimy na mine
		if any(not b.covered and b.mined for b in self.minefield.get_blocks()):
			return True
		# jesli oflagujemy wszystkie miny
		# wszystkie pola ktore sa zaminowane musza byc oflagowane
		if all(b.flagged for b in self.minefield.get_blocks() if b.mined):
			return True
		# jesli odkryjemy wszystkie niezaminowane pola
		if all(not b.covered for b in self.minefield.get_blocks() if not b.mined):
			return True

		return False
	def end_game(self):
		font = pygame.font.Font(None, 36)
		# wygrana
		if self.check_win():
			text = font.render("You win!", 1, (0, 255, 34))
		# przegrana
		else:
			text = font.render("You lose!", 1, (255, 0, 0))
		# odkrywanie wszystkich min
		self.minefield.uncover_mines()
		# umiejscowienie napisu
		textpos = text.get_rect()
		textpos.centerx = globals.background.get_rect().centerx
		textpos.centery = self.minefield.game_area.get_rect().top+40
		globals.background.blit(text, textpos)
		# wylaczenie mozliwosci odkrywania pol
		self.clickable = False
	def new_game(self):
		self.minefield.draw()
		self.minefield.set_mines()
		if DEBUG:
			self.minefield.debug()
	def check_win(self):
		# jesli trafimy na mine - przegrana
		if any(b.mined and not b.covered for b in self.minefield.get_blocks()):
			return False
		return True
	def update_clock(self):
		globals.refresh_background()
		self.minefield.update()
		self.clock.update()