from shot import Shot
import pygame
from circleshape import CircleShape
from constants import PLAYER_SHOOT_SPEED, PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_COOLDOWN

class Player(CircleShape): 
    def __init__(self, x, y): 
        super().__init__(x, y, PLAYER_RADIUS) 
        self.rotation = 0
        self.timer = 0
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def move(self, dt):
        vec = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += vec * PLAYER_SPEED * dt
    
    def shoot(self ):
        # check to prevent shoot spam
        if self.timer >0 :
            return
        shot = Shot(self.position.x, self.position.y)
        direction = pygame.Vector2(0,1).rotate(self.rotation)

        self.timer = PLAYER_SHOOT_COOLDOWN
        shot.velocity = direction*PLAYER_SHOOT_SPEED 


    def draw(self, screen):
        player_pos = self.triangle() 
        pygame.draw.polygon(screen, "white", player_pos, 2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
           self.rotate(-1*dt)
        if keys[pygame.K_d]:
           self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        
        if keys[pygame.K_SPACE]:
            self.shoot()
        if keys[pygame.K_s]:
            self.move(-1*dt)
