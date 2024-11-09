import pygame
import sys
from asteroidfield import AsteroidField
from player import Player
from asteroid import Asteroid
from shot import Shot
from constants import *
def main():
    pygame.init()
    clock_obj = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")

    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))   
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable) 
    player_obj = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for player in updatable:
            player.update(dt)
        for objs in asteroids:
                if objs.iscollision(player_obj):
                    sys.exit("Game over!")
        screen.fill((0,0,0))
        for player in drawable:
            player.draw(screen)
        pygame.display.flip()
        dt = clock_obj.tick(60)
        dt /=1000
        
       
       
if __name__ =='__main__':
    main()
