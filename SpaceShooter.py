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

#enemy data
ENEMY_SHIP=pygame.transform.scale(pygame.image.load(os.path.join("assets", "przeciwnik.png")).convert_alpha(),(75,75))
ENEMY_SHIP_CHARGE=pygame.transform.scale(pygame.image.load(os.path.join("assets", "enemy_charge.png")).convert_alpha(),(75,75))
ENEMY_SHIP_CHARGE_ANGRY=pygame.transform.scale(pygame.image.load(os.path.join("assets", "enemy_charge_angry.png")).convert_alpha(),(75,75))
ENEMY_SHIP_SHOTGUN=pygame.transform.scale(pygame.image.load(os.path.join("assets", "enemy_shotgun.png")).convert_alpha(),(75,40))

ENEMY_BULLET=pygame.transform.scale(pygame.image.load(os.path.join("assets", "pocisk.png")).convert_alpha(),(8,8))
ENEMY_BULLET_2=pygame.transform.scale(pygame.image.load(os.path.join("assets", "bullet2.png")).convert_alpha(),(10,10))


#player data
PLAYER_SHIP=pygame.transform.scale(pygame.image.load(os.path.join("assets", "stateczek.png")).convert_alpha(),(75,75))
PLAYER_SHIP_WHITE=pygame.transform.scale(pygame.image.load(os.path.join("assets", "stateczek_white.png")).convert_alpha(),(75,75))
PLAYER_SHIP_BLUE=pygame.transform.scale(pygame.image.load(os.path.join("assets", "stateczek_blue.png")).convert_alpha(),(75,75))
PLAYER_SHIP_YELLOW=pygame.transform.scale(pygame.image.load(os.path.join("assets", "stateczek_yellow.png")).convert_alpha(),(75,75))

PLAYER_BULLET=pygame.transform.scale(pygame.image.load(os.path.join("assets", "pocisk.png")),(8,8))

#buttons
#START_BUTTON=pygame.transform.scale(pygame.image.load(os.path.join("assets", "start_button.png")).convert_alpha(),(300,100))
#OPTIONS_BUTTON=pygame.transform.scale(pygame.image.load(os.path.join("assets", "options_button.png")).convert_alpha(),(300,100))
#RECORDS_BUTTON=pygame.transform.scale(pygame.image.load(os.path.join("assets", "records_button.png")).convert_alpha(),(300,100))
#EXIT_BUTTON=pygame.transform.scale(pygame.image.load(os.path.join("assets", "exit_button.png")).convert_alpha(),(300,100))
#ARROW_LEFT=pygame.transform.scale(pygame.image.load(os.path.join("assets", "arrow_left.png")).convert_alpha(),(200,200))
#ARROW_RIGHT=pygame.transform.scale(pygame.image.load(os.path.join("assets", "arrow_right.png")).convert_alpha(),(200,200))
#SKIN_CHANGE_BUTTON=pygame.transform.scale(pygame.image.load(os.path.join("assets", "skin_change_button.png")).convert_alpha(),(300,100))
#BACK_BUTTON=pygame.transform.scale(pygame.image.load(os.path.join("assets", "back_button.png")).convert_alpha(),(200,200))

#animations
EXPLOSION=[pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/explosion", "e1.png")).convert_alpha(),(75,75)),
           pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/explosion", "e2.png")).convert_alpha(),(75,75)),
           pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/explosion", "e3.png")).convert_alpha(),(75,75))]

SHIP1=[pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/1podstawowy", "statek1a.png")).convert_alpha(),(75,75)),
       pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/1podstawowy", "statek1b.png")).convert_alpha(),(75,75)),
       pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/1podstawowy", "statek1c.png")).convert_alpha(),(75,75)),
       pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/1podstawowy", "statek1d.png")).convert_alpha(),(75,75)),
       pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/1podstawowy", "statek1c.png")).convert_alpha(),(75,75)),
       pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/1podstawowy", "statek1b.png")).convert_alpha(),(75,75))]

SHIP2=[pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/2niebieski", "statek2a.png")).convert_alpha(),(75,75)),
       pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/2niebieski", "statek2b.png")).convert_alpha(),(75,75)),
       pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/2niebieski", "statek2c.png")).convert_alpha(),(75,75)),
       pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/2niebieski", "statek2d.png")).convert_alpha(),(75,75)),
       pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/2niebieski", "statek2c.png")).convert_alpha(),(75,75)),
       pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/2niebieski", "statek2b.png")).convert_alpha(),(75,75))]

SHIP3=[pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/3zielony", "statek4a.png")).convert_alpha(),(75,75)),
       pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/3zielony", "statek4b.png")).convert_alpha(),(75,75)),
       pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/3zielony", "statek4c.png")).convert_alpha(),(75,75)),
       pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/3zielony", "statek4d.png")).convert_alpha(),(75,75)),
       pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/3zielony", "statek4c.png")).convert_alpha(),(75,75)),
       pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/3zielony", "statek4b.png")).convert_alpha(),(75,75))]

SHIP4=[pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/4zolty", "statek3a.png")).convert_alpha(),(75,75)),
       pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/4zolty", "statek3b.png")).convert_alpha(),(75,75)),
       pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/4zolty", "statek3c.png")).convert_alpha(),(75,75)),
       pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/4zolty", "statek3d.png")).convert_alpha(),(75,75)),
       pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/4zolty", "statek3c.png")).convert_alpha(),(75,75)),
       pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/ship/4zolty", "statek3b.png")).convert_alpha(),(75,75))]

#button animations
START_BUTTON=[pygame.transform.scale(pygame.image.load(os.path.join("assets", "start_button.png")).convert_alpha(),(300,100)),
              pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/buttons", "start_button1.png")).convert_alpha(),(300,100))]

OPTIONS_BUTTON=[pygame.transform.scale(pygame.image.load(os.path.join("assets", "options_button.png")).convert_alpha(),(300,100)),
                pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/buttons", "options_button1.png")).convert_alpha(),(300,100))]

RECORDS_BUTTON=[pygame.transform.scale(pygame.image.load(os.path.join("assets", "records_button.png")).convert_alpha(),(300,100)),
                pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/buttons", "records_button1.png")).convert_alpha(),(300,100))]

EXIT_BUTTON=[pygame.transform.scale(pygame.image.load(os.path.join("assets", "exit_button.png")).convert_alpha(),(300,100)),
             pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/buttons", "exit_button1.png")).convert_alpha(),(300,100))]

ARROW_LEFT=[pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/buttons", "arrow_left.png")).convert_alpha(),(200,200)),
            pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/buttons", "arrow_left1.png")).convert_alpha(),(200,200))]

ARROW_RIGHT=[pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/buttons", "arrow_right.png")).convert_alpha(),(200,200)),
             pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/buttons", "arrow_right1.png")).convert_alpha(),(200,200))]

SKIN_CHANGE_BUTTON=[pygame.transform.scale(pygame.image.load(os.path.join("assets", "options_button.png")).convert_alpha(),(300,100)),
                    pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/buttons", "options_button1.png")).convert_alpha(),(300,100))]

BACK_BUTTON=[pygame.transform.scale(pygame.image.load(os.path.join("assets", "back_button.png")).convert_alpha(),(200,200)),
             pygame.transform.scale(pygame.image.load(os.path.join("assets/animations/buttons", "back_button1.png")).convert_alpha(),(200,200))]


#background
STARTING_BACKGROUND=pygame.transform.scale(pygame.image.load(os.path.join("assets", "menu.png")).convert(),(WIDTH,HEIGHT))
OPTIONS_BACKGROUND=pygame.transform.scale(pygame.image.load(os.path.join("assets", "options.png")).convert(),(WIDTH,HEIGHT))
SKIN_CHANGE_BACKGROUND=pygame.transform.scale(pygame.image.load(os.path.join("assets", "skin_change_background.png")).convert(),(WIDTH,HEIGHT))
BACKGROUND=pygame.transform.scale(pygame.image.load(os.path.join("assets", "kosmos1.png")).convert(),(WIDTH,HEIGHT))
OVERLAY=pygame.transform.scale(pygame.image.load(os.path.join("assets", "overlay.png")).convert_alpha(),(WIDTH,HEIGHT))
HP_BORDER=pygame.transform.scale(pygame.image.load(os.path.join("assets", "hp_border.png")).convert_alpha(),(300,50))
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
            bullet = Bullet(self.x + 45, self.y, self.bullet_img)
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

    def move_bullet(self, vel, objs):
        self.cooldown()
        for bullet in self.bullets:
            bullet.move(vel)
            if bullet.off_screen(HEIGHT):
                self.bullets.remove(bullet)
            else:
                for obj in objs:
                    if bullet.collision(obj):
                        pygame.mixer.Sound.play(ENEMY_HIT)
                        self.points+=obj.return_value()
                        objs.remove(obj)
                        
                        if bullet in self.bullets:
                            self.bullets.remove(bullet)

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
        pygame.draw.rect(window, (255,0,0), (100, 150, 300, 50))
        pygame.draw.rect(window, (0,255,0), (100, 150, 300* (self.health/self.max_health), 50))


class Enemy(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img=ENEMY_SHIP
        self.bullet_img =ENEMY_BULLET
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.value=100

    def move(self, vel):
        self.y += vel

    def shoot(self,objs):
        if self.cooldown_counter==0 and random.randrange(60)==1:
            bullet = Bullet(self.x+37, self.y+80, self.bullet_img)
            objs.append(bullet)
            self.cooldown_counter=1
            
    
    def return_value(self):
        return self.value
    
class Enemy_Charge(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img=ENEMY_SHIP_CHARGE
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.value=150
        self.idle = True
        self.on_board= False
        self.direction = random.randrange(1,11)
        
        if self.x>WIDTH/2:
            self.x=random.randrange(0,450)
        else:
            self.x=random.randrange(WIDTH-450,WIDTH)

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
            if self.x<450:
                self.direction=6
            elif self.x>WIDTH-550:
                self.direction=1

            if self.direction>5:
                self.x+=vel
            else:
                self.x-=vel

    def return_value(self):
        return self.value

class Enemy_Spread(Ship):

    COOLDOWN = 160

    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img=ENEMY_SHIP_SHOTGUN
        self.bullet_img =ENEMY_BULLET_2
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.value=100

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
        WINDOW.blit(pygame.transform.scale(PLAYER_SHIP,(350,350)),(WIDTH/2-175,HEIGHT/2-250))
    elif x==1:
        WINDOW.blit(pygame.transform.scale(PLAYER_SHIP_BLUE,(350,350)),(WIDTH/2-175,HEIGHT/2-250))
    elif x==2:
        WINDOW.blit(pygame.transform.scale(PLAYER_SHIP_WHITE,(350,350)),(WIDTH/2-175,HEIGHT/2-250))
    elif x==3:
        WINDOW.blit(pygame.transform.scale(PLAYER_SHIP_YELLOW,(350,350)),(WIDTH/2-175,HEIGHT/2-250))


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
    global ex_count
    ex_count=0
    all_bullets=[]

    main_font = pygame.font.SysFont("agency_fb", 80)
    second_font = pygame.font.SysFont("agency_fb", 120)
    record_font = pygame.font.SysFont("agency_fb", 100)

    spawn_rate=[[5,5,5,5,5],[1,1,1,1,1],[3,3,3,3,3]]
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
        
        score_label = main_font.render(f"{player.get_points()}", 1, (255,174,0))
        level_label = main_font.render(f"{level}", 1, (255,174,0))
        WINDOW.blit(OVERLAY, (0,0))


        
        
        WINDOW.blit(score_label, (WIDTH-250-score_label.get_rect().width/2,250))
        WINDOW.blit(level_label, (380,280))

        player.anim(ex_count,ship_option)
        player.draw(WINDOW)

        WINDOW.blit(HP_BORDER,(100,150))
        pygame.display.update()

    def off():
        player.health -= 5
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
                WINDOW.blit(BACKGROUND,(0,0))
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
                score_label = second_font.render(f"{player.get_points()}", 1, (255,21,0))
                
                               
            else:
                WINDOW.blit(VICTORY,(0,0))
                score_label = second_font.render(f"{player.get_points()}", 1, (0,234,255))
                
               
              
            WINDOW.blit(score_label, (WIDTH/2-score_label.get_rect().width/2,450))
            pygame.display.update()
            if keys[pygame.K_e]:
                run=False
            if keys[pygame.K_r]:
                player = Player(WIDTH/2-45,650,ship_option)
                player.health=100
                enemies = []
                enemies_charge = []
                main_menu=True
                lost=False
                level=0
                lives=3
                lost_count=0
                player.points=0
                ending_screen=False
                pygame.mixer.music.unload
                pygame.mixer.music.load("assets/bg_song.ogg")
                pygame.mixer.music.play(-1)
                
            

        else:
            redraw_w()
            if player.health <= 0:
                lost = True
                lost_count += 1
                ending_screen = True
                pygame.mixer.music.unload
                pygame.mixer.music.load("assets/lost_theme.mp3")
                pygame.mixer.music.play(-1)
            if level==3:
                ending_screen=True
                pygame.mixer.music.unload
                pygame.mixer.music.load("assets/win_theme.mp3")
                pygame.mixer.music.play(-1)

            if ending_screen == True:
                for enemy_charge in enemies_charge[:]:
                    enemies_charge.remove(enemy_charge)
                    print("usuwam charge")
                for enemy in enemies[:]:
                    enemies.remove(enemy)
                    print("usuwam zwykły")
                for bullet in all_bullets[:]:
                    all_bullets.remove(bullet)
                    print("suswam bullet")
                

            if len(enemies)+len(enemies_charge) == 0 and ending_screen == False:
                level += 1
                for i in range(spawn_rate[0][level-1]):
                    enemy = Enemy(random.randrange(600, WIDTH-600), random.randrange(-1500, -100))
                    enemies.append(enemy)
                for x in range(spawn_rate[1][level-1]):
                    enemy_charge = Enemy_Charge(random.randrange(500, WIDTH-500), random.randrange(-20,200))
                    enemies_charge.append(enemy_charge)
                for i in range(spawn_rate[2][level-1]):
                    enemy = Enemy_Spread(random.randrange(600, WIDTH-600), random.randrange(-1500, -100))
                    enemies.append(enemy)
  

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
                enemy.shoot(all_bullets)
                enemy.cooldown()
                enemy.move(enemy_vel)
                if enemy.y + enemy.get_height() > HEIGHT:
                    enemies.remove(enemy)
                    off()



            for enemy_charge in enemies_charge[:]:
                enemy_charge.move(enemy_vel,player)
                if collide(enemy_charge,player):
                    enemies_charge.remove(enemy_charge)
                    player.health-=15      
                if enemy_charge.y + enemy_charge.get_height() > HEIGHT:
                    enemies_charge.remove(enemy_charge)
                    off()

            for bullet in all_bullets[:]:
                bullet.move(bullet_vel)
                if bullet.off_screen(HEIGHT):
                    all_bullets.remove(bullet)
                elif bullet.collision(player):
                    player.health -= 10
                    all_bullets.remove(bullet)
                
        
        
        
        
        player.move_bullet(-10, enemies)
        player.move_bullet(0, enemies_charge)# to juz nie jest main game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            
main()




