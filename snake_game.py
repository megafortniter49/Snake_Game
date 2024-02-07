import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Game window dimensions
width = 640
height = 480
display = pygame.display.set_mode((width, height))

# Colors
black = (0, 0, 0)  # Background color
white = (255, 255, 255)  # Snake color
red = (213, 50, 80)  # Food color
green = (0, 255, 0)  # Snake color

# Frames per second controller
fps = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.size = 1  # Initial size of the snake
        self.positions = [[width / 2, height / 2]]  # Starting position of the snake
        self.direction = "UP"  # Initial direction of the snake
        self.change_to = self.direction  # Changes to direction based on user input

    def change_dir_to(self, dir):
        # Change direction of the snake if it's not directly opposite to current direction
        if dir == "RIGHT" and not self.direction == "LEFT":
            self.direction = "RIGHT"
        if dir == "LEFT" and not self.direction == "RIGHT":
            self.direction = "LEFT"
        if dir == "UP" and not self.direction == "DOWN":
            self.direction = "UP"
        if dir == "DOWN" and not self.direction == "UP":
            self.direction = "DOWN"

    def move(self, food_pos):
        # Move the snake in the specified direction and check for food collision
        if self.direction == "RIGHT":
            self.positions.insert(0, [self.positions[0][0] + 10, self.positions[0][1]])
        elif self.direction == "LEFT":
            self.positions.insert(0, [self.positions[0][0] - 10, self.positions[0][1]])
        elif self.direction == "UP":
            self.positions.insert(0, [self.positions[0][0], self.positions[0][1] - 10])
        elif self.direction == "DOWN":
            self.positions.insert(0, [self.positions[0][0], self.positions[0][1] + 10])

        # Check for collision with tail or walls
        if self.positions[0] in self.positions[1:]:
            gameOver()
        if self.positions[0][0] >= width or self.positions[0][0] < 0 or self.positions[0][1] >= height or self.positions[0][1] < 0:
            gameOver()

        # Eating food
        if self.positions[0] == food_pos:
            return 1
        else:
            self.positions.pop()
            return 0

    def draw(self, surface):
        # Draw the snake on the display
        for pos in self.positions:
            pygame.draw.rect(surface, green, pygame.Rect(pos[0], pos[1], 10, 10))

def spawn_food():
    # Return a random position for spawning food
    return [random.randint(0, (width - 10) // 10) * 10, random.randint(0, (height - 10) // 10) * 10]

def gameOver():
    # Quit the game and close the window
    pygame.quit()
    sys.exit()

def gameLoop():
    # Main game loop
    snake = Snake()
    food_pos = spawn_food()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver()
            elif event.type == pygame.KEYDOWN:
                # Change direction based on key press
                if event.key == pygame.K_UP:
                    snake.change_dir_to("UP")
                if event.key == pygame.K_DOWN:
                    snake.change_dir_to("DOWN")
                if event.key == pygame.K_LEFT:
                    snake.change_dir_to("LEFT")
                if event.key == pygame.K_RIGHT:
                    snake.change_dir_to("RIGHT")

        food_eaten = snake.move(food_pos)
        if food_eaten:
            food_pos = spawn_food()
            snake.size += 1

        display.fill(black)
        snake.draw(display)
        pygame.draw.rect(display, red, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
        pygame.display.update()
        fps.tick(10)

gameLoop()
