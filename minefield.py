import pygame
import colors
from Block import *
import random
import globals
import itertools
import time

#DEBUG MODE
DEBUG = True
calls = 0

class Minefield:

	def __init__(self, difficulty):
		self.mines_left = difficulty.mines_number
		self.difficulty = difficulty
		self.blocks = []
		self.game_area = None
		self.are_mines_set = False

	def get_blocks(self):
		return list(itertools.chain.from_iterable(self.blocks))

	def set_mines(self, block):
		random.seed()
		for _ in range(self.difficulty.mines_number):
			blocks = self.get_blocks()
			selected_block = blocks[random.randint(0, len(blocks)-1)]
			if block != selected_block:
				selected_block.mine()

		self.set_mines_surrounding()
		self.are_mines_set = True

	def set_mines_surrounding(self):
		for i in range(len(self.blocks)):
			for j in range(len(self.blocks[i])):
				if self.blocks[i][j].mined:
					self.set_mines_around(i,j)

	def set_mines_around(self, i, j):
		for n in range(i-1, i+2):
			for m in range(j-1, j+2):
				if n < 16 and m < 20 and n >= 0 and m >= 0 and self.blocks[n][m]:
					self.blocks[n][m].mines_surrounding += 1

	def ripple_effect(self, block):
		if not block.covered: return
		if block.mined or block.flagged: return
		block.uncover()
		if block.mines_surrounding != 0: return

		row_clicked, column_clicked = self.find(block)
		blocks = self.blocks
		for i in range(3):
			for j in range(3):
				current_row = row_clicked + i - 1
				current_column = column_clicked + j - 1
				try:
					if blocks[current_row][current_column].covered:
						self.ripple_effect(blocks[current_row][current_column])
				except IndexError as e:
					pass
		return

	def find(self, elem):
	    for row, i in enumerate(self.blocks):
	        try:
	            column = i.index(elem)
	        except ValueError:
	            continue
	        return row, column
	    return -1

	def draw(self):
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
		i, j = 0, 0
		while posy+size < self.difficulty.height:
			j += 1
			block = self.create_block(posx, posy, size, i, j)
			tmp_block.append(block)
			posx += size + padding
			# nowy rzad
			if posx+size > self.difficulty.width:
				i += 1
				j = 0
				posx = padding
				posy += size + padding
				self.blocks.append(tmp_block)
				tmp_block = []

	def create_block(self, posx, posy, size, i, j):
		block = Block(posx, posy, size, i, j)
		offset = self.game_area_pos.topleft
		block.rect.topleft = (posx+offset[0], posy+offset[1])
		return block

	def init_game_area(self):
		size = self.difficulty.width, self.difficulty.height
		self.game_area = pygame.Surface(size)
		self.game_area = self.game_area.convert()
		self.game_area.fill(colors.game_area_color)
		self.game_area_pos = self.game_area.get_rect()
		self.game_area_pos.centerx = globals.background.get_rect().centerx
		self.game_area_pos.centery = globals.background.get_rect().centery + 20

	def debug(self):
		for b in self.get_blocks():
			if b.mined:
				b.image.fill(colors.bombhint)

	def uncover_mines(self, clicked_block):
		for b in self.get_blocks():
			if b.mined and b != clicked_block:
				b.uncover()
			if b.mined and b == clicked_block:
				b.uncover(exploded=True)