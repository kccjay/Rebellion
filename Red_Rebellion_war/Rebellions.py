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
purple_star = pygame.image.load('assets/images/end_background.png')
starry_night = pygame.image.load('assets/images/background.png')
orange_bat = pygame.image.load('assets/images/orange2.0.png')
laser_img = pygame.image.load('assets/images/laser2.0.png')
red_bat = pygame.image.load('assets/images/red3.1.png')
e_laser = pygame.image.load('assets/images/purple_ting.png')
green_crab = pygame.image.load('assets/images/tri_war.png')
light_laser = pygame.image.load('assets/images/purple_fire.png')
get_hit = pygame.image.load('assets/images/hit.png')

deceased = False
hit = False

# Game classes
class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.speed = 3
        self.shield = 5

    def move_left(self):
        self.rect.x -= self.speed
        
    def move_right(self):
        self.rect.x += self.speed

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
            
        if self.shield == 0:
            #EXPLOSION.play()
            self.kill()
            print("*player* EXPLOSION!")
            
        if self.rect.x >= reloc_xr:
            self.rect.x = reloc_xr
        elif self.rect.x <= reloc_xl:
            self.rect.x = reloc_xl
        

            
    
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
    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

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

class Mob2(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.shield = 2

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
            print("*clink*")
            

        if self.shield == 0:
            #EXPLOSION.play()
            self.kill()
            print("*enemy* KABOOM!")


class Bomb(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        
        self.speed = 3

    def update(self):
        self.rect.y += self.speed

        if self.rect.y >= 632:
            self.kill()
    
    
class Fleet:

    def __init__(self, mobs):
        self.mobs = mobs
        self.moving_right = True
        self.speed = 5
        self.bomb_rate = 60

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
                m.rect.y += 15
                #kills the fleet when they reach the beyond point
                if m.rect.y >= 634:
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
    global player, mobs, bombs, fleet, ships, lasers, stage
    # Make game objects
    #500
    player = Ship(420, 450, orange_bat)
    lasers = pygame.sprite.Group()
    #mob1 = Mob(128, 74, red_bat)
    mob1 = Mob(128, 74, red_bat)
    mob2 = Mob(256, 74, red_bat)
    mob3 = Mob(384, 74, red_bat)
    mob4 = Mob(573, 74, red_bat)
    mob5 = Mob(701, 74, red_bat)
    mob6 = Mob(829, 74, red_bat)
    mob7 = Mob2(120, -100, green_crab)
    mob8 = Mob2(701, -100, green_crab)
    mob9 = Mob2(410, -100, green_crab)
    

    # Make sprite groups
    ships = pygame.sprite.GroupSingle()
    ships.add(player)

    mobs = pygame.sprite.Group()
    mobs.add(mob1, mob2, mob3, mob4, mob5, mob6, mob7, mob8, mob9)

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
                if event.key == pygame.K_x:
                        stage = END
                    
            elif stage == END:
                if event.key == pygame.K_2:
                    setup()
                                    
            
         
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT] and stage == PLAYING:
        player.move_left()
    elif pressed[pygame.K_RIGHT] and stage == PLAYING:
        player.move_right()
    # Game logic (Check for collisions, update points, etc.)
    if stage == PLAYING:
        ships.update()
        lasers.update()
        mobs.update(lasers)
        bombs.update()
        fleet.update()

    if stage == PLAYING:    
        if len(ships) == 0:
            stage = END
        if len(mobs) == 0:
            stage = END        
    

    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.blit(starry_night, (0, 0))        
    lasers.draw(screen)
    ships.draw(screen)
    bombs.draw(screen)
    mobs.draw(screen)

    #used to indicate the stage is on END
    if stage == END:
        print("The game has ended")
        print("Title card coming soon")
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)




# Close window and quit
pygame.quit()
