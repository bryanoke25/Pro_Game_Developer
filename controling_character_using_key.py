import pygame
from time import *
from pygame.locals import *

pygame.init()
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

player_x = 200
player_y = 200
keys = [False, False, False, False]

player = pygame.image.load("C:/Users/bryan/OneDrive/Desktop/JetLearn/Pro_Game_Developer/images/character.png")
background = pygame.image.load("C:/Users/bryan/OneDrive/Desktop/JetLearn/Pro_Game_Developer/images/background.png")

while player_y < 600:
    screen.blit(background, (0, 0))
    screen.blit(player, (player_x, player_y))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        #check if any keyboard button is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                keys[0] = True
            elif event.key == K_LEFT:
                keys[1] = True
            elif event.key == K_DOWN:
                keys[2] = True
            elif event.key == K_RIGHT:
                keys[3] == True

        #check if any keyboard button is released
        if event.type == pygame.KEYUP:
            if event.key == K_UP:
                keys[0] = False
            elif event.key == K_LEFT:
                keys[1] = False
            elif event.key == K_DOWN:
                keys[2] = False
            elif event.key == K_RIGHT:
                keys[3] == False

    if keys[0]:
        if player_y > 0:
            player_y -= 4

    elif keys[2]:
        if player_y < 536:
            player_y += 4

    if keys[1]:
        if player_x > 0:
            player_x  -= 2

    elif keys[3]:
        if player_x < 536:
            player_x += 2

    player_y += 3
    sleep(0.05)

print("GAME OVER")



