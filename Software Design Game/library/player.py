import pygame
from pygame.locals import *
from library.map import Obstacle
pygame.init()
vec = pygame.math.Vector2  # 2 for two dimensional

height = 450 #height of screen
width = 400
pSpeed = 5 #player speed

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 

        self.image = pygame.transform.scale(pygame.image.load('assets/bsquare.jpg').convert(), (100, 100))
        self.rect = self.image.get_rect(center = (width/2, height/2))
        
        self.acc = vec(0,0)

    def update(self, allSprites):
        self.acc = vec(0,0)
 
        pressedKeys = pygame.key.get_pressed()

        #Movement input detection
        if pressedKeys[K_LEFT]:
            self.acc.x = -pSpeed
        if pressedKeys[K_RIGHT]:
           self.acc.x = pSpeed
        if pressedKeys[K_UP]:
            self.acc.y = -pSpeed
        if pressedKeys[K_DOWN]:
           self.acc.y = pSpeed
    
        if self.acc.x and self.acc.y:
            self.acc.x /= 2 ** 0.5
            self.acc.y /= 2 ** 0.5

        #Collision detection
        obstacles = [sprite for sprite in allSprites if isinstance(sprite, Obstacle)]
        
        self.rect.x += self.acc.x
        for obstacle in pygame.sprite.spritecollide(self, obstacles, False):
            if self.acc.x > 0:
                self.rect.right = obstacle.rect.left
            if self.acc.x < 0:
                self.rect.left = obstacle.rect.right
        self.rect.y += self.acc.y
        for wall in pygame.sprite.spritecollide(self, obstacles, False):
            if self.acc.y > 0:
                self.rect.top = obstacle.rect.bottom
            if self.acc.y < 0:
                self.rect.bottom = obstacle.rect.top
