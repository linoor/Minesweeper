import pygame
import colors

class Block(pygame.sprite.Sprite):
	def __init__(self, posx, posy, size=10):
		pygame.sprite.Sprite.__init__(self)
		self.size = size
		self.covered = False
		self.mined = False
		self.flagged = False
		self.question = False
		self.posx = posx
		self.posy = posy
		self.init_image()
	def init_image(self):
		self.image = pygame.Surface((self.size, self.size))
		self.image = self.image.convert()
		self.image.fill(colors.coveredColor)