import pygame
import os
import time
import ctypes
import random


user32 = ctypes.windll.user32


WIDTH =  user32.GetSystemMetrics(78)
HEIGHT =  user32.GetSystemMetrics(79)


pygame.display.set_caption('SpaceShooter')
WINDOW=pygame.display.set_mode((WIDTH,HEIGHT),pygame.FULLSCREEN)

#enemy data
ENEMY_SHIP=pygame.transform.scale(pygame.image.load(os.path.join("assets", "przeciwnik.png")),(100,100))

ENEMY_BULLET=pygame.transform.scale(pygame.image.load(os.path.join("assets", "pocisk.png")),(10,10))

#player data
PLAYER_SHIP=pygame.transform.scale(pygame.image.load(os.path.join("assets", "stateczek.png")),(100,100))

PLAYER_BULLET=pygame.transform.scale(pygame.image.load(os.path.join("assets", "pocisk.png")),(10,10))

#buttons
START_BUTTON=pygame.transform.scale(pygame.image.load(os.path.join("assets", "start_button.png")),(300,100))


#background
STARTING_BACKGROUND=pygame.transform.scale(pygame.image.load(os.path.join("assets", "menu.png")),(WIDTH,HEIGHT))
BACKGROUND=pygame.transform.scale(pygame.image.load(os.path.join("assets", "kosmos.png")),(WIDTH,HEIGHT))

class Button():
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.clicked = False

	def draw(self):
		action = False

		
		pos = pygame.mouse.get_pos()

		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				action = True
				self.clicked = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		WINDOW.blit(self.image, self.rect)

		return action


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

    #def collision(self, obj):
    #    return collide(self, obj)


class Ship:

    COOLDOWN = 30
    def __init__(self,x,y, health=100):
        self.x=x
        self.y=y
        self.health = health
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

    def move_bullet(self, vel, obj):
        self.cooldown()
        for bullet in self.bullets:
            bullet.move(vel)
            if bullet.off_screen(HEIGHT):
                self.bullets.remove(bullet)
            #elif bullet.collision(obj):
             #   obj.health -= 10
             #   self.bullets.remove(bullet)

   
           
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
    def __init__(self,x,y, health=100):
        super().__init__(x,y)
        self.ship_img=PLAYER_SHIP
        self.bullet_img=PLAYER_BULLET
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

    def move_bullet(self, vel, objs):
        self.cooldown()
        for bullet in self.bullets:
            bullet.move(vel)
            if bullet.off_screen(HEIGHT):
                self.bullets.remove(bullet)
            #else:
              #  for obj in objs:
                #    if bullet.collision(obj):
                #        objs.remove(obj)
                 #       if bullet in self.bullets:
                   #         self.bullets.remove(bullet)
                




class Enemy(Ship):
    TYPE_MAP = {
               "przeciwnik": (ENEMY_SHIP, ENEMY_BULLET), 
               }
    def __init__(self, x, y, type, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.bullet_img = self.TYPE_MAP[type]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y += vel

    def shoot(self):
        if self.cooldown_counter == 0:
            bullet = Bullet(self.x+45, self.y+100, self.bullet_img)
            self.bullets.append(bullet)
            self.cooldown_counter = 1


def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None #################

def main():
    run = True
    FPS = 60
    level = 0
    lives = 3
    player = Player(WIDTH/2-45,650)
    main_menu = True 

    enemies = []
    wave_length = 5
    enemy_vel = 3
    bullet_vel = 5

    player_vel=5

    lost = False
    lost_count = 0

    start_button=Button(WIDTH/2-150 , HEIGHT/2+200, START_BUTTON)
    clock = pygame.time.Clock()
    def redraw_w():
        WINDOW.blit(BACKGROUND, (0,0))

        for enemy in enemies:
            enemy.draw(WINDOW)

        player.draw(WINDOW)
        pygame.display.update()

    


    while run:
        clock.tick(FPS)
        keys=pygame.key.get_pressed()
        if main_menu == True:
            WINDOW.blit(STARTING_BACKGROUND,(0,0))
            if start_button.draw():
                main_menu=False
            pygame.display.update()
            
             
        else:
            redraw_w()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
        
        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

        #if lost:
         #   if lost_count > FPS * 3:
         #       run = False
         #   else:
           #     continue

        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice(["przeciwnik"]))
                enemies.append(enemy)
  

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
        if keys[pygame.K_ESCAPE]:
            run=False

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_bullet(bullet_vel, player)

            if random.randrange(0, 2*60) == 1:
                enemy.shoot()

            #if collide(enemy, player):
             #   player.health -= 10
             #   enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > HEIGHT+100:
                lives -= 1
                enemies.remove(enemy)

        player.move_bullet(-10, enemies)
            
main()




