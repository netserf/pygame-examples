import pygame
"""
A Bit Racey Game
- This code follows the tutorial from sentdex:
https://www.youtube.com/watch?v=ujOTNg17LjI&list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO&index=1

version history
===============
v.0.1.0 - Initial game skeleton that displays the events that appear in event loop of the game
"""

pygame.init()
game_display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('A Bit Racey')
clock = pygame.time.Clock()

crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        print(event)
    pygame.display.update()  # updates the entire game surface unless specific arguments provided
    clock.tick(60)  # frames per second

pygame.quit()
quit()