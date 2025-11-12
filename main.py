import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock_obj = pygame.time.Clock()
    dt = 0
    
    plyer = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        log_state()
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
    
        screen.fill("black")
        plyer.draw(screen)
        pygame.display.flip()
        
        delta_time = clock_obj.tick(60)
        dt = delta_time / 1000  #convert from milliseconds to seconds
        
    
    
        
    
    print("Starting Asteroids with pygame version: pygame.version.ver")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    


if __name__ == "__main__":
    main()
