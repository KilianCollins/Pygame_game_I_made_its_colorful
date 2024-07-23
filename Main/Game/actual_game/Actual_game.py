import random
import pygame
# import game_stuff
from my_colors import colors, red_color_palate,orange_color_palate
# screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
dt = 0

# for finding the center point of the screen for start
HEIGHT_Y1 = 0
HEIGHT_Y2 = 600
WIDTH_X1 = 0
WIDTH_X2 = 1000

#                           X1
# SCREEN_HEIGHT_END_COORDS = (0, SCREEN_HEIGHT)
# SCREEN_WIDTH_END_COORDS = (0,SCREEN_WIDTH)
#
# SHEC = SCREEN_HEIGHT_END_COORDS
# SWEC = SCREEN_WIDTH_END_COORDS

# creat game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Groups")

# frame rate, note: change to dt soon.
clock = pygame.time.Clock()
# FPS = 60

# should move this colors to seprate file
rand_color = random.choice(colors)


# turn this into a class later
player_one = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


# Square sprite class below
class Square(pygame.sprite.Sprite):
    """contains a func that makes a square on a *surface* """

    def __init__(self, color="yellow", x=100, y=100):
        """"child of the pygame Sprite class"""
        pygame.sprite.Sprite.__init__(self)  # this line does this somehow
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


# soon to be an entity, note: I uncecessarily over--engineered the centering of the starting sprite for fun.
square = Square("yellow", int(((WIDTH_X1 + WIDTH_X2) / 2)), int(((HEIGHT_Y1 + HEIGHT_Y2) / 2)))

# this makes a group for your sprites, is it nesseacry to have sprites ina Group??
squares = pygame.sprite.Group()
squares.add(square)
# print(squares)

''' game loop'''
run = True
while run:

    # clock.tick()
    screen.fill("gray0")  # how do pygame colors work in this context??

    # updates background
    squares.update()

    # draws sprites int the Sprite Group, note: every time I read "sprite" I think of the drink lol.
    squares.draw(screen)

    print(squares)

    # event handler v2--(7_17_24) # what is that??
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            # gets mouse's coordinates
            cursor_pos = pygame.mouse.get_pos()
            # creates square
            square = Square(random.choice(colors), cursor_pos[0],
                            cursor_pos[1])  #what am I indexing through? coursor_pos is just an int right?
            squares.add(square)
            # quit prog
        if event.type == pygame.MOUSEMOTION:
            cursor_pos_current = pygame.mouse.get_pos()
            if cursor_pos_current != pygame.mouse.get_pos():
                pygame.draw.circle(surface=screen, color=rand_color, radius=15, center=cursor_pos_current)
                # not quite a trail but getting there
        if event.type == pygame.QUIT:
            run = False
    green = pygame.draw.circle(screen, rand_color, player_one, 40)

    def player_moves():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_one.y -= 300 * dt
        if keys[pygame.K_s]:
            player_one.y += 300 * dt
        if keys[pygame.K_a]:
            player_one.x -= 300 * dt
        if keys[pygame.K_d]:
            player_one.x += 300 * dt
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
        if keys[pygame.K_SPACE]:
            screen.fill("white")
            green = pygame.draw.circle(screen, "red", player_one, 40)
        if keys[pygame.K_j]:
            screen.fill("white")
            pygame.draw.rect(screen, "red", pygame.Rect(30, 30, 60, 60), 2)
    player_moves()
    # for event in pygame.event.get():
    #     # quit program
    #     if event.type == pygame.QUIT:
    #         run = False
    pygame.display.flip()
    dt = clock.tick(60) / 1000

'''end of game loop'''
pygame.quit()

# now that i can control player one with dt i want a trail of smaller cirles left behind where player one was previously
# also i want: when spacebar is pressed "day" light is on and shows diff
# stuff and enemys that can only move during day (think the weeping angels episode of dr who)
# or the game green light red light

# maybe not that makes me feel bad and like smbs watching me.
