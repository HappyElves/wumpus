#Imports the pygame library
import pygame
from pygame.locals import *

#Imports multiple other locally stored python files which include classes and
#code used within the program. This is done for the sake of neat code
from library.player import Player
from library.enemy import Enemy
from library.map import *

#pygame.init() initialises all imported pygame units
pygame.init()

height = 480 #height of screen
width = 864 #width of screen
FPS = 60 #FPS limit

#A pygame.time.clock object helps to track time in frames
FramePerSec = pygame.time.Clock()

#A pygame.display object is the display screen the game is viewed on
#set_mode initialises the width and height of the screen
displaySurface = pygame.display.set_mode((width, height))

#Sets the caption of the game window
pygame.display.set_caption("Game Test")

#Creates a Player object (from within the imported file library.player) named player)
player = Player()
enemy = Enemy()

#creates a pygame.surface object named background that more than fills the size of the game window and prints it onto the screen
background = pygame.transform.scale(pygame.image.load('assets/background.jpg').convert(), (width, height))
displaySurface.blit(background, (0, 0))
pygame.display.flip()

#Creates a pygame.sprite.Group object which contains all the sprite objects which need to be updated every frame
allSprites = pygame.sprite.OrderedUpdates()
allSprites.add(player)
allSprites.add(enemy)
allSprites.add(loadRoom(testRoom)) #Adds all the sprites in a given room from the loadRoom frunction

#Main game loop
while True:
    #Exits pygame if the window exit button is clicked, necessary in all pygame programs to avoid an infinite loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #Removes all sprites used in the last group.draw call by filling the positions with the sprite "background"
    allSprites.clear(displaySurface, background)
    allSprites.add(player.bullets)
    allSprites.add(player.hearts)
    allSprites.add(enemy.bullets)
    print(allSprites)

    #Calls all of the update functions of sprites
    allSprites.update(allSprites)

    #calls a craw function on all sprites updsating the screen
    rects = allSprites.draw(displaySurface)
    pygame.display.update(rects)

    #updates the clock by 1 frame ensuring that the number of milliseconds passed since the last call never makes the game exceed 60fps
    FramePerSec.tick(60)
    
