from constants import SHOT_RADIUS
import pygame
from circleshape import CircleShape
class Shot(CircleShape):
        
    def __init__(self, x, y ):
        super().__init__(x,y,SHOT_RADIUS )
        self.rotation = 0

    def move(self, dt):
        self.position +=  self.velocity* dt
    def draw(self, screen):
        pygame.draw.circle(screen, "blue", self.position,SHOT_RADIUS,2)

    def update(self, dt):
       self.move(dt) 
    
    
