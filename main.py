import pygame
from constants import SCREEN_HEIGHT,SCREEN_WIDTH,PLAYER_RADIUS
from logger import log_state
from player import Player
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

def main():
    dt = 0
    p1 = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,PLAYER_RADIUS) 
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    while (True):
        log_state()
        screen.fill("black")
        p1.update(dt)
        p1.draw(screen)
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                return False
        data = clock.tick(60)
        dt = data/1000
        pygame.display.flip()


       
        


if __name__ == "__main__":
    main()
