import pygame
from colors import *

class Minefield:
	def __init__(self, screen, background, height, width):
		self.background = background
		self.screen = screen
		self.height = height
		self.width = width
		self.draw()
		self.blocks = []
	def draw(self):
		size = self.height, self.width
		# 540, 350
		game_area = pygame.Surface((size[0]*0.9, size[1]*0.7))
		game_area = game_area.convert()
		game_area.fill(blueColor)
		game_area_pos = game_area.get_rect()
		game_area_pos.centerx = self.background.get_rect().centerx
		game_area_pos.centery = self.background.get_rect().centery
		self.background.blit(game_area, (game_area_pos))
	def init_blocks(self):
		pass