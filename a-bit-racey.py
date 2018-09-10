import pygame
"""
A Bit Racey Game
- This code follows the tutorial from sentdex:
https://www.youtube.com/watch?v=ujOTNg17LjI&list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO&index=1

version history
===============
v.0.1.0 - Initial game skeleton that displays the events that appear in event loop of the game
v.0.2.0 - Adding a car to the display.
"""

# display configuration
display_width = 800
display_height = 600

# colour configuration
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

car_image = pygame.image.load('assets/car.jpg')

# (0, 0) is top-left corner
def car(x, y):
    game_display.blit(car_image, (x, y))

pygame.init()
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A Bit Racey')
clock = pygame.time.Clock()
x = display_width * 0.45
y = display_height * 0.5

crashed = False
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        # print(event)
    game_display.fill(white)
    car(x, y)
    pygame.display.update()  # updates the entire game surface unless specific arguments provided
    clock.tick(60)  # frames per second

pygame.quit()
quit()