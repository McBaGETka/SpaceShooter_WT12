import pygame
import os
import time
import ctypes
import random
pygame.font.init()

from pygame import mixer

user32 = ctypes.windll.user32


WIDTH =  user32.GetSystemMetrics(0)
HEIGHT =  user32.GetSystemMetrics(1)
#print(WIDTH,HEIGHT)

pygame.display.set_caption('SpaceShooter')
WINDOW=pygame.display.set_mode((WIDTH,HEIGHT),pygame.FULLSCREEN)
mixer.init()
#resolution variables
ENEMY_VAR=int(WIDTH*0.039) #75px
ENEMY_S_VAR=int(WIDTH*0.02) #40ox
SKIN_SHOW=int(WIDTH*0.182) #350px
SKIN_SHOW_POS=int(WIDTH*0.13) #250px
BOSS_X=int(WIDTH*0.26) #500px
BOSS_Y=int(WIDTH*0.104) #200px

BUTTON_X_1=int(WIDTH*0.156) #300px
BUTTON_Y_1=int(WIDTH*0.052) #100px
BUTTON_2=int(WIDTH*0.104) #200px

HP_BOR_X=int(WIDTH*0.158) #300px
HP_BOR_Y=int(WIDTH*0.028) #50px

HP_POS_X=int(WIDTH*0.052) #100px
HP_POS_Y=int(HEIGHT*0.138) #150px

GAMEPLAY_BORDER=int(WIDTH*0.234) #450px
GAMEPLAY_SITE=WIDTH-2*GAMEPLAY_BORDER

#enemy data
ENEMY_SHIP=pygame.transform.scale(pygame.image.load(os.path.join("assets", "przeciwnik.png")).convert_alpha(),(ENEMY_VAR,ENEMY_VAR))
ENEMY_SHIP_CHARGE=pygame.transform.scale(pygame.image.load(os.path.join("assets", "enemy_charge.png")).convert_alpha(),(ENEMY_VAR,ENEMY_VAR))
ENEMY_SHIP_CHARGE_ANGRY=pygame.transform.scale(pygame.image.load(os.path.join("assets", "enemy_charge_angry.png")).convert_alpha(),(ENEMY_VAR,ENEMY_VAR))
ENEMY_SHIP_SHOTGUN=pygame.transform.scale(pygame.image.load(os.path.join("assets", "enemy_shotgun.png")).convert_alpha(),(ENEMY_VAR,ENEMY_S_VAR))
BOSS_SHIP=pygame.transform.scale(pygame.image.load(os.path.join("assets", "boss_ship.png")).convert_alpha(),(BOSS_X,BOSS_Y))

BOSS_MINE_CIRCLE=pygame.transform.scale(pygame.image.load(os.path.join("assets", "mine_circle.png")).convert_alpha(),(HP_POS_X,HP_POS_X))


ENEMY_BULLET=pygame.transform.scale(pygame.image.load(os.path.join("assets", "pocisk.png")).convert_alpha(),(8,8))
ENEMY_BULLET_2=pygame.transform.scale(pygame.image.load(os.path.join("assets", "bullet2.png")).convert_alpha(),(10,10))


#player data
PLAYER_SHIP=pygame.transform.scale(pygame.image.load(os.path.join("assets", "stateczek.png")).convert_alpha(),(SKIN_SHOW,SKIN_SHOW))
PLAYER_SHIP_WHITE=pygame.transform.scale(pygame.image.load(os.path.join("assets", "stateczek_white.png")).convert_alpha(),(SKIN_SHOW,SKIN_SHOW))
PLAYER_SHIP_BLUE=pygame.transform.scale(pygame.image.load(os.path.join("assets", "stateczek_blue.png")).convert_alpha(),(SKIN_SHOW,SKIN_SHOW))
PLAYER_SHIP_YELLOW=pygame.transform.scale(pygame.image.load(os.path.join("assets", "stateczek_yellow.png")).convert_alpha(),(SKIN_SHOW,SKIN_SHOW))

PLAYER_BULLET=pygame.transform.scale(pygame.image.load(os.path.join("assets", "pocisk.png")),(8,8))


#animations
EXPLOSION=[pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/explosion", "e1.png")).convert_alpha(),(ENEMY_VAR,ENEMY_VAR)),
           pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/explosion", "e2.png")).convert_alpha(),(ENEMY_VAR,ENEMY_VAR)),
           pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/explosion", "e3.png")).convert_alpha(),(ENEMY_VAR,ENEMY_VAR)),
           pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/explosion", "e4.png")).convert_alpha(),(ENEMY_VAR,ENEMY_VAR)),
           pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/explosion", "e5.png")).convert_alpha(),(ENEMY_VAR,ENEMY_VAR))]

BOSS_MINE_READY=[pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/bomb", "bomb_ready1.png")).convert_alpha(),(HP_POS_X,HP_POS_X)),
                pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/bomb", "bomb_ready2.png")).convert_alpha(),(HP_POS_X,HP_POS_X)),
                pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/bomb", "bomb_ready3.png")).convert_alpha(),(HP_POS_X,HP_POS_X)),
                pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/bomb", "bomb_ready4.png")).convert_alpha(),(HP_POS_X,HP_POS_X)),
                pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/bomb", "bomb_ready5.png")).convert_alpha(),(HP_POS_X,HP_POS_X)),
                pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/bomb", "bomb_ready6.png")).convert_alpha(),(HP_POS_X,HP_POS_X)),]

SHIP1=[pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/1podstawowy", "statek1a.png")).convert_alpha(),(ENEMY_VAR,ENEMY_VAR)),
       pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/1podstawowy", "statek1b.png")).convert_alpha(),(ENEMY_VAR,ENEMY_VAR)),
       pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/1podstawowy", "statek1c.png")).convert_alpha(),(ENEMY_VAR,ENEMY_VAR)),
       pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/1podstawowy", "statek1d.png")).convert_alpha(),(ENEMY_VAR,ENEMY_VAR)),
       pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/1podstawowy", "statek1c.png")).convert_alpha(),(ENEMY_VAR,ENEMY_VAR)),
       pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/1podstawowy", "statek1b.png")).convert_alpha(),(ENEMY_VAR,ENEMY_VAR))]

SHIP2=[pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/2niebieski", "statek2a.png")).convert_alpha(),(ENEMY_VAR,ENEMY_VAR)),
       pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/2niebieski", "statek2b.png")).convert_alpha(),(ENEMY_VAR,ENEMY_VAR)),
       pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/2niebieski", "statek2c.png")).convert_alpha(),(ENEMY_VAR,ENEMY_VAR)),
       pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/2niebieski", "statek2d.png")).convert_alpha(),(ENEMY_VAR,ENEMY_VAR)),
       pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/2niebieski", "statek2c.png")).convert_alpha(),(ENEMY_VAR,ENEMY_VAR)),
       pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/2niebieski", "statek2b.png")).convert_alpha(),(ENEMY_VAR,ENEMY_VAR))]

SHIP3=[pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/3zielony", "statek4a.png")).convert_alpha(),(ENEMY_VAR,ENEMY_VAR)),
       pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/3zielony", "statek4b.png")).convert_alpha(),(ENEMY_VAR,ENEMY_VAR)),
       pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/3zielony", "statek4c.png")).convert_alpha(),(ENEMY_VAR,ENEMY_VAR)),
       pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/3zielony", "statek4d.png")).convert_alpha(),(ENEMY_VAR,ENEMY_VAR)),
       pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/3zielony", "statek4c.png")).convert_alpha(),(ENEMY_VAR,ENEMY_VAR)),
       pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/3zielony", "statek4b.png")).convert_alpha(),(ENEMY_VAR,ENEMY_VAR))]

SHIP4=[pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/4zolty", "statek3a.png")).convert_alpha(),(ENEMY_VAR,ENEMY_VAR)),
       pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/4zolty", "statek3b.png")).convert_alpha(),(ENEMY_VAR,ENEMY_VAR)),
       pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/4zolty", "statek3c.png")).convert_alpha(),(ENEMY_VAR,ENEMY_VAR)),
       pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/4zolty", "statek3d.png")).convert_alpha(),(ENEMY_VAR,ENEMY_VAR)),
       pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/4zolty", "statek3c.png")).convert_alpha(),(ENEMY_VAR,ENEMY_VAR)),
       pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/4zolty", "statek3b.png")).convert_alpha(),(ENEMY_VAR,ENEMY_VAR))]

#button animations
START_BUTTON=[pygame.transform.scale(pygame.image.load(os.path.join("assets", "start_button.png")).convert_alpha(),(BUTTON_X_1,BUTTON_Y_1)),
              pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/buttons", "start_button1.png")).convert_alpha(),(BUTTON_X_1,BUTTON_Y_1))]

OPTIONS_BUTTON=[pygame.transform.scale(pygame.image.load(os.path.join("assets", "options_button.png")).convert_alpha(),(BUTTON_X_1,BUTTON_Y_1)),
                pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/buttons", "options_button1.png")).convert_alpha(),(BUTTON_X_1,BUTTON_Y_1))]

RECORDS_BUTTON=[pygame.transform.scale(pygame.image.load(os.path.join("assets", "records_button.png")).convert_alpha(),(BUTTON_X_1,BUTTON_Y_1)),
                pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/buttons", "records_button1.png")).convert_alpha(),(BUTTON_X_1,BUTTON_Y_1))]

EXIT_BUTTON=[pygame.transform.scale(pygame.image.load(os.path.join("assets", "exit_button.png")).convert_alpha(),(BUTTON_X_1,BUTTON_Y_1)),
             pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/buttons", "exit_button1.png")).convert_alpha(),(BUTTON_X_1,BUTTON_Y_1))]

ARROW_LEFT=[pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/buttons", "arrow_left.png")).convert_alpha(),(BUTTON_2,BUTTON_2)),
            pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/buttons", "arrow_left1.png")).convert_alpha(),(BUTTON_2,BUTTON_2))]

ARROW_RIGHT=[pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/buttons", "arrow_right.png")).convert_alpha(),(BUTTON_2,BUTTON_2)),
             pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/buttons", "arrow_right1.png")).convert_alpha(),(BUTTON_2,BUTTON_2))]

SKIN_CHANGE_BUTTON=[pygame.transform.scale(pygame.image.load(os.path.join("assets", "options_button.png")).convert_alpha(),(BUTTON_X_1,BUTTON_Y_1)),
                    pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/buttons", "options_button1.png")).convert_alpha(),(BUTTON_X_1,BUTTON_Y_1))]

BACK_BUTTON=[pygame.transform.scale(pygame.image.load(os.path.join("assets", "back_button.png")).convert_alpha(),(BUTTON_2,BUTTON_2)),
             pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/buttons", "back_button1.png")).convert_alpha(),(BUTTON_2,BUTTON_2))]


#background
STARTING_BACKGROUND=pygame.transform.scale(pygame.image.load(os.path.join("assets", "menu.png")).convert(),(WIDTH,HEIGHT))
SKIN_CHANGE_BACKGROUND=pygame.transform.scale(pygame.image.load(os.path.join("assets", "skin_change_background.png")).convert(),(WIDTH,HEIGHT))
TABLE_OF_RECORDS_BACKGROUND=pygame.transform.scale(pygame.image.load(os.path.join("assets", "table_of_records_background.png")).convert(),(WIDTH,HEIGHT))
BACKGROUND=pygame.transform.scale(pygame.image.load(os.path.join("assets", "kosmos1.png")).convert(),(WIDTH,HEIGHT))
OVERLAY=pygame.transform.scale(pygame.image.load(os.path.join("assets", "overlay.png")).convert_alpha(),(WIDTH,HEIGHT))
HP_BORDER=pygame.transform.scale(pygame.image.load(os.path.join("assets", "hp_border.png")).convert_alpha(),(HP_BOR_X,HP_BOR_Y))
VICTORY=pygame.transform.scale(pygame.image.load(os.path.join("assets", "victory.png")).convert(),(WIDTH,HEIGHT))
GAME_OVER=pygame.transform.scale(pygame.image.load(os.path.join("assets", "game_over.png")).convert(),(WIDTH,HEIGHT))



#SOUNDS
pygame.mixer.music.load("assets/bg_song.ogg")
PLAYER_SHOOT=pygame.mixer.Sound("assets/player_shoot.mp3")
PLAYER_SHOOT.set_volume(0.05)
CLICK_SOUND=pygame.mixer.Sound("assets/click.wav")
CLICK_SOUND.set_volume(0.05)
ENEMY_HIT=pygame.mixer.Sound("assets/enemy_hit.mp3")
ENEMY_HIT.set_volume(0.03)

BOSS_CHARGE=pygame.mixer.Sound("assets/boss_charge.wav")
BOSS_CHARGE.set_volume(0.15)
BOSS_BOMB=pygame.mixer.Sound("assets/bomb.wav")
BOSS_BOMB.set_volume(0.1)


class Button():
    def __init__(self, x, y, image):
        self.image = image[0]
        self.image_anim=image[1]
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
                pygame.mixer.Sound.play(CLICK_SOUND)
                WINDOW.blit(self.image_anim, self.rect)
                return action


        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False


        WINDOW.blit(self.image, self.rect)
        

        return action



class Explosion:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.lifespan=0

    def anim(self):
        WINDOW.blit(EXPLOSION[self.lifespan//10], (self.x, self.y))
        self.lifespan+=1

    def return_lifespan(self):
        return self.lifespan


class Bomb:
     def __init__(self,x,y):
        self.x=x
        self.y=y
        self.img =BOSS_MINE_CIRCLE
        self.mask = pygame.mask.from_surface(BOSS_MINE_READY[0])
        self.lifespan=0
        self.anim=0

     def draw(self):
        if self.lifespan<100:
            WINDOW.blit(self.img, (self.x, self.y))
        else:
            self.anim+=1
            WINDOW.blit(BOSS_MINE_READY[self.anim//10], (self.x, self.y))

        self.lifespan+=1

     def collision(self, obj):
        return collide(self, obj)

     def return_lifespan(self):
        return self.lifespan



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
        if self.y <= height and self.y >= 0:
            return False
        else:
            return True

    def collision(self, obj):
        return collide(self, obj)

class Bullet_SRS(Bullet): #full name Bullet Spread Right Short
    def move(self, vel):
        self.y += vel
        self.x += vel*0.05

class Bullet_SLS(Bullet): #full name Bullet Spread Left Short
    def move(self, vel):
        self.y += vel
        self.x -= vel*0.05

class Bullet_SRL(Bullet): #full name Bullet Spread Right Long
    def move(self, vel):
        self.y += vel
        self.x += vel*0.1

class Bullet_SLL(Bullet): #full name Bullet Spread Left Long
    def move(self, vel):
        self.y += vel
        self.x -= vel*0.1


class Ship:

    COOLDOWN = 50
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
            pygame.mixer.Sound.play(PLAYER_SHOOT)
            bullet = Bullet(self.x +self.ship_img.get_width()/2-5, self.y, self.bullet_img)
            self.bullets.append(bullet)
            self.cooldown_counter = 1

   
           
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
    def __init__(self,x,y,ship_options, health=100):
        super().__init__(x,y)
        if ship_options==0:
            self.ship_img=SHIP1[ex_count//20]
        elif ship_options==1:
            self.ship_img=SHIP2[ex_count//20]
        elif ship_options==2:
            self.ship_img=SHIP3[ex_count//20]
        elif ship_options==3:
            self.ship_img=SHIP4[ex_count//20]
        self.bullet_img=PLAYER_BULLET
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health
        self.points=0
        self.flawless=True

    def move_bullet(self, vel, objs,expl):
        self.cooldown()
        global multiplier
        for bullet in self.bullets:
            bullet.move(vel)
            if bullet.off_screen(HEIGHT):
                self.bullets.remove(bullet)
            else:
                for obj in objs:
                    if bullet.collision(obj):
                        pygame.mixer.Sound.play(ENEMY_HIT)
                        explosion=Explosion(bullet.x-25,bullet.y-20)
                        expl.append(explosion)
                        obj.health-=100
                        if self.flawless==True and obj.health<=0:
                            multiplier+=0.5
                        else:
                            self.flawless=True


                        self.points+=obj.return_value()*multiplier  
                        
                        
                        if bullet in self.bullets:
                            self.bullets.remove(bullet)

    def get_hit(self,val):
        global multiplier
        self.flawless=False
        multiplier=1
        self.health -= val



    def anim(self,ex_count,ship_option):
        if ship_option==0:
            self.ship_img=SHIP1[ex_count//20]
        elif ship_option==1:
            self.ship_img=SHIP2[ex_count//20]
        elif ship_option==2:
            self.ship_img=SHIP3[ex_count//20]
        elif ship_option==3:
            self.ship_img=SHIP4[ex_count//20]



    def border_pass(self):
        self.points-=50
        

    def get_points(self):
        return self.points

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)



    def healthbar(self, window):
        pygame.draw.rect(window, (255,0,0), (HP_POS_X, HP_POS_Y, 300, 50))
        pygame.draw.rect(window, (0,255,0), (HP_POS_X, HP_POS_Y, 300* (self.health/self.max_health), 50))


class Enemy(Ship):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.ship_img=ENEMY_SHIP
        self.bullet_img =ENEMY_BULLET
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.value=100
        self.health=100

    def move(self, vel):
        self.y += vel

    def shoot(self,objs):
        if self.cooldown_counter==0 and random.randrange(60)==1:
            bullet = Bullet(self.x+37, self.y+80, self.bullet_img)
            objs.append(bullet)
            self.cooldown_counter=1
            
    
    def return_value(self):
        return self.value


class Boss(Ship):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.ship_img=BOSS_SHIP
        self.bullet_img =ENEMY_BULLET
        self.bullet_img_2=ENEMY_BULLET_2
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.health=7000
        self.max_health=7000
        self.value=0
        self.direction_x=0
        self.direction_y=1
        self.attack_dur=0
        self.attack_pattern=2
        self.idle=False
        self.charge=False

    def move(self, vel):
        if self.charge==True:
            if self.idle==False:
                if self.attack_dur<30:
                    self.y-=1;
                else:
                    self.y+=vel*5
            
                if self.y>HEIGHT+200:
                    self.y=-BOSS_Y
                    self.idle=True
            else:
                self.y+=vel
                if self.y>=100:
                    self.charge=False

        else:
            if self.direction_x==0:
                self.x+=3
                if self.x + self.get_width()>=WIDTH-GAMEPLAY_BORDER:
                    self.direction_x=1
            if self.direction_x==1:
                self.x-=3
                if self.x<=GAMEPLAY_BORDER:
                    self.direction_x=0
            if self.direction_y>0:
                self.y+=1
                self.direction_y+=1
                if self.direction_y>=100:
                    self.direction_y=-1
            if self.direction_y<0:
                self.y-=1
                self.direction_y-=1
                if self.direction_y<=-100:
                    self.direction_y=1


        

    def shoot(self,objs,bombs):
        if self.attack_pattern==0:
            if self.cooldown_counter==0:
                bullet = Bullet(self.x+int(self.get_width()*0.14), self.y+BOSS_Y, self.bullet_img)
                bullet2 = Bullet(self.x+int(self.get_width()*0.28), self.y+BOSS_Y, self.bullet_img)
                bullet3 = Bullet(self.x+int(self.get_width()*0.42), self.y+BOSS_Y, self.bullet_img)
                bullet4 = Bullet(self.x+int(self.get_width()/2), self.y+BOSS_Y, self.bullet_img)
                bullet5 = Bullet(self.x+int(self.get_width()*0.64), self.y+BOSS_Y, self.bullet_img)
                bullet6 = Bullet(self.x+int(self.get_width()*0.78), self.y+BOSS_Y, self.bullet_img)
                bullet7 = Bullet(self.x+int(self.get_width()*0.92), self.y+BOSS_Y, self.bullet_img)
                objs.append(bullet)
                objs.append(bullet2)
                objs.append(bullet3)
                objs.append(bullet4)
                objs.append(bullet5)
                objs.append(bullet6)
                objs.append(bullet7)
                self.cooldown_counter=1


        elif self.attack_pattern==1:
            if self.cooldown_counter==0:
                bullet = Bullet(self.x+40, self.y+BOSS_Y,  self.bullet_img_2)
                bulletsrs = Bullet_SRS(self.x+40, self.y+BOSS_Y,  self.bullet_img_2)
                bulletsls = Bullet_SLS(self.x+40, self.y+BOSS_Y,  self.bullet_img_2)
                bulletsrl = Bullet_SRL(self.x+40, self.y+BOSS_Y,  self.bullet_img_2)
                bulletsll = Bullet_SLL(self.x+40, self.y+BOSS_Y,  self.bullet_img_2)
                objs.append(bullet)
                objs.append(bulletsrs)
                objs.append(bulletsls)
                objs.append(bulletsrl)
                objs.append(bulletsll)

                bullet = Bullet(self.x+self.get_width()/2, self.y+BOSS_Y-20,  self.bullet_img_2)
                bulletsrs = Bullet_SRS(self.x+self.get_width()/2, self.y+BOSS_Y-20,  self.bullet_img_2)
                bulletsls = Bullet_SLS(self.x+self.get_width()/2, self.y+BOSS_Y-20,  self.bullet_img_2)
                bulletsrl = Bullet_SRL(self.x+self.get_width()/2, self.y+BOSS_Y-20,  self.bullet_img_2)
                bulletsll = Bullet_SLL(self.x+self.get_width()/2, self.y+BOSS_Y-20,  self.bullet_img_2)
                objs.append(bullet)
                objs.append(bulletsrs)
                objs.append(bulletsls)
                objs.append(bulletsrl)
                objs.append(bulletsll)

                bullet = Bullet(self.x+self.get_width()-40, self.y+BOSS_Y,  self.bullet_img_2)
                bulletsrs = Bullet_SRS(self.x+self.get_width()-40, self.y+BOSS_Y,  self.bullet_img_2)
                bulletsls = Bullet_SLS(self.x+self.get_width()-40, self.y+BOSS_Y,  self.bullet_img_2)
                bulletsrl = Bullet_SRL(self.x+self.get_width()-40, self.y+BOSS_Y,  self.bullet_img_2)
                bulletsll = Bullet_SLL(self.x+self.get_width()-40, self.y+BOSS_Y,  self.bullet_img_2)
                objs.append(bullet)
                objs.append(bulletsrs)
                objs.append(bulletsls)
                objs.append(bulletsrl)
                objs.append(bulletsll)
                self.cooldown_counter=1

        

        elif self.attack_pattern==2:
            bomb=Bomb(random.randrange(GAMEPLAY_BORDER+100,WIDTH-GAMEPLAY_BORDER-100),random.randrange(400,HEIGHT-100))
            bomb2=Bomb(random.randrange(GAMEPLAY_BORDER+100,WIDTH-GAMEPLAY_BORDER-100),random.randrange(400,HEIGHT-100))
            bomb3=Bomb(random.randrange(GAMEPLAY_BORDER+100,WIDTH-GAMEPLAY_BORDER-100),random.randrange(400,HEIGHT-100))
            bomb4=Bomb(random.randrange(GAMEPLAY_BORDER+100,WIDTH-GAMEPLAY_BORDER-100),random.randrange(400,HEIGHT-100))
            bomb5=Bomb(random.randrange(GAMEPLAY_BORDER+100,WIDTH-GAMEPLAY_BORDER-100),random.randrange(400,HEIGHT-100))
            bomb6=Bomb(random.randrange(GAMEPLAY_BORDER+100,WIDTH-GAMEPLAY_BORDER-100),random.randrange(400,HEIGHT-100))
            bomb7=Bomb(random.randrange(GAMEPLAY_BORDER+100,WIDTH-GAMEPLAY_BORDER-100),random.randrange(400,HEIGHT-100))
            bomb8=Bomb(random.randrange(GAMEPLAY_BORDER+100,WIDTH-GAMEPLAY_BORDER-100),random.randrange(400,HEIGHT-100))
            bombs.append(bomb)
            bombs.append(bomb2)
            bombs.append(bomb3)
            bombs.append(bomb4)
            bombs.append(bomb5)
            bombs.append(bomb6)
            bombs.append(bomb7)
            bombs.append(bomb8)
            pygame.mixer.Sound.play(BOSS_BOMB)
            self.attack_pattern=-1
            self.attack_dur+100

        
        elif self.attack_pattern==3:
            self.charge=True;
            self.idle=False
            pygame.mixer.Sound.play(BOSS_CHARGE)
            self.attack_pattern=-1



        self.attack_dur+=1
        if self.attack_dur>=240:
            self.attack_dur=0
            self.attack_pattern=random.randrange(0,4)

        

   
    def collision(self, obj):
        return collide(self, obj)       
            
    def draw(self, window):
        super().draw(window)
        self.healthbar(window)
            
    def healthbar(self, window):
        pygame.draw.rect(window, (255,0,0), (WIDTH/2-GAMEPLAY_SITE/2, 20, GAMEPLAY_SITE, 50))
        pygame.draw.rect(window, (0,255,0), (WIDTH/2-GAMEPLAY_SITE/2, 20, GAMEPLAY_SITE* (self.health/self.max_health), 50))
    
    def return_value(self):
        return self.value    

class Enemy_Charge(Ship):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.ship_img=ENEMY_SHIP_CHARGE
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.value=150
        self.idle = True
        self.on_board= False
        self.health=100
        self.direction = random.randrange(1,11)
        
        if self.x>WIDTH/2:
            self.x=random.randrange(0,GAMEPLAY_BORDER)
        else:
            self.x=random.randrange(WIDTH-GAMEPLAY_BORDER,WIDTH)

    def move(self, vel,obj):
        if obj.x<self.x<obj.x+10:
            self.idle=False
            self.ship_img=ENEMY_SHIP_CHARGE_ANGRY

        if self.idle==False:
            self.y+=vel*5
            if  not obj.x-150<self.x<obj.x+150:
                self.idle=True
                self.ship_img=ENEMY_SHIP_CHARGE
        else:
            if self.x<GAMEPLAY_BORDER:
                self.direction=6
            elif self.x>WIDTH-GAMEPLAY_BORDER-100:
                self.direction=1

            if self.direction>5:
                self.x+=vel
            else:
                self.x-=vel

    def return_value(self):
        return self.value

class Enemy_Spread(Ship):

    COOLDOWN = 160

    def __init__(self, x, y ):
        super().__init__(x, y)
        self.ship_img=ENEMY_SHIP_SHOTGUN
        self.bullet_img =ENEMY_BULLET_2
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.value=100
        self.health=100

    def move(self, vel):
        self.y += vel

    def shoot(self,objs):
        if self.cooldown_counter==0:
            bullet = Bullet(self.x+37, self.y+50, self.bullet_img)
            bulletsrs = Bullet_SRS(self.x+37, self.y+50, self.bullet_img)
            bulletsls = Bullet_SLS(self.x+37, self.y+50, self.bullet_img)
            bulletsrl = Bullet_SRL(self.x+37, self.y+50, self.bullet_img)
            bulletsll = Bullet_SLL(self.x+37, self.y+50, self.bullet_img)
            objs.append(bullet)
            objs.append(bulletsrs)
            objs.append(bulletsls)
            objs.append(bulletsrl)
            objs.append(bulletsll)
            self.cooldown_counter=1
            


    
    def return_value(self):
        return self.value


def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (int(offset_x), int(offset_y)))

def ship_skin_showcase(x):
    if x==0:
        WINDOW.blit(PLAYER_SHIP,(WIDTH/2-SKIN_SHOW/2,HEIGHT/2-SKIN_SHOW_POS))
    elif x==1:
        WINDOW.blit(PLAYER_SHIP_BLUE,(WIDTH/2-SKIN_SHOW/2,HEIGHT/2-SKIN_SHOW_POS))
    elif x==2:
        WINDOW.blit(PLAYER_SHIP_WHITE,(WIDTH/2-SKIN_SHOW/2,HEIGHT/2-SKIN_SHOW_POS))
    elif x==3:
        WINDOW.blit(PLAYER_SHIP_YELLOW,(WIDTH/2-SKIN_SHOW/2,HEIGHT/2-SKIN_SHOW_POS))


def main():
    run = True
    FPS = 60
    level = 0
    lives = 3 
    main_menu = True 
    options=False
    options_skins=False
    ending_screen=False
    records=False
    victory=False
    ship_option=0

    levels = []
    strint = 0
    strint2 = 0
    string3 = 0
    with open("levels.txt") as level_list:
        levels = [line.split() for line in level_list]

    global ex_count
    ex_count=0
    global lazy_timer
    lazy_timer=0
    global multiplier
    multiplier=1

    all_bullets=[]
    explosions=[]
    all_bombs=[]

    main_font = pygame.font.SysFont("agency_fb", 80)
    second_font = pygame.font.SysFont("agency_fb", 120)
    third_font = pygame.font.SysFont("agency_fb", 70)
    record_font = pygame.font.SysFont("agency_fb", 100)

    player = Player(WIDTH/2-45,650,ship_option)

    enemies = []
    enemies_charge = []
    

    wave_length = 1
    enemy_vel = 3
    bullet_vel = 5

    player_vel=7

    lost = False
    lost_count = 0

    start_button=Button(WIDTH/2-315 , HEIGHT/2+200, START_BUTTON)
    option_button=Button(WIDTH/2+25 , HEIGHT/2+200, OPTIONS_BUTTON)
    records_button=Button(WIDTH/2-315 , HEIGHT/2+300, RECORDS_BUTTON)
    exit_button=Button(WIDTH/2+25 , HEIGHT/2+300, EXIT_BUTTON)
    arrow_l=Button(WIDTH/2-250 , HEIGHT/2+250, ARROW_LEFT)
    arrow_r=Button(WIDTH/2+50 , HEIGHT/2+250, ARROW_RIGHT)
    back_button=Button(0,0, BACK_BUTTON)

    clock = pygame.time.Clock()
    def redraw_w():
        global ex_count
        global lazy_timer
        global multiplier
        WINDOW.blit(BACKGROUND, (0,0))
        if ex_count >= 119:
            ex_count=0;
        ex_count+=1

        for bullet in all_bullets:
            bullet.draw(WINDOW)
        for enemy in enemies:
            enemy.draw(WINDOW)

        for enemy_charge in enemies_charge:
            enemy_charge.draw(WINDOW)
        for explosion in explosions:
            if explosion.return_lifespan()>49:
                explosions.remove(explosion)
            else:
                explosion.anim()

        if lazy_timer>60 and level!=3:
            player.points-=10
            lazy_timer=0
        else:
            lazy_timer+=1

        for bomb in all_bombs:
            bomb.draw()
            if bomb.return_lifespan()>100:
                if bomb.collision(player):
                    player.get_hit(1)                 
            if bomb.return_lifespan()>151:
                all_bombs.remove(bomb)


        
        score_label = main_font.render(f"{int(player.get_points())}", 1, (255,174,0))
        combo = main_font.render(f"x{multiplier}", 1, (255,174,0))
        level_label = main_font.render(f"{level}", 1, (255,174,0))
        WINDOW.blit(OVERLAY, (0,0))


        
        
        WINDOW.blit(score_label, (WIDTH-250-score_label.get_rect().width/2,250))
        WINDOW.blit(combo, (WIDTH-250-combo.get_rect().width/2,350))
        WINDOW.blit(level_label, (380,280))

        player.anim(ex_count,ship_option)
        player.draw(WINDOW)

        WINDOW.blit(HP_BORDER,(HP_POS_X,HP_POS_Y))
        pygame.display.update()

    def off():
        global multiplier
        player.health -= 5
        player.flawless=False
        multiplier=1
        player.border_pass()

    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(-1)

    while run:
        clock.tick(FPS)
        keys=pygame.key.get_pressed()
        if main_menu == True:
            #MAIN MENU LOOP
            if options==True:
                WINDOW.blit(SKIN_CHANGE_BACKGROUND,(0,0))
                if back_button.draw():
                    main_menu=True
                    options=False
                if arrow_l.draw() and ship_option>0:
                    ship_option-=1
                    
                if arrow_r.draw()and ship_option<3:
                    ship_option+=1
                   
                
                ship_skin_showcase(ship_option)
                player = Player(WIDTH/2-45,650,ship_option)
            elif records==True:
                WINDOW.blit(TABLE_OF_RECORDS_BACKGROUND,(0,0))
                if back_button.draw():
                    records=False

            else:
                WINDOW.blit(STARTING_BACKGROUND,(0,0))
                if start_button.draw():
                    main_menu=False
                    pygame.mixer.music.unload
                    pygame.mixer.music.load("assets/bg_song_2.ogg")
                    pygame.mixer.music.play(-1)
                    pygame.mouse.set_visible(False)
                if option_button.draw():
                    options=True
                if records_button.draw():
                    records=True
                if exit_button.draw():
                    run = False
            

            pygame.display.update()
            
        elif ending_screen==True:
            pygame.mouse.set_visible(True)
            
                    
            if lost==True:
                WINDOW.blit(GAME_OVER,(0,0))
                score_label = second_font.render(f"{int(player.get_points())}", 1, (255,21,0))
                restart=third_font.render("Press R to restart", 1, (255,21,0))
                               
            else:
                WINDOW.blit(VICTORY,(0,0))
                score_label = second_font.render(f"{int(player.get_points())}", 1, (0,234,255))
                restart=third_font.render("Press R to restart", 1, (0,234,255))
                
               
              
            WINDOW.blit(score_label, (WIDTH/2-score_label.get_rect().width/2,450))
            WINDOW.blit(restart, (WIDTH/2-restart.get_rect().width/2,650))
            pygame.display.update()
            if keys[pygame.K_e]:
                run=False
            if keys[pygame.K_r]:
                player = Player(WIDTH/2-45,650,ship_option)
                player.health=100
                enemies = []
                enemies_charge = []
                bullets=[]
                main_menu=True
                lost=False
                level=0
                lost_count=0
                player.points=0
                ending_screen=False
                pygame.mixer.music.unload
                pygame.mixer.music.load("assets/bg_song.ogg")
                pygame.mixer.music.play(-1)
                multiplier=1
                
            

        else:
            redraw_w()
            if player.health <= 0:
                lost = True
                lost_count += 1
                ending_screen = True
                pygame.mixer.music.unload
                pygame.mixer.music.load("assets/lost_theme.mp3")
                pygame.mixer.music.play(-1)
            if level==3 and len(enemies)+len(enemies_charge) == 0:
                ending_screen=True
                player.points+=2000*multiplier
                pygame.mixer.music.unload
                pygame.mixer.music.load("assets/win_theme.mp3")
                pygame.mixer.music.play(-1)

            if ending_screen == True:
                for enemy_charge in enemies_charge[:]:
                    enemies_charge.remove(enemy_charge)
                for enemy in enemies[:]:
                    enemies.remove(enemy)
                for bullet in all_bullets[:]:
                    all_bullets.remove(bullet)
                for explosion in explosions[:]:
                    explosions.remove(explosion)
                

            elif len(enemies)+len(enemies_charge) == 0:
                level += 1
                level_version = random.randrange(0,2)          
                level_nr = (level-1)*6+level_version*3
                for i in range(len(levels[level_nr])):
                    strint = int(levels[level_nr][i])
                    if strint==1:
                        strint2 = int(levels[level_nr+2][i])
                        strint3 = int(levels[level_nr+1][i])
                        enemy = Enemy(strint2,strint3)
                        enemies.append(enemy)
                    elif strint==2:
                        strint2 = int(levels[level_nr+2][i])
                        strint3 = int(levels[level_nr+1][i])
                        enemy_charge = Enemy_Charge(strint2,strint3)
                        enemies_charge.append(enemy_charge)
                    elif strint==3:
                        strint2 = int(levels[level_nr+2][i])
                        strint3 = int(levels[level_nr+1][i])
                        enemy = Enemy_Spread(strint2,strint3)
                        enemies.append(enemy)
                    elif strint==4:
                        strint2 = int(levels[level_nr+2][i])
                        strint3 = int(levels[level_nr+1][i])
                        enemy = Boss(strint2,strint3)
                        enemies.append(enemy)
                        pygame.mixer.music.unload
                        pygame.mixer.music.load("assets/boss_music.mp3")
                        pygame.mixer.music.play(-1)
  

            if keys[pygame.K_a] and player.x - player_vel > 520:
                player.x -= player_vel
            if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH-520:
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
                if level==3:
                    enemy.shoot(all_bullets,all_bombs)
                    if collide(enemy,player):
                       player.get_hit(3)
                else:
                    enemy.shoot(all_bullets)
                enemy.move(enemy_vel)
                enemy.cooldown()
                if enemy.health<=0:
                   enemies.remove(enemy)
                if enemy.y + enemy.get_height() > HEIGHT and level!=3:
                    enemies.remove(enemy)
                    off()

            player.move_bullet(-10, enemies,explosions)
            player.move_bullet(0, enemies_charge,explosions)

            for enemy_charge in enemies_charge[:]:
                enemy_charge.move(enemy_vel,player)
                if enemy_charge.health<=0:
                    enemies_charge.remove(enemy_charge)
                if collide(enemy_charge,player):
                    player.get_hit(15)
                    enemies_charge.remove(enemy_charge)
                    
                if enemy_charge.y + enemy_charge.get_height() > HEIGHT:
                    enemies_charge.remove(enemy_charge)
                    off()

            for bullet in all_bullets[:]:
                bullet.move(bullet_vel)
                if bullet.off_screen(HEIGHT):
                    all_bullets.remove(bullet)
                elif bullet.collision(player):
                    player.get_hit(10)
                    all_bullets.remove(bullet)
                        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            
main()




