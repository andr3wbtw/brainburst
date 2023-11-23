import pygame

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()  #Force frame rate to be slower
surfaceSizeX = 1000
surfaceSizeY = 500
pygame.display.set_caption('BrainBurst') # change window name
screen = pygame.display.set_mode((surfaceSizeX,surfaceSizeY))
gameState = "menu"