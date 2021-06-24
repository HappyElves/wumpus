import random
import pygame
from pygame.locals import *
from library.player import *
from library.map import Obstacle
ph1 = True
eSpeed = 1
ebspeed = 2
pygame.init()
vec = pygame.math.Vector2  # 2 for two dimensional
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.transform.scale(pygame.image.load('assets/enemy.png').convert_alpha(), (100, 100))
        self.rect = self.image.get_rect(center = (300, 300))

        self.attackDelay = 30
        self.bullets = pygame.sprite.Group()
        
        self.hp = 10
        self.damageDelay = 20


        
    def update(self, allSprites):
        possiblePlayer = [sprite for sprite in allSprites if isinstance(sprite, Player)]
        player = possiblePlayer[0]
        self.acc = vec(0,0)
        if self.rect.x < (player.rect.x - 50):
            self.acc.x = eSpeed
        if self.rect.x > (player.rect.x + 50):
            self.acc.x = -eSpeed
        if self.rect.y < (player.rect.y - 50):
            self.acc.y = eSpeed
        if self.rect.y > (player.rect.y + 50):
            self.acc.y = -eSpeed

        self.damageDelay -= 1
        if self.damageDelay <=0:
            enemies = [sprite for sprite in allSprites if isinstance(sprite, (Bullet))]
            enemiesCollided = pygame.sprite.spritecollide(self, enemies, False)
            if enemiesCollided:
                self.hp -= 1
                self.damageDelay = 100
                if self.hp < 7:
                    ph1 = False
                    ph2 = True
                if self.hp == 0:
                    self.kill()
        
        obstacles = [sprite for sprite in allSprites if isinstance(sprite, Obstacle)]
        self.rect.x += self.acc.x
        for obstacle in pygame.sprite.spritecollide(self, obstacles, False):
            if self.acc.x > 0:
                self.rect.right = obstacle.rect.left
            if self.acc.x < 0:
                self.rect.left = obstacle.rect.right
        self.rect.y += self.acc.y
        for obstacle in pygame.sprite.spritecollide(self, obstacles, False):
            if self.acc.y < 0:
                self.rect.top = obstacle.rect.bottom
            if self.acc.y > 0:
                self.rect.bottom = obstacle.rect.top
        self.attackDelay -=1
        if self.attackDelay <= 0:
            if ph1 == True:
                self.attackDelay = 30
                direction = pygame.Vector2(player.rect.center) - pygame.Vector2(self.rect.center)
                direction = direction.normalize() * 6
                self.bullets.add(EnemyBullet('assets/bullet.png', direction, self.rect.center))

            #if ph2

class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, bulletImage ,direction=vec(0,0), center=(0,0)):
        super().__init__()
        
        self.image = pygame.transform.scale(pygame.image.load('assets/bullet.png').convert_alpha(), (30, 30))
        self.rect = self.image.get_rect(center=center)
        self.dir = direction
        
    def update(self, allSprites):
        self.rect.move_ip(self.dir)
        
        obstacles = [sprite for sprite in allSprites if isinstance(sprite, Obstacle)]
        if pygame.sprite.spritecollideany(self, obstacles):
            self.kill()
            return
        if self.rect.x > width*2 or self.rect.y > height:
            self.kill()
            return
    
            
