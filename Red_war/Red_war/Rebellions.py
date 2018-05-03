# Imports
import pygame

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
        pass
    
class Laser(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        
        self.speed = 5

    def update(self):
        self.rect.y -= self.speed
    
class Mob:

    def __init__(self):
        pass

    def update(self):
        pass


class Bomb:
    
    def __init__(self):
        pass

    def update(self):
        pass
    
    
class Fleet:

    def __init__(self):
        pass

    def update(self):
        pass

    
# Make game objects
player = Ship(384, 450, orange_bat)
lasers = pygame.sprite.Group()

# Make sprite groups
ships = pygame.sprite.GroupSingle()
ships.add(player)


# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]:
        player.move_left()
    elif pressed[pygame.K_RIGHT]:
        player.move_right()
        
    
    # Game logic (Check for collisions, update points, etc.)
    ships.update()
    lasers.update()   

        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)
    lasers.draw(screen)
    ships.draw(screen)

    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
