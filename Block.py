import pygame
import colors
from globals import *

class Block(pygame.sprite.Sprite):
	def __init__(self, posx, posy, size, i, j):
		pygame.sprite.Sprite.__init__(self)
		self.size = size
		self.covered = True
		self.mined = False
		self.flagged = False
		self.question = False
		self.mines_surrounding = 0
		self.posx = posx
		self.posy = posy
		self.indexes = i, j
		self.init_image()
		self.rect = self.image.get_rect()
	def init_image(self):
		self.image = pygame.Surface((self.size, self.size))
		self.image = self.image.convert()
		self.image.fill(colors.coveredColor)
	def uncover(self):
		if self.mined:
			self.image.fill(colors.bombColor)	
		else:
			self.image.fill(colors.uncoveredColor)
			# ustawianie napisu na polach
			font = pygame.font.Font(None, 36)
			text = font.render(str(self.mines_surrounding), 1, (10, 10, 10))
			textpos = text.get_rect()
			textpos.centerx = self.image.get_rect().centerx
			textpos.centery = self.image.get_rect().centery
			self.image.blit(text, textpos)
		self.covered = False
		# print("coordinates: ", self.posx, self.posy)
	def flag(self):
		self.image.fill(colors.redColor)
		self.flagged = True
	def question(self):
		self.flagged = False
		self.question = True
		self.image.fill(colors.questionColor)
	def cover(self):
		self.flagged = False
		self.question = False
		self.image.fill(colors.coveredColor)
	def mine(self):
		self.mined = True