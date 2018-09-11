import pygame
import time
"""
A Bit Racey Game
- This code follows the tutorial from sentdex:
https://www.youtube.com/watch?v=ujOTNg17LjI&list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO&index=1

version history
===============
v.0.1.0 - Initial game skeleton that displays the events that appear in event loop of the game
v.0.2.0 - Adding a car to the display.
v.0.3.0 - Allow car to move left or right on the screen.
v.0.4.0 - Allow car to crash at boundaries.
v.0.5.0 - Allow the user to restart the game after a crash.
"""

# display configuration
display_width = 800
display_height = 600

# colour configuration
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# car variables
car_image = pygame.image.load('assets/car.jpg')
car_width = 210

pygame.init()
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A Bit Racey')
clock = pygame.time.Clock()

# (0, 0) is top-left corner
def car(x, y):
    game_display.blit(car_image, (x, y))

def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()

def message_display(text):
    large_text = pygame.font.Font('freesansbold.ttf', 115)
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.center = ((display_width / 2), (display_height / 2))
    game_display.blit(text_surf, text_rect)
    pygame.display.update()
    time.sleep(2)    # show message for a short 2 sec period
    game_loop()   # restart the game after message

def crash():
    message_display('You Crashed')

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.6)

    x_change = 0
    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -20
                if event.key == pygame.K_RIGHT:
                    x_change = 20
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        x += x_change
        game_display.fill(white)
        car(x, y)
        if x > display_width - car_width or x < 0:
            crash()
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()