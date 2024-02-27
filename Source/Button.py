import pygame

class Button:
	def __init__(self, x_axis, y_axis, width, height):
		self.x_axis = x_axis
		self.y_axis = y_axis
		self.width = width
		self.height = height

	def set_display(self, screen, standard, highlight):
		self.screen = screen
		self.standard  = pygame.image.load(standard)
		self.highlight = pygame.image.load(highlight)

	# Method that verify if the mouse cursor is 
	# hovering over the object defined positions.

	def is_hovering(self):
		(x_axis, y_axis) = pygame.mouse.get_pos()
		if (self.x_axis <= x_axis <= self.x_axis + self.width and
			self.y_axis <= y_axis <= self.y_axis + self.height):
			return True
		return False

	def display(self):
		display = self.standard
		if (self.is_hovering()):
			display = self.highlight

		self.screen.blit(display, (self.x_axis, self.y_axis))
		pygame.display.update()