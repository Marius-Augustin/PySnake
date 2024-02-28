import pygame
import random
from Menu import Menu

SCREEN_WIDTH  = 1200
SCREEN_HEIGHT = 800
BLOCK_SIZE    = 50

DELAY = 200

# Flags used for directions.

LEFT  = 0
UP    = 1
RIGHT = 2
DOWN  = 3

def load_game():
	global head
	global body
	global fruit
	global background

	pygame.init()
	pygame.display.set_caption('PySnake')
	
	pygame.mixer.init()
	pygame.mixer.music.load('Assets/Music.mp3')
	pygame.mixer.music.play(-1)

	head = []
	head.append(pygame.image.load("Assets/Head_Left.png"))
	head.append(pygame.image.load("Assets/Head_Up.png"))
	head.append(pygame.image.load("Assets/Head_Right.png"))
	head.append(pygame.image.load("Assets/Head_Down.png"))
	
	body = pygame.image.load("Assets/Body.png")
	fruit = pygame.image.load("Assets/Fruit.png")
	background = pygame.image.load("Assets/Background.png")

	return pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def resetVariables():
	global body_length
	global body_positions
	global fruit_position
	global direction
	
	body_length = 2
	direction = RIGHT

	body_positions = [[300, 400], [250, 400]]
	fruit_position = (600, 400)

def get_random_position():
	is_valid = 0	
	while is_valid == False:	
		is_valid = True
		x_axis = random.randrange(1, int(SCREEN_WIDTH  / BLOCK_SIZE - 1), 1) * BLOCK_SIZE
		y_axis = random.randrange(1, int(SCREEN_HEIGHT / BLOCK_SIZE - 1), 1) * BLOCK_SIZE
		for position in body_positions:
			if (x_axis, y_axis) == position:
				is_valid = False	
	
	return (x_axis, y_axis)
	
def read_player_input():
	global direction

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a and direction != RIGHT:
				direction = LEFT
			if event.key == pygame.K_w and direction != DOWN:
				direction = UP
			if event.key == pygame.K_d and direction != LEFT:
				direction = RIGHT
			if event.key == pygame.K_s and direction != UP:
				direction = DOWN

def update_positions():
	global direction
	global body_positions

	(x_axis, y_axis) = body_positions[0]
	if direction == RIGHT:
		x_axis += BLOCK_SIZE
	if direction == LEFT:
		x_axis -= BLOCK_SIZE
	if direction == UP:
		y_axis -= BLOCK_SIZE
	if direction == DOWN:
		y_axis += BLOCK_SIZE
	
	body_positions.insert(0, (x_axis, y_axis))
	body_positions.pop()

def display_game():
	screen.blit(background, (0, 0))
	screen.blit(head[direction], body_positions[0])

	for i in range(1, body_length):
		screen.blit(body, body_positions[i])
	screen.blit(fruit, fruit_position)

	pygame.display.update()
	pygame.time.wait(DELAY)

def verify_collisions():
	global body_length
	global body_positions
	global fruit_position
	
	(x_axis, y_axis) = body_positions[0]

	# Verify if the Snake's head intersects the walls.

	if (x_axis < BLOCK_SIZE) or (x_axis > SCREEN_WIDTH - 2 * BLOCK_SIZE):
		return False
	if (y_axis < BLOCK_SIZE) or (y_axis > SCREEN_HEIGHT - 2 * BLOCK_SIZE):
		return False

	# Verify if the Snake's head intersects its body.

	for i in range(1, body_length):
		if (x_axis, y_axis) == body_positions[i]:
			return False

	# Verify if the Snake's head intersects a fruit.

	if ((x_axis, y_axis) == fruit_position):
		body_positions.append(body_positions[body_length - 1])
		fruit_position = get_random_position()
		body_length += 1
	
	return True

screen = load_game()
menu = Menu(screen)

while (True):
	menu.load()
	resetVariables()
	while (verify_collisions()):
		read_player_input()
		update_positions()
		display_game()