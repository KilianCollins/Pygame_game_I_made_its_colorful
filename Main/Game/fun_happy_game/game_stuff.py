import random
import pygame



pygame.init()

global player_green_circle
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280




screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #why the two parenthessis?
display_ouput = [SCREEN_WIDTH, SCREEN_HEIGHT]
pygame.display.set_caption("funny game")

# x = screen.get_width() / 2
# y = screen.get_width() / 2

speed = 3
x = 40
y = 40
player_radius = 40


clock = pygame.time.Clock()
running = True
# how does this instance of dt(delta time)in this context work??
dt = 0


class Square(pygame.sprite.Sprite):
    """contains a func that makes a square on a *surface* """



    def __init__(self, color="yellow", x=100, y=100):
        """"child of the pygame Sprite class"""
        pygame.sprite.Sprite.__init__(self)  # this line does this somehow
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
# ww



# sets player starting pos as the middle of the window
# start_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# # trying to make this func change the player's shape every time you hit the space bar or smth
# def charactor_changer(color,shape,radius=40, width=40, height=50, border_raiduis= 0):
#     '''color == desiered color, shape== desierd character shape, radius == desierd raduis, outline == desiered thicknews'''
#     if shape == "circle":
#         return pygame.draw.circle(screen, color, player_one, radius)
#     if shape == "rectangle":
#         return pygame.draw.rect(screen, color, player_one, width, border_raiduis)
#


while running:
    keys = pygame.key.get_pressed()
    screen.fill("black")

    green = pygame.draw.circle(screen, "darkseagreen1", [x, y], player_radius)
    # trail = pygame.draw.line(screen, "darkseagreen1", , (640, 135), width=3)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #         make ecape key exit funcitonhere too.
    # make a button
     # gray13 is nice and warm
    # player sprites, i dont know how to add them all to a class yet
    # green = pygame.draw.
# tomorow take these controls and dt and implament it into THE ****Actual Game**** file

    if keys[pygame.K_w] or keys[pygame.K_UP]:
        y -= speed * dt
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        y += speed * dt
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        x -= speed * dt
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        x += speed * dt
    if keys[pygame.K_ESCAPE]:
        pygame.quit()

        # screen border enforcement, border enforced to specified entity,  not working with dt 7.23.24 --k
        if x < player_radius:
            x = player_radius
        if x > SCREEN_WIDTH - player_radius:
            x = SCREEN_WIDTH - player_radius
        if y < player_radius:
            y = player_radius
        if y > SCREEN_HEIGHT - player_radius:
            y = SCREEN_HEIGHT - player_radius

    if keys[pygame.K_SPACE]:
        screen.fill("ivory")
        green = pygame.draw.circle(screen, "firebrick1", [x, y], player_radius)
        # trail
        # trail = pygame.draw.line(screen, "yellow", player_one.x, pygame.MOUSEMOTION.__int__() width=3)# doesnt work bc mehtod call isnt aceeptedd as endpos

    if keys[pygame.K_j]:
        screen.fill("gray95")
        pygame.draw.rect(screen, "red3", pygame.Rect(30, 30, 60, 60), 2)
        player_green_circle = pygame.draw.circle(screen, "firebrick1", [x, y], player_radius)



# flip() the display to put your work on screen
#     player_moves()
    pygame.display.flip()
    dt = clock.tick(100) / 1000

pygame.quit()

# goals:
# make a backroung, make a charater, control charatoer

# done



# new goal:  pres key and scren changes color for x timem then back done

# now make camera follow player
