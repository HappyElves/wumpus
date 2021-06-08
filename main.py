import pygame
from pygame.locals import *
from library.player import Player
from library.map import *
#from library.map import Obstacle
 
pygame.init()

RES = (854, 480)
height = 480 #height of screen
width = 864 #width of screen
FPS = 60 #FPS limit

#Sets up the game clock and window
FramePerSec = pygame.time.Clock()

displaySurface = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game Test")

player = Player()
background = pygame.transform.scale(pygame.image.load('assets/gsquare.png').convert(), (1000, 1000))
displaySurface.blit(background, (0, 0))
pygame.display.flip()

allSprites = pygame.sprite.OrderedUpdates()
allSprites.add(player)
allSprites.add(loadRoom(testRoom))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    allSprites.clear(displaySurface, background)

    #pygame.display.flip()

    allSprites.update(allSprites)
    
    rects = allSprites.draw(displaySurface)
    pygame.display.update(rects)
    
    FramePerSec.tick(60)
    
