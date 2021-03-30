import pygame
import os
import time

 #cokolwiek
 #asdasd
 #halaoihsaohsao

WIDTH = 850
HEIGHT = 850
WINDOW=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('SpaceShooter')


#player data
PLAYER_SHIP=pygame.transform.scale(pygame.image.load(os.path.join("assets", "stateczek.png")),(100,100))

PLAYER_BULLET=pygame.transform.scale(pygame.image.load(os.path.join("assets", "pocisk.png")),(10,10))

#background
BACKGROUND=pygame.transform.scale(pygame.image.load(os.path.join("assets", "kosmos.png")),(WIDTH,HEIGHT))

class Bullet:
    def __init__(self,x,y,img):
        self.x=x
        self.y=y
        self.bullet_img=img
        self.mask = pygame.mask.from_surface(self.bullet_img)

    def draw(self,window):
        window.blit(self.bullet_img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return not self.y <= height and self.y >= 0


class Ship:

    COOLDOWN = 30
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.ship_img = None
        self.bullet_img = None
        self.bullets = []
        self.cooldown_counter = 0

    def draw(self,window):
        window.blit(self.ship_img, (self.x,self.y))
        for bullet in self.bullets:
            bullet.draw(window)

    def shoot(self):
        if self.cooldown_counter == 0:
            bullet = Bullet(self.x + 45, self.y, self.bullet_img)
            self.bullets.append(bullet)
            self.cooldown_counter = 1

    def move_bullet(self, vel):
        self.cooldown()
        for bullet in self.bullets:
            bullet.move(vel)
            if bullet.off_screen(HEIGHT):
                self.bullets.remove(bullet)
   
           
    def cooldown(self):
        if self.cooldown_counter >=self.COOLDOWN:
            self.cooldown_counter=0
        elif self.cooldown_counter>0 :
            self.cooldown_counter +=1



    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

class Player(Ship):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.ship_img=PLAYER_SHIP
        self.bullet_img=PLAYER_BULLET
        self.mask = pygame.mask.from_surface(self.ship_img)



def main():
    run = True
    FPS = 60
    player = Player(300,650)

    player_vel=5
 
    clock = pygame.time.Clock()
    def redraw_w():
        WINDOW.blit(BACKGROUND, (0,0))

        player.draw(WINDOW)
        pygame.display.update()




    while run:
        clock.tick(FPS)
        redraw_w()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
        keys=pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0:
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH:
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel > 0:
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel + player.get_height() < HEIGHT:
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()

        player.move_bullet(-10)

            
main()




