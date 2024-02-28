import pygame
from Button import Button 

class Menu:
	def __init__(self, screen):
		self.screen = screen
		self.set_assets()

	def set_assets(self):
		BUTTON_WIDTH  = 200
		BUTTON_HEIGHT = 100

		self.play = Button(500, 500, BUTTON_WIDTH, BUTTON_HEIGHT)
		self.exit = Button(500, 625, BUTTON_WIDTH, BUTTON_HEIGHT)

		self.play.set_display(self.screen, "Assets/Play_Dark.png", "Assets/Play_Light.png")
		self.exit.set_display(self.screen, "Assets/Exit_Dark.png", "Assets/Exit_Light.png")
		self.cover = pygame.image.load("Assets/Cover.png")

	def load(self):
		COVER_AXIS  = (350, 10)
		LIGHT_COLOR = (243, 233, 211)

		self.screen.fill(LIGHT_COLOR)
		self.screen.blit(self.cover, COVER_AXIS)

		while(True):
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					quit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if (self.exit.is_hovering() == True):
						quit()
					if (self.play.is_hovering() == True):
						return

				self.play.display()
				self.exit.display()
				pygame.display.update()