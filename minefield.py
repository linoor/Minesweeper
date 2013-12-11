import pygame
from colors import *
from Block import *

class Minefield:


	def __init__(self, screen, background, height, width):
		self.background = background
		self.screen = screen
		self.height = height
		self.width = width
		self.block = None
		self.game_area = None

	def draw(self):
		size = self.height, self.width
		# 540, 350
		self.game_area = pygame.Surface((size[0]*0.9, size[1]*0.7))
		self.game_area =self.game_area.convert()
		self.game_area.fill(blueColor)
		game_area_pos =self.game_area.get_rect()
		game_area_pos.centerx = self.background.get_rect().centerx
		game_area_pos.centery = self.background.get_rect().centery

		self.init_blocks()


		self.game_area.blit(self.block.image, (0,0))
		self.background.blit(self.game_area, (game_area_pos))

	def init_blocks(self):
		self.block = Block(0,0)
		self.block.init_image()