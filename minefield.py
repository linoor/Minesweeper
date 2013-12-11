import pygame
from colors import *
from Block import *

class Minefield:


	def __init__(self, screen, background, difficulty):
		self.background = background
		self.screen = screen
		self.difficulty = difficulty
		self.blocks = pygame.sprite.Group()
		self.game_area = None

	def draw(self):
		# 540, 350
		self.init_game_area()	
		self.init_blocks()
		self.update()

	def update(self):
		for b in self.blocks.sprites():
			self.game_area.blit(b.image, (b.posx, b.posy))
		self.background.blit(self.game_area, (self.game_area_pos))

	def init_blocks(self):
		size = 25
		padding = 1
		posx = padding
		posy = padding
		while posy+size < self.difficulty.height:
			block = Block(posx, posy, size)	
			offset = self.game_area_pos.topleft
			block.rect.topleft = (posx+offset[0], posy+offset[1])
			posx += size + padding
			if posx+size> self.difficulty.width:
				posx = padding
				posy += size + padding
			self.blocks.add(block)

	def init_game_area(self):
		size = self.difficulty.width, self.difficulty.height
		self.game_area = pygame.Surface(size)
		self.game_area =self.game_area.convert()
		self.game_area.fill(blueColor)
		self.game_area_pos = self.game_area.get_rect()
		self.game_area_pos.centerx = self.background.get_rect().centerx
		self.game_area_pos.centery = self.background.get_rect().centery