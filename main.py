import pygame
from pygame.locals import*

import menu
import functions
from variables import *

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

def main():
    ### MAIN GAME LOOP ###
    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop
        if gameState == "menu": # menu state
            menu.menu(screen)
        pygame.display.flip()
    pygame.quit()

main()