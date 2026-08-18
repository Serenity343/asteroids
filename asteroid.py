import pygame
import random
from circleshape import CircleShape
from constants import *
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position,self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):

        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")

        split_angle = random.uniform(20,50)

        asteroid1 = Asteroid(self.position.x, self.position.y, self.radius-ASTEROID_MIN_RADIUS )
        asteroid1.velocity= 1.2 * self.velocity.rotate(split_angle)
        asteroid2 = Asteroid(self.position.x, self.position.y, self.radius-ASTEROID_MIN_RADIUS )
        asteroid2.velocity= 1.2 * self.velocity.rotate(-split_angle)