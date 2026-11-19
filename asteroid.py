import circleshape
import pygame
import constants
from logger import *
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface, color:str = "white") -> None:
        pygame.draw.circle(screen, color, self.position, self.radius, constants.LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity*dt

    def split(self) -> None:
        old_rad_Tmp = self.radius
        old_pos_Tmp = self.position
        old_vel_Tmp = self.velocity
        self.kill()

        if old_rad_Tmp <= constants.ASTEROID_MIN_RADIUS:
            log_event("asteroid_destroid")
            return

        log_event("asteroid_split")
        rotation_Tmp = random.uniform(20, 50)

        new_vel_Tmp1 = new_vel_Tmp2 = old_vel_Tmp * 1.2
        new_vel_Tmp1 = new_vel_Tmp1.rotate(rotation_Tmp)
        new_vel_Tmp2 = new_vel_Tmp2.rotate(-rotation_Tmp)

        new_rad_Tmp = old_rad_Tmp - constants.ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(old_pos_Tmp.x, old_pos_Tmp.y, new_rad_Tmp)
        asteroid2 = Asteroid(old_pos_Tmp.x, old_pos_Tmp.y, new_rad_Tmp)
        asteroid1.velocity = new_vel_Tmp1
        asteroid2.velocity = new_vel_Tmp2
