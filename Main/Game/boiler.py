import pygame

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

run = True

while run:

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            run = False


pygame.quit()