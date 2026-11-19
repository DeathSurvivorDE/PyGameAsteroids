import circleshape
import constants
import pygame
import shot

class Player(circleshape.CircleShape):
    def __init__(self, x: float, y: float, radius = constants.PLAYER_RADIUS) -> None:
        super().__init__(x, y, radius)
        self.rotation = 0
        self.shoot_timer = 0
        self.weapon_heat = constants.PLAYER_WEAPON_HEAT_CAPACITY
        self.__color = (255, 255, 255)

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        right = pygame.Vector2(0,1).rotate(self.rotation +90)*self.radius/1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a,b,c]

    def draw(self, screen: pygame.Surface, lineWidth = constants.LINE_WIDTH ) -> None:
        pygame.draw.polygon(screen, self.__color, self.triangle(), lineWidth)

    def rotate(self, dt: float) -> None:
        self.rotation += dt * constants.PLAYER_TURN_SPEED

    def move(self, dt:float) -> None:
        unit_vector = pygame.Vector2(0,1)
        unit_vector = unit_vector.rotate(self.rotation) # Adding current player rotationstate
        unit_vector *= (constants.PLAYER_SPEED * dt) # adding the current motion component to vector
        self.position += unit_vector # updatig the position with the motion vector


    def update(self, dt:float) -> None:
        self.shoot_timer-= dt
        self.weapon_heat += ((constants.PLAYER_WEAPON_HEAT_CAPACITY - self.weapon_heat)/constants.PLAYER_WEAPON_HEAT_CAPACITY) *dt *constants.PLAYER_WEAPON_COOLDAOWN_FACTOR
        color_shift_tmp: int = int(255*(self.weapon_heat/constants.PLAYER_WEAPON_HEAT_CAPACITY))
        self.__color = (255, color_shift_tmp,color_shift_tmp)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self) -> None:
        if self.shoot_timer > 0: return
        if self.weapon_heat < constants.SHOT_HEAT_LOAD: return
        self.shoot_timer = constants.PLAYER_SHOOT_COOLDOWN_SECONDS
        self.weapon_heat -= constants.SHOT_HEAT_LOAD
        vectDirTmp = pygame.Vector2(0,1).rotate(self.rotation)
        vectDirTmp *= constants.SHOT_SPEED
        shot_1 = shot.Shot(self.position.x, self.position.y, constants.SHOT_RADIUS)
        shot_1.velocity = vectDirTmp
