from Block import Block
import pygame
import globals
class Game:
	def __init__(self, minefield):
		self.minefield = minefield
	def find_collide_rect(self, pos):
		for b in self.minefield.blocks:
			if b.rect.collidepoint(pos):
				return b
	def left_click(self, pos):
		b = self.find_collide_rect(pos)
		if b:
			if b.covered and not b.flagged and not b.question:
				b.uncover()	
			print(b.rect)
			print(pos)

		if self.is_game_over():
			self.end_game()
		self.minefield.update()
	def right_click(self, pos):
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
		for b in self.minefield.blocks:
			if not b.covered and b.mined:
				return True
		# jesli oflagujemy wszystkie miny
		for b in self.minefield.blocks:
			if b.mined and not b.flagged:
				return False
		# jesli odkryjemy wszystkie niezaminowane pola
		for b in self.minefield.blocks:
			if b.covered and not b.mined:
				return False
		return True
	def end_game(self):
		font = pygame.font.Font(None, 36)
		if self.check_win():
			text = font.render("You win!", 1, (0, 255, 34))
		else:
			text = font.render("You lose!", 1, (255, 0, 0))
			self.minefield.uncover_mines()
		textpos = text.get_rect()
		textpos.centerx = globals.background.get_rect().centerx
		textpos.centery = self.minefield.game_area.get_rect().top+40
		globals.background.blit(text, textpos)
	def new_game(self):
		self.minefield.draw()
		self.minefield.set_mines()
	def check_win(self):
		if self.minefield.mines_left == 0:
			return True
		else:
			return False