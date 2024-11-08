import pygame
from player import Player
#from shapes import Circle

from constants import *
def main():
    pygame.init()
    clock_obj = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")

    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))   
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(dt)
        screen.fill((0,0,0))
        player.draw(screen)
        pygame.display.flip()
        dt = clock_obj.tick(60)
        dt /=1000
        
       
       
if __name__ =='__main__':
    main()
