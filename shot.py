from circleshape import *
from constants import *
import pygame

class Shot(CircleShape):
    def __init__(self, x: float, y: float, radius: float = SHOT_RADIUS) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface, color:str = "red") -> None:
        pygame.draw.circle(screen, color, self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity*dt
