import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable

    asteroid_field = AsteroidField()

    clock = pygame.time.Clock()
    dt: float = 0.0

    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        updatable.update(dt)
        for drawableTmp in drawable:
            drawableTmp.draw(screen)

        for asteroidTmp in asteroids:
            if player1.collides_with(asteroidTmp):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()

        dt = clock.tick(60) / 1000
        pygame.display.flip()

if __name__ == "__main__":
    main()
