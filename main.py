import pygame
from pygame.locals import *
 
pygame.init()
vec = pygame.math.Vector2  # 2 for two dimensional
 
HEIGHT = 450
WIDTH = 400
pSpeed = 5 #player speed
FPS = 60

#Sets up the game clock and window
FramePerSec = pygame.time.Clock()
 
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Movement Test")


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect(center = (10, 420))
        
        self.pos = vec((10, 385))
        self.acc = vec(0,0)

def move(self):
    self.acc = vec(0,0)
 
    pressedKeys = pygame.key.get_pressed()
    
    if pressedKeys[K_LEFT]:
        self.acc.x = -pSpeed
    if pressedKeys[K_RIGHT]:
       self.acc.x = pSpeed
    if pressedKeys[K_UP]:
        self.acc.y = -pSpeed
    if pressedKeys[K_DOWN]:
       self.acc.y = pSpeed

   
    self.pos += self.acc
        
    self.rect.midbottom = self.pos

P1 = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
     
    displaysurface.fill((0,0,0)) #resets screen
 
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect) #writes
 
    pygame.display.update()
    FramePerSec.tick(FPS)
    
    move(P1)
