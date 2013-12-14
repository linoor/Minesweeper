import pygame
import colors
from Block import *
import random
import globals
import itertools

#DEBUG MODE
DEBUG = True

class Minefield:

	def __init__(self, difficulty):
		self.mines_left = difficulty.mines_number
		self.difficulty = difficulty
		self.blocks = []
		self.game_area = None

	def get_blocks(self):
		return list(itertools.chain.from_iterable(self.blocks))

	def set_mines(self):
		random.seed()
		indices = [random.randint(0, len(self.get_blocks())-1) for i in range(self.difficulty.mines_number)]
		for i in indices:
			self.get_blocks()[i].mine()
		self.set_mines_surrounding()

	def draw(self):
		# 540, 350
		self.init_game_area()	
		self.init_blocks()
		self.update()

	def update(self):
		for b in self.get_blocks():
			self.game_area.blit(b.image, (b.posx, b.posy))
		globals.background.blit(self.game_area, (self.game_area_pos))

	def init_blocks(self):
		size = 25
		padding = 1
		posx, posy = padding, padding
		tmp_block = []
		while posy+size < self.difficulty.height:
			block = self.create_block(posx, posy, size)
			tmp_block.append(block)
			posx += size + padding
			# nowy rzad
			if posx+size > self.difficulty.width:
				posx = padding
				posy += size + padding
				self.blocks.append(tmp_block)
				tmp_block = []

	def set_mines_surrounding(self):
		for i in range(len(self.blocks)):
			for j in range(len(self.blocks[i])):
				if self.blocks[i][j].mined:
					self.set_mines_around(i,j)

	def set_mines_around(self, i, j):
		for n in range(i-1, i+2):
			for m in range(j-1, j+2):
				if n != m:
					if self.blocks[n][m]:
						self.blocks[n][m].mines_surrounding += 1

	def create_block(self, posx, posy, size):
		block = Block(posx, posy, size)
		offset = self.game_area_pos.topleft
		block.rect.topleft = (posx+offset[0], posy+offset[1])
		return block

	def init_game_area(self):
		size = self.difficulty.width, self.difficulty.height
		self.game_area = pygame.Surface(size)
		self.game_area =self.game_area.convert()
		self.game_area.fill(colors.game_area_color)
		self.game_area_pos = self.game_area.get_rect()
		self.game_area_pos.centerx = globals.background.get_rect().centerx
		self.game_area_pos.centery = globals.background.get_rect().centery+20

	def debug(self):
		for b in self.get_blocks():
			if b.mined:
				b.image.fill(colors.bombhint)

	def uncover_mines(self):
		for b in self.get_blocks():
			if b.mined:
				b.uncover()