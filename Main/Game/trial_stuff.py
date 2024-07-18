import random
import pygame
import game_stuff

# screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

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
FPS = 60
# pygame's list of named colors: https://www.pygame.org/docs/ref/color_list.html
colors = ["deeppink", "red", "firebrick1", "orange", "gold", "yellow", "green", "blue", "mediumblue", "indigo", "purple", "violet"]


# Square sprite class below
class Square(pygame.sprite.Sprite):
    """contains a func that makes a square on a *surface* """

    def __init__(self, color="yellow", x=100, y=100):
        """"child of the pygame Sprite class"""
        pygame.sprite.Sprite.__init__(self) #this line does this some how
        self.image = pygame.Surface((50,50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

# soon to be an entity, note: I uncecessarily over--engineered the centering of the starting sprite for fun.
square = Square("yellow", int(((WIDTH_X1 + WIDTH_X2) /2)), int(((HEIGHT_Y1 + HEIGHT_Y2) /2) ) )

# this makes a group for your sprites, is it nesseacry to have sprites ina Group??
squares = pygame.sprite.Group()
squares.add(square)
# print(squares)

''' game loop'''
run = True
while run:

    clock.tick(FPS)
    screen.fill("black") #how do pygame colors work in this context??

    # updates backgroudn
    squares.update()

    # draws sprites int the Sprite Group, note: every time I read "sprite" I think of the drink lol.
    squares.draw(screen)

    print(squares)

    # event handler v2--(7_17_24) # what is that??
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            # gets mouse's coordinates
            cursor_pos = pygame.mouse.get_pos()
            #create square
            square = Square(random.choice(colors), cursor_pos[0], cursor_pos[1]) #what am I indexing through? coursor_pos is just an int right?
            squares.add(square)
            #quit prog
        if event.type == pygame.QUIT:
            run = False




    # for event in pygame.event.get():
    #     # quit program
    #     if event.type == pygame.QUIT:
    #         run = False
    pygame.display.flip()

'''end of game loop'''
pygame.quit()


