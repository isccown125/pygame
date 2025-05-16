from circleshape import CircleShape
import pygame
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius >= ASTEROID_MIN_RADIUS:
            for _ in range(2):
                angle = random.uniform(20, 50)
                asteroid = Asteroid(self.position.x, self.position.y, self.radius / 2)
                asteroid.velocity = self.velocity.rotate(angle) * 1.2
        self.kill()