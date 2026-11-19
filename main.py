import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from shot import *


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Group Definitions
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #Class Group Assignment
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)

    #Asteroid Field
    asteroid_field = AsteroidField()

    #Game Time keeping and pacing
    clock = pygame.time.Clock()
    dt: float = 0.0

    #player initialization
    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    #Game loop
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

            for shotTmp in shots:
                if asteroidTmp.collides_with(shotTmp):
                    #log_event("asteroid_shot")
                    asteroidTmp.split()
                    shotTmp.kill()

        dt = clock.tick(60) / 1000
        pygame.display.flip()

if __name__ == "__main__":
    main()
