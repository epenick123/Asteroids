# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main () :
    running = True
    pygame.init()
    print( f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0  
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        screen.fill((0,0,0))
        pygame.display.flip()    
        dt = (clock.tick(60)) / 1000
    pygame.quit()
if __name__ == "__main__":
        main()

