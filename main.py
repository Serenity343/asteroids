import pygame
import sys
from constants import *
from logger import log_state
from logger import log_event
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import *

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    #variables
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameclock = pygame.time.Clock()
    dt = 0.0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    #stupid submission checks dont allow me to call it pewpews... :(
    shots = pygame.sprite.Group()

    #containers
    Player.containers = (updatable,drawable)
    Asteroid.containers =  (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    #game-elements
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #player.update(dt)
        
        updatable.update(dt)
        for obj in asteroids:

            #playercollision
            if obj.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

            #pewpew vs asteroids
            for pew in shots:
                if obj.collides_with(pew):
                    log_event("asteroid_shot")
                    pew.kill()
                    obj.split()

        #drawscreen
        screen.fill("black")
        for object in drawable:
            object.draw(screen)

        #player.draw(screen)

        pygame.display.flip()


        dt = gameclock.tick(60) / 1000
        #print(f"{dt}")
    


if __name__ == "__main__":
    main()
