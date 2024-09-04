# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *


def main () :
    running = True
    pygame.init()
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
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        screen.fill((0,0,0))
        for updatable in updatables:
            updatable.update(dt)
        for asteroid in asteroids:
             if player.collision_detection(asteroid) == True:
                (print("Game Over!"),
                pygame.quit()
            )
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
if __name__ == "__main__":
        main()

