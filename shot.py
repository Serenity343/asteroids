import pygame
from constants import SHOT_RADIUS
from constants import SHOT_WIDTH
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
            pygame.draw.circle(screen, "white", self.position,self.radius, SHOT_WIDTH)
        
    def update(self, dt):
        self.position += (self.velocity * dt)