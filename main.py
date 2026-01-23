import sys
import pygame
from constants import SCREEN_HEIGHT,SCREEN_WIDTH,PLAYER_RADIUS,SHOT_RADIUS
from logger import log_state,log_event
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots,drawable,updatable)
    dt = 0
    p1 = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2) 
    a1 = AsteroidField()


    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    while (True):
        log_state()
        screen.fill("black")
        updatable.update(dt)       
        for dr in drawable:
            dr.draw(screen)
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                return False
        for obj in asteroids:
            if(obj.collides_with(p1)):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        data = clock.tick(60)
        dt = data/1000
        pygame.display.flip()


       
        


if __name__ == "__main__":
    main()
