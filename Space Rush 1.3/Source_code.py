from cmath import rect
from pygame import mixer
import json
import pygame
import random
import time

# intialize the pygame
pygame.init()

# intialize the mixer
pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()

# title and stuff
pygame.display.set_caption('Space Rush by @itsswaggy')
icon = pygame.image.load('Spaceship2.png')
pygame.display.set_icon(icon)

# create window
screen = pygame.display.set_mode((800, 600))

# load the sounds
laser_fx = pygame.mixer.Sound("lazer.wav")
laser_fx.set_volume(0.55)

ex = pygame.mixer.Sound("explosion.wav")
ex.set_volume(0.60)

# background music
bgmusic = pygame.mixer.Sound("bgmusic.wav")
bgmusic.play(-1)
bgmusic.set_volume(0.75)

# load shop icons
val1 = pygame.image.load('Spaceship1.png')
val2 = pygame.image.load('Spaceship2.png')
val3 = pygame.image.load('Spaceship3.png')

val_check = 2

# money system
coin_timer = 0
money = 0


# define sounds are muted
bgmusic_mute = False
sfx = False

# score and stuff
shine = 0
score = -1
highscore = 0
font = pygame.font.Font('Bubblegum.ttf', 22)
font1 = pygame.font.Font('Bubblegum.ttf', 16)
font2 = pygame.font.Font('Bubblegum.ttf', 48)
fontE = pygame.font.Font('Bubblegum.ttf', 12)

def show_score():
    score_value = font.render('Score: ' + str(score), True, (255,255,255))
    screen.blit(score_value, (345, 20))

def high_score():
    highscore_value = font.render('Highscore: ' + str(highscore), True, (255,255,255))
    screen.blit(highscore_value, (323, 40))

def show_money():
    money_value = font1.render('Money: ' + str(money), True, (255,255,255))
    screen.blit(money_value, (708, 30))

def esc_to():
    esc_to_ = font1.render('ESC to pause', True, (255,255,255))
    screen.blit(esc_to_, (688, 10))

with open('virus.txt') as highscore_file:
    highscore = json.load(highscore_file)

with open('virus2.txt') as money_file:
    money = json.load(money_file)

# press q to quit
def q_to_quit():
    q_to = font1.render('Press Q to quit.', True, (255,255,255))
    screen.blit(q_to, (10, 10))

# baground
bg = pygame.image.load('bg.png')

# Shop info
alien_Ufo_info = False
hightech_Ufo_info = False
original_Ufo_info = False

# spaceship
playerImg = val2
hitbox = playerImg.get_rect()
vel = 2
hitbox.y = 268

# small asteroid
asteroid_smallImg = pygame.image.load('asteroid.png')
hitbox_ = asteroid_smallImg.get_rect()
vel_ = 1

# check if the player can restart
check = False
# check if main menu = true
mainmenu = False
# check if pausescreen = true
pausescreen = False
# check if shop is open
shop = False

# coin
coinImg = pygame.image.load('dollar.png')
coin_hit = coinImg.get_rect()
coin_hit.x = random.randint(1,200)
coin_hit.y = random.randint(1,550)

# aliens
alienImg = pygame.image.load('Invader.png')
hitbox___ = alienImg.get_rect()
vel___ = 1
hitbox___.x = 530

alien_Img = pygame.image.load('Invader.png')
alien_hitbox = alien_Img.get_rect()
speed___ = 1
alien_hitbox.x = 630

# big asteroid
big_asteroidImg = pygame.image.load('Big_asteroid.png')
hitbox__ = big_asteroidImg.get_rect()
vel__ = 0.5
hitbox__.y = -150

# bullets
bulletImg = pygame.image.load('laser.png')
bullet_hitbox = bulletImg.get_rect()
speed_ = 2
bullet_hitbox.x = -50
bullet_hitbox.y = 0

bullet_Img = pygame.image.load('laser.png')
bullet__hitbox = bullet_Img.get_rect()
speed__ = 2
bullet__hitbox.x = -50
bullet__hitbox.y = 0

player_bullet = pygame.image.load('laser.png')
pbullet_hitbox = player_bullet.get_rect()
pbullet_speed = 3
pbullet_hitbox.x = 2000

# point
pointImg = pygame.image.load('asteroid.png')
point = pointImg.get_rect()
point_speed = 4
point.y

# blue scoreboard
bluebg = pygame.image.load('spacebg.png')

# load skin
with open('virus3.txt') as skin_file:
    val_check = json.load(skin_file)

# if player has the skin
with open('virus4.txt') as skin1_file:
    lol1 = json.load(skin1_file)

with open('virus5.txt') as skin2_file:
    lol2 = json.load(skin2_file)

running = True
while running:

        # RGB
        screen.fill((149, 27, 218))
        # bagground
        screen.blit(bg, (0,0))

        # define quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open('virus.txt', 'w') as highscore_file:
                    json.dump(highscore,highscore_file)
                with open('virus2.txt', 'w') as money_file:
                    json.dump(money,money_file)
                with open('virus3.txt', 'w') as skin_file:
                    json.dump(val_check,skin_file)
                with open('virus4.txt', 'w') as skin1_file:
                    json.dump(lol1,skin1_file)
                with open('virus5.txt', 'w') as skin2_file:
                    json.dump(lol2,skin2_file)
                running = False

        # keyboard input
        userInput = pygame.key.get_pressed()
        if userInput[pygame.K_RIGHT]:
            hitbox.x += vel
        if userInput[pygame.K_LEFT]:
            hitbox.x -= vel
        if userInput[pygame.K_UP]:
            hitbox.y -= vel
        if userInput[pygame.K_DOWN]:
            hitbox.y += vel
        if userInput[pygame.K_d]:
            hitbox.x += vel
        if userInput[pygame.K_a]:
            hitbox.x -= vel
        if userInput[pygame.K_w]:
            hitbox.y -= vel
        if userInput[pygame.K_s]:
            hitbox.y += vel
        if userInput[pygame.K_SPACE] and pbullet_hitbox.x > 2000:
            pbullet_hitbox.x = hitbox.x
            pbullet_hitbox.y = hitbox.y
            laser_fx.play()
        if userInput[pygame.K_ESCAPE] and check == True:
            hitbox.x = 0
            hitbox.y = 268
            hitbox__.x = 0
            hitbox__.y = -150
            bullet_hitbox.x = -70
            bullet__hitbox.x = -70
            hitbox_.x = 736
            hitbox_.y = 150
            score = 1
            speed_ = 2
            speed__ = 2
            speed___ = 1.5
            vel = 2
            vel_ = 1
            vel__ = 0.5
            vel___ = 1
            point_speed = 4
            pbullet_speed = 3
            shine = 1
            check = False
        if userInput[pygame.K_h] and score == 0 and mainmenu == True:
            hitbox.x = 0
            hitbox.y = 268
            hitbox__.x = 0
            hitbox__.y = -150
            bullet_hitbox.x = -70
            bullet__hitbox.x = -70
            hitbox_.x = 736
            hitbox_.y = 150
            score += 1
            speed_ = 2
            speed__ = 2
            speed___ = 1.5
            vel = 2
            vel_ = 1
            vel__ = 0.5
            vel___ = 1
            point_speed = 4
            pbullet_speed = 3
            mainmenu = False
        if userInput[pygame.K_ESCAPE] and score >= 3 and mainmenu == False and check == False:
            pausescreen = True
        if userInput[pygame.K_e] and pausescreen == True and mainmenu == False and check == False:
            pausescreen = False
            score += 1
            speed_ = 2
            speed__ = 2
            speed___ = 1.5
            vel = 2
            vel_ = 1
            vel__ = 0.5
            vel___ = 1
            point_speed = 4
            pbullet_speed = 3
        if userInput[pygame.K_f] and mainmenu == True:
            shop = True
        if userInput[pygame.K_f] and check == True:
            shop = True
        if userInput[pygame.K_g] and shop == True:
            shop = False
        if userInput[pygame.K_1] and lol1 == 0 and shop == True and money >= 30:
            money -= 30
            lol1 = 1
            val_check = 1
        if userInput[pygame.K_3] and lol2 == 0 and shop == True and money >= 10:
            money -= 10
            lol2 = 1
            val_check = 3
        if userInput[pygame.K_3] and lol2 == 1 and shop == True:
            val_check = 3
        if userInput[pygame.K_1] and lol1 == 1 and shop == True:
            val_check = 1
        if userInput[pygame.K_2] and shop == True:
            val_check = 2
        if userInput[pygame.K_u] and shop == True and original_Ufo_info == False:
            original_Ufo_info = True
        if userInput[pygame.K_i] and shop == True:
            original_Ufo_info = False
        if userInput[pygame.K_n] and shop == True and hightech_Ufo_info == False:
            hightech_Ufo_info = True
        if userInput[pygame.K_m] and hightech_Ufo_info == True:
            hightech_Ufo_info = False
        if userInput[pygame.K_j] and shop == True and alien_Ufo_info == False:
            alien_Ufo_info = True
        if userInput[pygame.K_k] and alien_Ufo_info == True:
            alien_Ufo_info = False
        if userInput[pygame.K_v]:
            bgmusic.set_volume(0)
            bgmusic_mute = True
        if userInput[pygame.K_b]:
            bgmusic.set_volume(0.75)
            bgmusic_mute = False
        if userInput[pygame.K_z]:
            laser_fx.set_volume(0)
            ex.set_volume(0)
            sfx = True
        if userInput[pygame.K_x]:
            laser_fx.set_volume(0.55)
            ex.set_volume(0.60)
            sfx = False
        if userInput[pygame.K_q]:
            with open('virus.txt', 'w') as highscore_file:
                json.dump(highscore,highscore_file)
            with open('virus2.txt', 'w') as money_file:
                json.dump(money,money_file)
            with open('virus3.txt', 'w') as skin_file:
                json.dump(val_check,skin_file)
            with open('virus4.txt', 'w') as skin1_file:
                json.dump(lol1,skin1_file)
            with open('virus5.txt', 'w') as skin2_file:
                json.dump(lol2,skin2_file)
            pygame.quit()

        # movement
        if hitbox_.x >= 0:
            hitbox_.x -= vel_
        
        if hitbox__.x >= 0:
            hitbox__.x -= vel__

        if score == 10:
            hitbox__.y = 112

        if hitbox___.y <= 600:
            hitbox___.y += vel___

        if alien_hitbox.y <= 600:
            alien_hitbox.y += speed___

        if bullet_hitbox.x > -70:
            bullet_hitbox.x -= speed_

        if bullet__hitbox.x > -70:
            bullet__hitbox.x -= speed__

        # point clock
        if point.x > 0:
            point.x -= point_speed
        
        if point.x <= 5:
            point.x = 736
            shine += 1
            score += 1
            coin_timer += 1

        if score > highscore:
            highscore += 1
        
        # speed boost
        if playerImg == val1:
            vel = 3

        # player bounderies
        if hitbox.y <= 0:
            hitbox.y = 0
        elif hitbox.y >= 536:
            hitbox.y = 536
            
        if hitbox.x <= 0:
            hitbox.x = 0
        elif hitbox.x >= 736:
            hitbox.x = 736

        # if the asteroid hits the left side, tp back
        if hitbox_.x <= 1:
            hitbox_.x = 736
            hitbox_.y = random.randint(1,536)
            vel_ += 0.05
        
        if score > 9 and hitbox__.x <= 0:
            hitbox__.x = 672
            hitbox__.y = random.randint(1,472)
            vel__ += 0.05
        
        if bullet_hitbox.x < 0 and shine > 20 and hitbox___.y == hitbox.y:
            bullet_hitbox.y = hitbox.y
            bullet_hitbox.x = alien_hitbox.x
            laser_fx.play()
        
        if bullet_hitbox.x < 0 and shine > 20 and hitbox___.y == hitbox.y:
            bullet_hitbox.y = hitbox.y
            bullet_hitbox.x = hitbox___.x
            laser_fx.play()

        if bullet__hitbox.x < 0 and shine > 35 and alien_hitbox.y == hitbox.y:
            bullet__hitbox.y = hitbox.y
            bullet__hitbox.x = alien_hitbox.x
            laser_fx.play()
        
        if bullet__hitbox.x < 0 and shine > 35 and alien_hitbox.y == hitbox.y:
            bullet__hitbox.y = hitbox.y
            bullet__hitbox.x = alien_hitbox.x
            laser_fx.play()

        if hitbox___.y >= 572:
            vel___ *= -1
        
        if hitbox___.y <= 0:
            vel___ *= -1
        
        if alien_hitbox.y >= 572:
            speed___ *= -1
        
        if alien_hitbox.y <= 0:
            speed___ *= -1
        
        if coin_timer > 10 and check == False and mainmenu == False and shop == False and pausescreen == False:
            screen.blit(coinImg, coin_hit)

        if coin_timer > 10 and hitbox.colliderect(coin_hit):
            money += 1
            coin_timer = 0
            coin_hit.x = random.randint(1,200)
            coin_hit.y = random.randint(1,568)
            if playerImg == val1:
                money += 1
            if playerImg == val3:
                money += 1
            
        if shine >= 20:
            screen.blit(alienImg, hitbox___)

        if shine >= 35:
            screen.blit(alien_Img, alien_hitbox)

        screen.blit(playerImg, hitbox)
        screen.blit(asteroid_smallImg, hitbox_)
        screen.blit(big_asteroidImg, hitbox__)
        screen.blit(bulletImg, bullet_hitbox)
        screen.blit(bullet_Img, bullet__hitbox)
        screen.blit(player_bullet, pbullet_hitbox)

        # define if the hitboxes hit eachother
        if hitbox.colliderect(hitbox_):
            speed_ = 0
            speed__ = 0
            speed___ = 0
            vel = 0
            vel_ = 0
            vel__ = 0
            vel___ = 0
            point_speed = 0
            pbullet_speed = 0
            check = True
            coin_timer = 0
            coin_hit.x = random.randint(1,200)
            coin_hit.y = random.randint(1,568)
            pbullet_hitbox.x = 2000

            screen.blit(bluebg, (0,0))

            def shop_font():
                shop_pen = font2.render('Press F for shop', True, (255,255,255))
                screen.blit(shop_pen, (190, 320))

            shop_font()

            def restart():
                q_to = font2.render('Press ESC to restart', True, (255,255,255))
                screen.blit(q_to, (145, 220))

            restart()

        if hitbox.colliderect(hitbox__):
            speed_ = 0
            speed__ = 0
            speed___ = 0
            vel = 0
            vel_ = 0
            vel__ = 0
            vel___ = 0
            point_speed = 0
            pbullet_speed = 0
            check = True
            coin_timer = 0
            coin_hit.x = random.randint(1,200)
            coin_hit.y = random.randint(1,568)
            pbullet_hitbox.x = 2000

            screen.blit(bluebg, (0,0))

            def shop_font():
                shop_pen = font2.render('Press F for shop', True, (255,255,255))
                screen.blit(shop_pen, (190, 320))

            shop_font()

            def restart():
                q_to = font2.render('Press ESC to restart', True, (255,255,255))
                screen.blit(q_to, (145, 220))

            restart()

        if shine > 20 and hitbox.colliderect(hitbox___):
            speed_ = 0
            speed__ = 0
            speed___ = 0
            vel = 0
            vel_ = 0
            vel__ = 0
            vel___ = 0
            point_speed = 0
            pbullet_speed = 0
            check = True
            coin_timer = 0
            coin_hit.x = random.randint(1,200)
            coin_hit.y = random.randint(1,568)
            pbullet_hitbox.x = 2000

            screen.blit(bluebg, (0,0))

            def shop_font():
                shop_pen = font2.render('Press F for shop', True, (255,255,255))
                screen.blit(shop_pen, (190, 320))

            shop_font()

            def restart():
                q_to = font2.render('Press ESC to restart', True, (255,255,255))
                screen.blit(q_to, (145, 220))

            restart()

        if shine > 35 and hitbox.colliderect(alien_hitbox):
            speed_ = 0
            speed__ = 0
            speed___ = 0
            vel = 0
            vel_ = 0
            vel__ = 0
            vel___ = 0
            point_speed = 0
            pbullet_speed = 0
            check = True
            coin_timer = 0
            coin_hit.x = random.randint(1,200)
            coin_hit.y = random.randint(1,568)
            pbullet_hitbox.x = 2000

            screen.blit(bluebg, (0,0))

            def shop_font():
                shop_pen = font2.render('Press F for shop', True, (255,255,255))
                screen.blit(shop_pen, (190, 320))

            shop_font()

            def restart():
                q_to = font2.render('Press ESC to restart', True, (255,255,255))
                screen.blit(q_to, (145, 220))
            
            restart()

        if hitbox.colliderect(bullet_hitbox):
            speed_ = 0
            speed__ = 0
            speed___ = 0
            vel = 0
            vel_ = 0
            vel__ = 0
            vel___ = 0
            point_speed = 0
            pbullet_speed = 0
            check = True
            coin_timer = 0
            coin_hit.x = random.randint(1,200)
            coin_hit.y = random.randint(1,568)
            pbullet_hitbox.x = 2000

            screen.blit(bluebg, (0,0))

            def shop_font():
                shop_pen = font2.render('Press F for shop', True, (255,255,255))
                screen.blit(shop_pen, (190, 320))

            shop_font()

            def restart():
                q_to = font2.render('Press ESC to restart', True, (255,255,255))
                screen.blit(q_to, (145, 220))

            restart()

        if hitbox.colliderect(bullet__hitbox):
            speed_ = 0
            speed__ = 0
            speed___ = 0
            vel = 0
            vel_ = 0
            vel__ = 0
            vel___ = 0
            point_speed = 0
            pbullet_speed = 0
            check = Truecoin_timer = 0
            coin_hit.x = random.randint(1,200)
            coin_hit.y = random.randint(1,568)
            pbullet_hitbox.x = 2000

            screen.blit(bluebg, (0,0))

            def shop_font():
                shop_pen = font2.render('Press F for shop', True, (255,255,255))
                screen.blit(shop_pen, (190, 320))

            shop_font()

            def restart():
                q_to = font2.render('Press ESC to restart', True, (255,255,255))
                screen.blit(q_to, (145, 220))

            restart()

        if score == 0:
            speed_ = 0
            speed__ = 0
            speed___ = 0
            vel = 0
            vel_ = 0
            vel__ = 0
            vel___ = 0
            point_speed = 0
            pbullet_speed = 0
            mainmenu = True
            coin_timer = 0
            coin_hit.x = random.randint(1,200)
            coin_hit.y = random.randint(1,568)

            screen.blit(bluebg, (0,0))

            def shop_font():
                shop_pen = font2.render('Press F for shop', True, (255,255,255))
                screen.blit(shop_pen, (190, 320))

            shop_font()

            def main_menu():
                main_pen = font2.render('Press H to start', True, (255,255,255))
                screen.blit(main_pen, (190, 220))

            main_menu()

        if pausescreen == True:
            speed_ = 0
            speed__ = 0
            speed___ = 0
            vel = 0
            vel_ = 0
            vel__ = 0
            vel___ = 0
            point_speed = 0
            pbullet_speed = 0

            screen.blit(bluebg, (0,0))

            def pause():
                esc_to = font2.render('Press E to resume', True, (255,255,255))
                screen.blit(esc_to, (185, 270))
            
            pause()
        
        if shop == True:
            screen.blit(bluebg, (0,0))

            screen.blit(val1, (278, 180))
            screen.blit(val2, (278, 280))
            screen.blit(val3, (278, 380))

            def u_for_info():
                u_for1 = font1.render('Press U for info', True, (255,255,255))
                u_for2 = font1.render('Press J for info', True, (255,255,255))
                u_for3 = font1.render('Press N for info', True, (255,255,255))
                screen.blit(u_for1, (530,230))
                screen.blit(u_for2, (530,330))
                screen.blit(u_for3, (530,430))

            def g_to_quit():
                gto = font.render('Press G to quit the shop', True, (255,255,255))
                screen.blit(gto, (260, 550))

            def your_balance():
                balance = font2.render('Your balance: ' + str(money), True, (255,255,255))
                screen.blit(balance, (205, 95))

            def original_ufo():
                original = font.render('Starter UFO', True, (255,255,255))
                screen.blit(original, (100, 300))
            
            def freeUfo():
                free = font.render('Price 0$', True, (255,255,255))
                screen.blit(free, (370, 300))
            
            def key2():
                key2_press = font.render('Press 2 to equip', True, (255,255,255))
                screen.blit(key2_press, (530, 300))

            def spaceship1():
                high_tech = font.render('High tech UFO', True, (255,255,255))
                screen.blit(high_tech, (100, 200))
            
            def spaceship1_offer():
                high_tech_offer = font.render('Price 30$', True, (255,255,255))
                screen.blit(high_tech_offer, (370, 200))

            def alien_Ufo():
                alienU = font.render('Alien UFO', True, (255,255,255))
                screen.blit(alienU, (100,400))
            
            def alien_Ufo_offer():
                alien_U = font.render('Price 10$', True, (255,255,255))
                screen.blit(alien_U, (370, 400))
            
            if lol1 == 0:
                key1_ = font.render('Press 1 to buy', True, (255,255,255))
                screen.blit(key1_, (530, 200))
            
            if lol1 == 1:
                key1__ = font.render('Press 1 to equip', True, (255,255,255))
                screen.blit(key1__, (530, 200))

            if lol2 == 0:
                key3 = font.render('Press 3 to buy', True, (255,255,255))
                screen.blit(key3, (530, 400))
            
            if lol2 == 1:
                key_3 = font.render('Press 3 to equip', True, (255,255,255))
                screen.blit(key_3, (530, 400))

            spaceship1_offer()
            spaceship1()
            original_ufo()
            freeUfo()
            key2()
            your_balance()
            g_to_quit()
            alien_Ufo()
            alien_Ufo_offer()
            u_for_info()
        
        if hightech_Ufo_info == True:
            screen.blit(bluebg, (0,0))

            def Oufo_info():
                Ofu1 = font.render('This UFO gets you more money', True, (255,255,255))
                Ofu2 = font.render('Speed = 2', True, (255,255,255))
                Ofu3 = font.render('Coins = 2x', True, (255,255,255))
                qtoshop1 = font.render('Press M to quit the info', True, (255,255,255))
                screen.blit(Ofu1, (100,150))
                screen.blit(Ofu2, (100,250))
                screen.blit(Ofu3, (100,300))
                screen.blit(qtoshop1, (270, 550))
            
            Oufo_info()
        
        if original_Ufo_info == True:
            screen.blit(bluebg, (0,0))

            def Oufo_info():
                Ofu1 = font.render('This UFO is faster than others', True, (255,255,255))
                Ofu2 = font.render('Speed = 3', True, (255,255,255))
                Ofu3 = font.render('Coins = 2x', True, (255,255,255))
                qtoshop1 = font.render('Press I to quit the info', True, (255,255,255))
                screen.blit(Ofu1, (100,150))
                screen.blit(Ofu2, (100,250))
                screen.blit(Ofu3, (100,300))
                screen.blit(qtoshop1, (270, 550))
            
            Oufo_info()
        
        if alien_Ufo_info == True:
            screen.blit(bluebg, (0,0))

            def Oufo_info():
                Ofu1 = font.render('This UFO is the deafualt UFO', True, (255,255,255))
                Ofu2 = font.render('Speed = 2', True, (255,255,255))
                Ofu3 = font.render('Coins = 1x', True, (255,255,255))
                qtoshop1 = font.render('Press K to quit the info', True, (255,255,255))
                screen.blit(Ofu1, (100,150))
                screen.blit(Ofu2, (100,250))
                screen.blit(Ofu3, (100,300))
                screen.blit(qtoshop1, (270, 550))
            
            Oufo_info()

        if pbullet_hitbox.colliderect(hitbox_):
            hitbox_.y = -150
            ex.play()
        
        if pbullet_hitbox.colliderect(hitbox__):
            hitbox__.y = -150
            ex.play()
        
        if shine >= 35 and pbullet_hitbox.colliderect(alien_hitbox):
            shine = 25

        if shine >= 20 and pbullet_hitbox.colliderect(hitbox___):
            shine = 15
        
        if val_check == 3:
            playerImg = val3

        if val_check == 2:
            playerImg = val2
        
        if val_check == 1:
            playerImg = val1
        
        if pbullet_hitbox.x < 2200:
            pbullet_hitbox.x += 4

        if bgmusic_mute == False:
            v_to = fontE.render('Press V to mute the music', True, (255,255,255))
            screen.blit(v_to, (10, 557))

        if bgmusic_mute == True:
            b_to = fontE.render('Press B for music', True, (255,255,255))
            screen.blit(b_to, (10, 557))
        
        if sfx == False:
            z_to = fontE.render('Press Z to mute the sound effects', True, (255,255,255))
            screen.blit(z_to, (10, 574))

        if sfx == True:
            x_to = fontE.render('Press X for sound effects', True, (255,255,255))
            screen.blit(x_to, (10, 574))

        # update the window
        show_money()
        esc_to()
        high_score()
        q_to_quit()
        show_score()
        pygame.time.delay(3)
        pygame.display.update()    

