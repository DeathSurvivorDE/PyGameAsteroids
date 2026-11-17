import circleshape
import constants
import pygame

class Player(circleshape.CircleShape):
    def __init__(self, x: float, y: float, radius = constants.PLAYER_RADIUS) -> None:
        super().__init__(x, y, radius)
        self.rotation = 0

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        right = pygame.Vector2(0,1).rotate(self.rotation +90)*self.radius/1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a,b,c]

    def draw(self, screen: pygame.Surface, color: str ="white", lineWidth = constants.LINE_WIDTH ) -> None:
        pygame.draw.polygon(screen, color, self.triangle(), lineWidth)

    def rotate(self, dt: float) -> None:
        self.rotation += dt * constants.PLAYER_TURN_SPEED

    def move(self, dt:float) -> None:
        unit_vector = pygame.Vector2(0,1)
        unit_vector = unit_vector.rotate(self.rotation) # Adding current player rotationstate
        unit_vector *= (constants.PLAYER_SPEED * dt) # adding the current motion component to vector
        self.position += unit_vector # updatig the position with the motion vector


    def update(self, dt:float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)
