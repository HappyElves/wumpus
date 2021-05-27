import pygame
from pygame.locals import *

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, imagePath):
        super().__init__()
        if imagePath:
            self.image = pygame.image.load(imagePath).convert
        self.rect = self.image.get_rect(center=center)
