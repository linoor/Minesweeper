class Game:
	def __init__(self, minefield):
		self.minefield = minefield
	def is_game_over(self):
		raise NotImplementedError()
	def new_game(self):
		self.minefield.draw()
	def check_win(self):
		raise NotImplementedError()