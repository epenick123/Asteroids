# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
pygame.init()
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

#Variables
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = ( 255, 0, 0)
GRAY = (87,94,89)

#default loop set to Main Menu
running = "main"

#Game Loop function
def play () :
    running = "play"
    
    print( f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0  
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    Player.containers = (updatables, drawables)
    asteroid_field = AsteroidField()
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    while running == "play":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
        screen.fill((0,0,0))
        for updatable in updatables:
            updatable.update(dt)
        #Ohhh... back to main menu
        for asteroid in asteroids:
             if player.collision_detection(asteroid) == True: 
                main()
            
        for drawable in drawables:
            drawable.draw(screen)
        for asteroid in asteroids:
             for shot in shots:
                  if shot.collision_detection(asteroid) == True:
                       shot.kill()
                       asteroid.split()
        pygame.display.flip()    
        dt = (clock.tick(60)) / 1000
       
    
    
    pygame.quit()
    sys.exit()

#Main menu and associated buttons.
def main () :
    pygame.display.set_caption("ASTEROIDS!")
    running = "main"
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(GRAY)
    font = pygame.font.SysFont("freesansbold",24,True,)
    clock = pygame.time.Clock()
    dt = (clock.tick(60)) / 1000
    start_button = pygame.draw.rect(screen, (0,255,0), pygame.Rect(480,180,320,100), 10, 50)
    quit_button = pygame.draw.rect(screen, (255,0,0), pygame.Rect(480,330,320,100), 10, 50)
    options_button = pygame.draw.rect(screen, (0,0,255), pygame.Rect(480,480,320,100), 10, 50)
    start_text_surface_object = pygame.font.SysFont("freesansbold", 30).render("Start Game", True, GREEN)
    start_rect = start_text_surface_object.get_rect(center = start_button.center)
    screen.blit(start_text_surface_object, (585,225),None)

    while running == "main":
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if start_rect.collidepoint(x,y):
                    play()
        pygame.display.update()
    

    pygame.quit()
    sys.exit()

#Default startup is main menu loop
if running == "main":
        main()

