import pygame
import time
import random

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
v.0.6.0 - Add raining block functionality.
v.0.7.0 - Crashing.
v.0.8.0 - Scoring.
"""

# display configuration
display_width = 800
display_height = 600

# colour configuration
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# car variables
car_image = pygame.image.load('car.png')
car_width = 65

# block variables
block_color = (53,115,255)


pygame.init()
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A Bit Racey')
clock = pygame.time.Clock()

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    game_display.blit(text, (0,0))

# (0, 0) is top-left corner
def car(x, y):
    game_display.blit(car_image, (x, y))

def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()

def message_display(text):
    large_text = pygame.font.Font('freesansbold.ttf', 115)
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.center = ((display_width / 2), (display_height / 4))
    game_display.blit(text_surf, text_rect)
    pygame.display.update()
    time.sleep(2)    # show message for a short 2 sec period
    game_loop()   # restart the game after message

def things(thingx, thingy, thingw, thingh, color):
    # draw box to screen
    pygame.draw.rect(game_display, color, [thingx, thingy, thingw, thingh])

def crash():
    message_display('You Crashed')

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0
    game_exit = False

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600   # start -600 pixels off screen
    thing_speed = 5
    thing_width = 100  # pixels
    thing_height= 100  # pixels
    dodged = 0

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
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        thing_starty += thing_speed
        car(x, y)
        things_dodged(dodged)
        if x > display_width - car_width or x < 0:
            crash()
        if thing_starty > display_height:  # block off the screen
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.1)
        if y < thing_starty + thing_height:
            print('Y crossover')
            if x > thing_startx and x < thing_startx + thing_width \
                    or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                print('X crossover ... CRASH')
                crash()
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
