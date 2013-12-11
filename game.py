from Block import Block
class Game:
	def __init__(self, minefield):
		self.minefield = minefield
	def left_click(self, pos):
		for b in self.minefield.blocks:
			if b.rect.collidepoint(pos):
				if b.covered and not b.flagged and not b.question:
					b.uncover()	
				print(b.rect)
				print(pos)
		self.minefield.update()
	def right_click(self, pos):
		for b in self.minefield.blocks:
			if b.rect.collidepoint(pos):
				if b.covered:
					if not b.flagged and not b.question:
						b.flag()
					elif b.flagged:
						Block.question(b)
					elif b.question:
						b.cover()
				print(b.rect)
				print(pos)
		self.minefield.update()
	def is_game_over(self):
		raise NotImplementedError()
	def new_game(self):
		self.minefield.draw()
		self.minefield.set_mines()
	def check_win(self):
		raise NotImplementedError()