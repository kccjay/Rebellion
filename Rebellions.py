#
#
#
#
#
#
#
# Imports
import pygame
import random
import sys



# Initialize game engine
pygame.init()


# Window
WIDTH = 1000
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
TITLE = "Rebellion War"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (100, 255, 100)

# Images

#Background
starry_night = pygame.image.load('assets/images/background.png')
starry_night2 = pygame.image.load('assets/images/background-2.png')
starry_night3 = pygame.image.load('assets/images/background-3.png')
starry_night4 = pygame.image.load('assets/images/background-4.png')
#Splash Screen
splash = pygame.image.load('assets/images/splash-1.png')
splash2 = pygame.image.load('assets/images/splash-2.png')
splash3 = pygame.image.load('assets/images/splash-3.png')
splash4 = pygame.image.load('assets/images/splash-4.png')
splash5 = pygame.image.load('assets/images/splash-5.png')
splash6 = pygame.image.load('assets/images/splash-6.png')
splash7 = pygame.image.load('assets/images/splash-7.png')
splash8 = pygame.image.load('assets/images/splash-8.png')
splash9 = pygame.image.load('assets/images/splash-9.png')
splash10 = pygame.image.load('assets/images/splash-10.png')
splash11 = pygame.image.load('assets/images/splash-11.png')
splash12 = pygame.image.load('assets/images/splash-12.png')
splash13 = pygame.image.load('assets/images/splash-13.png')
splash14 = pygame.image.load('assets/images/splash-14.png')
splash15 = pygame.image.load('assets/images/splash-15.png')
splash16 = pygame.image.load('assets/images/splash-16.png')
splash17 = pygame.image.load('assets/images/splash-17.png')
splash18 = pygame.image.load('assets/images/splash-18.png')
splash19 = pygame.image.load('assets/images/splash-19.png')
splash20 = pygame.image.load('assets/images/splash-20.png')
splash21 = pygame.image.load('assets/images/splash-21.png')
splash22 = pygame.image.load('assets/images/splash-22.png')
splash23 = pygame.image.load('assets/images/splash-23.png')
#Player
orange_bat2 = pygame.image.load('assets/images/orange2.0-1.png')
orange_bat3 = pygame.image.load('assets/images/orange2.0-2.png')
orange_bat4 = pygame.image.load('assets/images/orange2.0-3.png')
orange_bat5 = pygame.image.load('assets/images/orange2.0-4.png')
orange_bat6 = pygame.image.load('assets/images/orange2.0-5.png')
orange_bat7 = pygame.image.load('assets/images/orange2.0-6.png')
orange_bat8 = pygame.image.load('assets/images/orange2.0-7.png')
#Lasers
laser_img = pygame.image.load('assets/images/laser2.0.png')
e_laser = pygame.image.load('assets/images/purple_ting.png')
light_laser = pygame.image.load('assets/images/purple_fire.png')
#Secondary Enemy
green_crab = pygame.image.load('assets/images/triangle-1.png')
green_crab2 = pygame.image.load('assets/images/triangle-2.png')
green_crab3 = pygame.image.load('assets/images/triangle-3.png')
green_crab_hit = pygame.image.load('assets/images/triangle-4.png')
#Primary Enemy 
red_bat = pygame.image.load('assets/images/red_troop-1.png')
red_bat2 = pygame.image.load('assets/images/red_troop-2.png')
red_bat3 = pygame.image.load('assets/images/red_troop-3.png')
red_bat4 = pygame.image.load('assets/images/red_troop-4.png')
red_bat5 = pygame.image.load('assets/images/red_troop-5.png')

#for when the player gets hit


deceased = False
hit = False
timerdone = False

# Game classes
class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y, image1, image2, image3, image4, image5, image6, image7):
        super().__init__()
        self.image = image1
        self.image2 = image2
        self.image3 = image3
        self.image4 = image4
        self.image5 = image5
        self.image6 = image6
        self.image7 = image7
        #when putting a new image in make sure to add a new self.image#
        #add image# to init
        #add self.image# to self.ticks if statements
        
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
        
        self.speed = 5
        self.plusspeed = 50
        self.shield = 5
        
        
        self.ticks = 0
        

    def move_left(self):
        self.rect.x -= self.speed
        
    def move_right(self):
        self.rect.x += self.speed

    def move_left2(self):
        self.rect.x -= self.plusspeed
        
    def move_right2(self):
        self.rect.x += self.plusspeed

    def shoot(self):
        laser = Laser(laser_img)
        laser.rect.centerx = self.rect.centerx
        laser.rect.centery = self.rect.top
        lasers.add(laser)

    def update(self):
        hit_list = pygame.sprite.spritecollide(self, bombs, True)
        reloc_xr = 850
        reloc_xl = 0
        
        for hit in hit_list:
            # play hit sound
            self.shield -= 1
            print("OUCH! ... " + str(self.shield) + " more hits left")
            
        if self.shield == 0:
            #EXPLOSION.play()
            self.kill()
            print("*player* EXPLOSION!")
            
        if self.rect.x >= reloc_xr:
            self.rect.x = reloc_xr
        elif self.rect.x <= reloc_xl:
            self.rect.x = reloc_xl
        
        self.ticks += 2
        if self.ticks %70 == 0:
            self.image, self.image2, self.image3, self.image4, self.image5, self.image6, self.image7 = self.image2, self.image3, self.image4, self.image5, self.image6, self.image7, self.image

class Laser(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        
        self.speed = 7

    def update(self):
        self.rect.y -= self.speed

        if self.rect.y <= 0:
            self.kill()
    
class Mob(pygame.sprite.Sprite):
    def __init__(self, x, y, image, image2, image3, image4, image5):
        super().__init__()

        self.image = image
        self.image2 = image2
        self.image3 = image3
        self.image4 = image4
        self.image5 = image5 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.ticks = 0

    def drop_bomb(self):
        bomb = Bomb(e_laser)
        bomb.rect.centerx = self.rect.centerx
        bomb.rect.centery = self.rect.bottom
        bombs.add(bomb)
    
    def update(self, lasers):
        hit_list = pygame.sprite.spritecollide(self, lasers, True)

        if len(hit_list) > 0:
            #EXPLOSION.play()
            self.kill()
            print("*enemy*BOOM!")
            
        self.ticks += 1
        if self.ticks %40 == 0:
            self.image, self.image2, self.image3, self.image4, self.image5 = self.image2, self.image3, self.image4, self.image5, self.image

class Mob2(pygame.sprite.Sprite):
    def __init__(self, x, y, image, image2, image3, image4):
        super().__init__()
        self.image = image
        self.image2 = image2
        self.image3 = image3
        self.image4 = image4
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.shield = 3
        self.ticks = 0

    def drop_bomb(self):
        bomb = Bomb(light_laser)
        bomb.rect.centerx = self.rect.centerx
        bomb.rect.centery = self.rect.bottom
        bombs.add(bomb)
    
    def update(self, lasers):
        hit_list = pygame.sprite.spritecollide(self, lasers, True)

        for hit in hit_list:
            # play hit sound
            self.shield -= 1
            # I need help with this
            # This is suppose to change the character
            #showing the character is hurt
            self.image4
            print("*clink" + str(self.shield) + "*")
            

        if self.shield == 0:
            #EXPLOSION.play()
            self.kill()
            print("*enemy* KABOOM!")
            
        self.ticks += 1
        if self.ticks %40 == 0:
            self.image, self.image2, self.image3 = self.image2, self.image3, self.image
        


class Bomb(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        
        self.speed = 7

    def update(self):
        self.rect.y += self.speed

        if self.rect.y >= 632:
            self.kill()

class Background(pygame.sprite.Sprite):
    def __init__(self, x, y, image, image2, image3, image4):
        super().__init__()
        self.ticks = 0
        self.image = image
        self.image2 = image2
        self.image3 = image3
        self.image4 = image4
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        

    def update(self):
        self.ticks += 1
        if self.ticks %98 == 0:
            self.image, self.image2, self.image3, self.image4 = self.image2, self.image3, self.image4, self.image
class Splash(pygame.sprite.Sprite):
    def __init__(self, x, y, image, image2, image3, image4, image5, image6, image7, image8, image9, image10, image11, image12, image13, image14, image15, image16, image17, image18, image19, image20, image21, image22, image23):
        super().__init__()
        self.ticks = 0
        self.image = image
        self.image2 = image2
        self.image3 = image3
        self.image4 = image4
        self.image5 = image5
        self.image6 = image6
        self.image7 = image7
        self.image8 = image8
        self.image9 = image9
        self.image10 = image10
        self.image11 = image11
        self.image12 = image12
        self.image13 = image13
        self.image14 = image14
        self.image15 = image15
        self.image16 = image16
        self.image17 = image17
        self.image18 = image18
        self.image19 = image19
        self.image20 = image20
        self.image21 = image21
        self.image22 = image22
        self.image23 = image23
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        

    def update(self):
        self.ticks += 1
        if self.ticks %3 == 0:
            self.image, self.image2, self.image3, self.image4, self.image5, self.image6, self.image7, self.image8, self.image9, self.image10, self.image11, self.image12, self.image13, self.image14, self.image15, self.image16, self.image17, self.image19, self.image20, self.image21, self.image22, self.image23, self.image18 = self.image2, self.image3, self.image4, self.image5, self.image6, self.image7, self.image8, self.image9, self.image10, self.image11, self.image12, self.image13, self.image14, self.image15, self.image16, self.image17, self.image19, self.image20, self.image21, self.image22, self.image23, self.image18, self.image
            
class Fleet:

    def __init__(self, mobs):
        self.mobs = mobs
        self.moving_right = True
        self.speed = 3
        self.bomb_rate = 50

    def move(self):
        reverse = False
        
        for m in mobs:
            if self.moving_right:
                m.rect.x += self.speed
                if m.rect.right >= WIDTH:
                    reverse = True
            else:
                m.rect.x -= self.speed
                if m.rect.left <=0:
                    reverse = True

        if reverse == True:
            self.moving_right = not self.moving_right
            for m in mobs:
                #determines the speed of the fleet
                m.rect.y += 20
                #kills the fleet when they reach the beyond point
                if m.rect.y >= 400:
                    m.kill()
            

    def choose_bomber(self):
        rand = random.randrange(0, self.bomb_rate)
        all_mobs = mobs.sprites()
        
        if len(all_mobs) > 0 and rand == 0:
            return random.choice(all_mobs)
        else:
            return None
    
    def update(self):
        self.move()

        bomber = self.choose_bomber()
        if bomber != None:
            bomber.drop_bomb()

def setup():
    global player, mobs, bombs, fleet, ships, lasers, stage, background, screen_splash

    # Make game objects
    #500
    player = Ship(420, 450, orange_bat2, orange_bat3, orange_bat4, orange_bat5, orange_bat6, orange_bat7, orange_bat8)
    lasers = pygame.sprite.Group()
    #mob1 = Mob(128, 74, red_bat)
    mob1 = Mob(128, 74, red_bat, red_bat2, red_bat3, red_bat4, red_bat5)
    mob2 = Mob(256, 74, red_bat, red_bat2, red_bat3, red_bat4, red_bat5)
    mob3 = Mob(384, 74, red_bat, red_bat2, red_bat3, red_bat4, red_bat5)
    mob4 = Mob(573, 74, red_bat, red_bat2, red_bat3, red_bat4, red_bat5)
    mob5 = Mob(701, 74, red_bat, red_bat2, red_bat3, red_bat4, red_bat5)
    mob6 = Mob(829, 74, red_bat, red_bat2, red_bat3, red_bat4, red_bat5)
    mob7 = Mob2(120, -100, green_crab, green_crab2, green_crab3, green_crab_hit)
    mob8 = Mob2(701, -100, green_crab, green_crab2, green_crab3, green_crab_hit)
    mob9 = Mob2(410, -100, green_crab, green_crab2, green_crab3, green_crab_hit)

    back1 = Background(0, 0, starry_night, starry_night2, starry_night3, starry_night4)
    
    intro = Splash(0, 0, splash, splash2, splash3, splash4, splash5, splash6, splash7, splash8, splash9, splash10, splash11, splash12, splash13, splash14, splash15, splash16, splash17, splash18, splash19, splash20, splash21, splash22, splash23)

    # Make sprite groups
    ships = pygame.sprite.GroupSingle()
    ships.add(player)

    mobs = pygame.sprite.Group()
    mobs.add(mob1, mob2, mob3, mob4, mob5, mob6, mob7, mob8, mob9)

    background = pygame.sprite.GroupSingle()
    background.add(back1)

    screen_splash = pygame.sprite.GroupSingle()
    screen_splash.add(intro)

    bombs = pygame.sprite.Group()

    fleet = Fleet(mobs)

    stage = START

# Game loop
PLAYING = 1
START = 0
END = 3
PAUSE = 4
pew_shot = 0
#stage = START

setup()
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        #Finish the playing end etc
        elif event.type == pygame.KEYDOWN:
            if stage == START:
                if event.key == pygame.K_DELETE:
                        stage = PLAYING
                        
            elif stage == PLAYING:
                if event.key == pygame.K_SPACE:
                        pew_shot += 1
                        player.shoot()
                        print("Pew!" + str(pew_shot))
                if event.key == pygame.K_DELETE:
                        stage = END
                    
            elif stage == END:
                if event.key == pygame.K_DELETE:
                    setup()
                                    
            
         
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT] and stage == PLAYING:
        player.move_left()
    elif pressed[pygame.K_RIGHT] and stage == PLAYING:
        player.move_right()
    if pressed[pygame.K_a] and stage == PLAYING:
        player.move_left2()
    elif pressed[pygame.K_d] and stage == PLAYING:
        player.move_right2()
    # Game logic (Check for collisions, update points, etc.)
    if stage == START:
        screen_splash.update()
    if stage == END:
        screen_splash.update()
        
                   
    if stage == PLAYING:
        ships.update()
        lasers.update()
        mobs.update(lasers)
        bombs.update()
        fleet.update()
        background.update()
        
        

    if stage == PLAYING:    
        if len(ships) == 0:
            stage = END
        if len(mobs) == 0:
            stage = END        
    

    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen_splash.draw(screen)
    background.draw(screen)
    lasers.draw(screen)
    ships.draw(screen)
    bombs.draw(screen)
    mobs.draw(screen)
    if stage == START:
        screen_splash.draw(screen)
    if stage == END:
        screen_splash.draw(screen)
    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)




# Close window and quit
pygame.quit()
