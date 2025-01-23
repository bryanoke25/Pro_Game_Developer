import pygame
pygame.init()
screen = pygame.display.set_mode([500, 500])
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW =(255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
screen.fill(WHITE)

class mycircle():
    def __init__(self, color, pos, rad, width = 0):
        self.color = color
        self.pos = pos
        self.width = width
        self.rad = rad
        self.scrn = screen

    def draw(self):
        pygame.draw.circle(self.scrn, self.color, self.pos, self.rad, self.width )
        
    def grow(self, x):
        self.rad += x
        pygame.draw.circle(self.scrn, self.color, self.pos, self.rad, self.width )

#how to draw a circle
position = (300, 300)
radius = 50
width = 2
pygame.draw.circle(screen, RED, position, radius, width)
pygame.display.update()
        
    
blueCircle = mycircle(BLUE, position, radius+60)
redCircle = mycircle(RED, position, radius+40)
yellowCircle = mycircle(YELLOW, position, radius, 5)
greenCircle = mycircle(GREEN, position, 20)

while(1):
    for event in pygame.event.get():
        if (event.type == pygame.MOUSEBUTTONDOWN):
            blueCircle.draw()
            redCircle.draw()
            yellowCircle.draw()
            greenCircle.draw()
            pygame.display.update()
        elif (event.type == pygame.MOUSEBUTTONUP):
            blueCircle.grow(2)
            redCircle.grow(2)
            yellowCircle.grow(2)
            greenCircle.grow(2)
            pygame.display.update()
        elif (event.type == pygame.MOUSEMOTION):
            pos = pygame.mouse.get_pos()
            blackCircle = mycircle(BLACK, pos, 5)
            blackCircle.draw()
            pygame.display.update()

