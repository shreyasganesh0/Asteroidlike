from constants import ASTEROID_MIN_RADIUS
import random
import pygame
from circleshape import CircleShape
class Asteroid(CircleShape):
        
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)
        child_radius = self.radius - ASTEROID_MIN_RADIUS 
        vec1  = self.velocity.rotate(random_angle)
        vec2 = self.velocity.rotate(-1*random_angle)
        child_1 = Asteroid(self.position.x,self.position.y, child_radius)
        child_2 = Asteroid(self.position.x,self.position.y, child_radius)

        child_1.velocity = vec1 * 1.2
        child_2.velocity = vec2 * 1.2
    def move(self, dt):
        self.position +=  self.velocity* dt
    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position,self.radius,2)

    def update(self, dt):
       self.move(dt) 
