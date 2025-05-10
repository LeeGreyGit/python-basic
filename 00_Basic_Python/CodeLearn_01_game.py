
# Import library
import pygame, sys
from pygame.locals import *

pygame.init()

# Create game windows with width x = 400 and height y = 300
DISPLAYSURF = pygame.display.set_mode((400, 300))
# Display game title
pygame.display.set_caption('Hello world!')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # Game windows color
    DISPLAYSURF.fill((255, 255, 255))
    # Create surface with width 150 + height 50 and color green
    surface2rect = pygame.Surface((150, 50))
    surface2rect.fill((0, 255, 0))
    '''
    Draw box in surface
        pygame.draw.rect(surface, color, rect, width)
    color : color of box
    rect (position x : from left top of surface, position y : from left top of surface, width box, height box)
    width : line thickness of box
    '''
    pygame.draw.rect(surface2rect, (255, 0, 0), (20, 20, 50, 20))
    # Display surface
    DISPLAYSURF.blit(surface2rect, (100, 80))
    pygame.display.update()