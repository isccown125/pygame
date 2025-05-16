import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    dt = 0
    clock = pygame.time.Clock()


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.fill(("#000000"))
        updatable.update(dt)
        for asteroid in asteroids.sprites():
            if player.distance_to(asteroid) < asteroid.radius + PLAYER_RADIUS:
                print('Game Over')
                exit(1)
        for dr in drawable.sprites():
            dr.draw(screen)
        for shot in shots.sprites():
            for asteroid in asteroids.sprites():
                if shot.distance_to(asteroid) < shot.radius + asteroid.radius:
                    print('Shot hit asteroid')
                    shot.kill()
                    asteroid.split()
                    break
        pygame.display.flip()



        dt = clock.tick(60) / 1000

if __name__ == '__main__':
    main()