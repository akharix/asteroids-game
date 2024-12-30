import pygame
from constants import *
from circleshape import CircleShape

# Base class for game objects
class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', (self.position.x, self.position.y), SHOT_RADIUS)
    
    def update(self, dt):
        self.position += self.velocity * dt