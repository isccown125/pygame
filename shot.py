from circleshape import CircleShape
import pygame
class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, -1)
        
    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = (int(self.position.x), int(self.position.y))

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.rect.center, self.radius)
