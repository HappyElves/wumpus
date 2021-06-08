import pygame
from pygame.locals import *

firstRoom = ('assets/levels/startingRoom.txt')
testRoom = ('assets/levels/testRoom.txt')

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, imagePath):
        super().__init__()
        self.image = pygame.image.load(imagePath).convert()
        #self.rect = self.image.get_rect(center = (0,0))
    def __call__(self, center=(0,0)):
        self.rect = self.image.get_rect(center = center)
        return self
        
#spriteDictionary = { '#' : Obstacle('assets/greySquare.jpg') } 

def loadRoom(roomPath):
    spriteDictionary = { '#' : 'assets/greySquare.jpg' } 
    roomSprites = pygame.sprite.Group()
    with open(roomPath, 'r') as roomData:
        for a, line in enumerate(roomData.readlines()):
            for b, char in enumerate(line):
                if char not in [' ', '\n']:
                    roomSprites.add(Obstacle(spriteDictionary[char])((16 + (32 * b), 16 + (32 * a))))
            
    
    return roomSprites
