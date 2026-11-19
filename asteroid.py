from tkinter.constants import TRUE

import circleshape
import pygame
import constants
from logger import *
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        self.collision = 5

    def draw(self, screen: pygame.Surface, color:str = "white") -> None:
        pygame.draw.circle(screen, color, self.position, self.radius, constants.LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity*dt
        self.collision -= 2

    def split(self) -> int:
        old_rad_Tmp = self.radius
        old_pos_Tmp = self.position
        old_vel_Tmp = self.velocity
        self.kill()

        if old_rad_Tmp <= constants.ASTEROID_MIN_RADIUS:
            log_event("asteroid_destroid")
            return 10

        log_event("asteroid_split")
        rotation_Tmp = random.uniform(20, 50)

        new_vel_Tmp1 = new_vel_Tmp2 = old_vel_Tmp * 1.2
        new_vel_Tmp1 = new_vel_Tmp1.rotate(rotation_Tmp)
        new_vel_Tmp2 = new_vel_Tmp2.rotate(-rotation_Tmp)

        new_rad_Tmp = old_rad_Tmp - constants.ASTEROID_MIN_RADIUS

        new_pos_Tmp1= old_pos_Tmp + new_vel_Tmp1.normalize()*new_rad_Tmp*0.5
        new_pos_Tmp2= old_pos_Tmp + new_vel_Tmp2.normalize()*new_rad_Tmp*0.5

        asteroid1 = Asteroid(new_pos_Tmp1.x, new_pos_Tmp1.y, new_rad_Tmp)
        asteroid2 = Asteroid(new_pos_Tmp2.x, new_pos_Tmp2.y, new_rad_Tmp)
        asteroid1.velocity = new_vel_Tmp1
        asteroid2.velocity = new_vel_Tmp2

        return 5

    def impact(self, other) -> None:
        if self.position.distance_to(other.position) < (self.position + self.velocity*0.1).distance_to((other.position + other.velocity*0.1)): return
        mass_factor_self = self.radius
        mass_factor_other = other.radius

        impulse_factor: pygame.Vector2 = (mass_factor_other * mass_factor_self)/(mass_factor_other+mass_factor_self)*(constants.ASTEROID_IMPACT_RESTITUTION)*(other.velocity - self.velocity)
        self.velocity = impulse_factor / mass_factor_self
        other.velocity = -impulse_factor / mass_factor_other
        self.collision = 1
        other.collision = 1
