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
orange_bat = pygame.image.load('assets/images/orange2.0.png')
laser_img = pygame.image.load('assets/images/laser2.0.png')
red_bat = pygame.image.load('assets/images/red3.0.png')
e_laser = pygame.image.load('assets/images/purple_eye.png')



# Game classes
class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.speed = 3
        self.shield = 10

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
        
        for hit in hit_list:
            # play hit sound
            self.shield -= 1
            
        if self.shield == 0:
            #EXPLOSION.play()
            self.kill()

            
    
class Laser(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        
        self.speed = 5

    def update(self):
        self.rect.y -= self.speed
    
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

class Bomb(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        
        self.speed = 3

    def update(self):
        self.rect.y += self.speed
    
    
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
                m.rect.y += 32
            

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

    
# Make game objects
player = Ship(384, 450, orange_bat)
lasers = pygame.sprite.Group()
mob1 = Mob(128, 64, red_bat)
mob2 = Mob(256, 64, red_bat)
mob3 = Mob(384, 64, red_bat)


# Make sprite groups
ships = pygame.sprite.GroupSingle()
ships.add(player)

mobs = pygame.sprite.Group()
mobs.add(mob1, mob2, mob3)

bombs = pygame.sprite.Group()

fleet = Fleet(mobs)

# Game loop
PLAYING = 1
START = 0
END = 3
PAUSE = 4

done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        #Finish the playing end etc
        elif event.type == pygame.KEYDOWN:
            if stage == START:
                
            if event.key == pygame.K_1:
                    stage = PLAYING
                    
            if event.key == pygame.K_SPACE:
                 player.shoot()
                 
            pressed = pygame.key.get_pressed()

            if pressed[pygame.K_LEFT]:
                player.move_left()
            elif pressed[pygame.K_RIGHT]:
                player.move_right()
        

        elif stage == END:
            if event.key == pygame.K_2:
                
                
            
    
    # Game logic (Check for collisions, update points, etc.)
    ships.update()
    lasers.update()
    mobs.update(lasers)
    bombs.update()
    fleet.update()
        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)
    lasers.draw(screen)
    ships.draw(screen)
    bombs.draw(screen)
    mobs.draw(screen)
    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
