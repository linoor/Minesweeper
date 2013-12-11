import pygame
import colors

class Block(pygame.sprite.Sprite):
	def __init__(self, size=10, posx, posy):
		pygame.sprite.Sprite.__init__(self)
		self.size = size
		self.covered = False
		self.mined = False
		self.flagged = False
		self.question = False
		self.posx = posx
		self.posy = posy
		self.set_init_image()
	def set_init_image(self):
		self.image = pygame.Surface(size, size)
		self.image.fill(colors.coveredColor)