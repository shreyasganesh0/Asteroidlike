import pygame
from circleshape import CircleShape
class Asteroid(CircleShape):
        
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    
    def move(self, dt):
        self.position +=  self.velocity* dt
    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position,self.radius,2)

    def update(self, dt):
       self.move(dt) 
