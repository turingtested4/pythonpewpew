import random
from logger import log_event
import pygame
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self,Group):
        if(self.radius < ASTEROID_MIN_RADIUS):
            self.kill()
        else:
            self.kill()
            log_event("asteroid_split")
            angl = random.uniform(20,50)
            vc1 = self.velocity.rotate(angl)
            vc2 = -(self.velocity.rotate(angl))
            a1 = Asteroid(self.position.x, self.position.y ,self.radius - ASTEROID_MIN_RADIUS)
            a2 =    Asteroid(self.position.x, self.position.y,self.radius - ASTEROID_MIN_RADIUS)

            a1.velocity = vc1 * 1.2
            a2.velocity = vc2 * 1.2
            Group.add(a1)
            Group.add(a2)
            

            



            