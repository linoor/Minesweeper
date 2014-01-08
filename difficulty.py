class Difficulty:
	def __init__(self, width, height, mines_number, field_size, name):
		self.name = name
		self.mines_number = mines_number
		self.height = height*field_size+(height+1)
		self.width = width*field_size+(width+1)