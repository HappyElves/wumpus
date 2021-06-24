import pygame
from pygame.locals import *
from library.map import Obstacle
#from library.enemy import Enemy, EnemyBullet
pygame.init()
vec = pygame.math.Vector2  # 2 for two dimensional

height = 450 #height of screen
width = 400
pSpeed = 5 #player speed

#pressedKeys = pygame.key.get_pressed()

class Heart(pygame.sprite.Sprite):
    def __init__(self, center=(0,0)):
        super().__init__()

        self.image = pygame.transform.scale(pygame.image.load('assets/heart.png').convert_alpha(), (70, 70))
        self.rect = self.image.get_rect(center=center)

    def update(self, allSprites):
        possiblePlayer = [sprite for sprite in allSprites if isinstance(sprite, Player)]
        player = possiblePlayer[0]
        if player.hp == 2:
            if self.rect.x == 155:
                self.kill()
                return
        if player.hp == 1:
            if self.rect.x == 85:
                self.kill()
                return
        if player.hp == 0:
            if self.rect.x == 15:
                self.kill()
                return
            

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 

        self.image = pygame.transform.scale(pygame.image.load('assets/player.png').convert_alpha(), (60, 60))
        self.rect = self.image.get_rect(center = (width/2, height/2))
        
        self.acc = vec(0,0)
        self.attackDelay = 30
        self.damageDelay = 100
        self.hp = 3
        self.hearts = pygame.sprite.Group()
        
        self.bullets = pygame.sprite.Group()

        self.hearts.add(Heart((50, 30)))
        self.hearts.add(Heart((120, 30)))
        self.hearts.add(Heart((190, 30)))

    def update(self, allSprites):
        self.acc = vec(0,0)
 
        pressedKeys = pygame.key.get_pressed()

        #Movement input detection
        if pressedKeys[K_a]:
            self.acc.x = -pSpeed
        if pressedKeys[K_d]:
           self.acc.x = pSpeed
        if pressedKeys[K_w]:
            self.acc.y = -pSpeed
        if pressedKeys[K_s]:
           self.acc.y = pSpeed
    
        if self.acc.x and self.acc.y:
            self.acc.x /= 2 ** 0.5
            self.acc.y /= 2 ** 0.5
            
        self.damageDelay -= 1
        if self.damageDelay <=0:
            enemies = [sprite for sprite in allSprites if isinstance(sprite, (Enemy, EnemyBullet))]
            enemiesCollided = pygame.sprite.spritecollide(self, enemies, False)
            if enemiesCollided:
                self.hp -= 1
                self.damageDelay = 100
                if self.hp == 0:
                    pygame.quit()
                    sys.exit()
        
        #Collision detection
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
        arrowKeys = {pygame.K_UP:vec(0,-1), pygame.K_DOWN:vec(0,1), pygame.K_LEFT:vec(-1,0), pygame.K_RIGHT:vec(1, 0)}

        #Shoot bullets
        self.bullets = pygame.sprite.Group()
        self.attackDelay -= 1
        if self.attackDelay <= 0:
            if [key for key in arrowKeys if pressedKeys[key]]:
                self.attackDelay = 30
                direction = vec(0,0)
                pressedList = [key for key in arrowKeys if pressedKeys[key]]
                for key in pressedList:

                    if key == pygame.K_UP or key == pygame.K_DOWN:
                        direction.y = arrowKeys[key].y
  
                    if key == pygame.K_LEFT or key == pygame.K_RIGHT:
                        direction.x = arrowKeys[key].x
                        

                #bullet = Bullet('assets/bullet.png', direction)
                self.bullets.add(Bullet('assets/bullet.png', direction, self.rect.center))
        
    

class Bullet(pygame.sprite.Sprite):
    def __init__(self, bulletImage ,direction=vec(0,0), center=(0,0)):
        super().__init__()
        
        self.image = pygame.transform.scale(pygame.image.load('assets/arrow.png').convert_alpha(), (20,20))
        self.rect = self.image.get_rect(center=center)
        self.dir = direction * 6
        
    def update(self, allSprites):
        self.rect.move_ip(self.dir)
        
        obstacles = [sprite for sprite in allSprites if isinstance(sprite, Obstacle)]
        if pygame.sprite.spritecollideany(self, obstacles):
            self.kill()
            return
        if self.rect.x > width*2 or self.rect.y > height:
            self.kill()
            return
            
from library.enemy import Enemy, EnemyBullet
