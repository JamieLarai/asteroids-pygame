from circleshape import *
from constants import *
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        #self.x = x
        #self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20.0, 50.0)
            first_velocity = self.velocity.rotate(angle)
            second_velocity = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            position = self.position
            asteroid_one = Asteroid(position.x, position.y, new_radius)
            asteroid_two = Asteroid(position.x, position.y, new_radius)
            asteroid_one.velocity = first_velocity * 1.2
            asteroid_two.velocity = second_velocity * 1.2