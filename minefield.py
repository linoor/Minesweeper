import pygame
from colors import *
from Block import *

class Minefield:


	def __init__(self, screen, background, difficulty):
		self.background = background
		self.screen = screen
		self.difficulty = difficulty
		self.blocks = []
		self.game_area = None

	def draw(self):
		# 540, 350
		self.init_game_area()	

		self.init_blocks()

		for b in self.blocks:
			self.game_area.blit(b.image, (b.posx, b.posy))
		self.background.blit(self.game_area, (self.game_area_pos))

	def init_blocks(self):
		size = 25
		padding = 1
		posx = padding
		posy = padding
		while posy < self.difficulty.height:
			block = Block(posx, posy, size)	
			block.init_image()
			posx += size + padding
			if posx > self.difficulty.width:
				posx = padding
				posy += size + padding
			self.blocks.append(block)

	def init_game_area(self):
		size = self.difficulty.width, self.difficulty.height
		self.game_area = pygame.Surface((size[0]*0.9, size[1]*0.7))
		self.game_area =self.game_area.convert()
		self.game_area.fill(blueColor)
		self.game_area_pos = self.game_area.get_rect()
		self.game_area_pos.centerx = self.background.get_rect().centerx
		self.game_area_pos.centery = self.background.get_rect().centery