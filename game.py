class Game:
	def __init__(self, minefield):
		self.minefield = minefield
	def click(self, pos):
		for b in self.minefield.blocks.sprites():
			if b.rect.collidepoint(pos):
				b.uncover()	
				print(b.rect)
				print(pos)
		self.minefield.update()
	def is_game_over(self):
		raise NotImplementedError()
	def new_game(self):
		self.minefield.draw()
		pass
	def check_win(self):
		raise NotImplementedError()