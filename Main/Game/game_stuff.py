import random
import pygame



pygame.init()

global green

screen = pygame.display.set_mode((1280,720)) #why the two parenthessis?
clock = pygame.time.Clock()
running = True
# how the fuck does this instance of dt(delta time)in this context work??
dt = 0

# this below does nothing idk why
white_time = 30 #seconds

# sets player starting pos as the middle of the window
player_one = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# # trying to make this func change the player's shape every time you hit the space bar or smth
# def charactor_changer(color,shape,radius=40, width=40, height=50, border_raiduis= 0):
#     '''color == desiered color, shape== desierd character shape, radius == desierd raduis, outline == desiered thicknews'''
#     if shape == "circle":
#         return pygame.draw.circle(screen, color, player_one, radius)
#     if shape == "rectangle":
#         return pygame.draw.rect(screen, color, player_one, width, border_raiduis)
#


while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # make a button
    screen.fill("black")
    green = pygame.draw.circle(screen, "green", player_one, 40)

# tomorow take these controls and dt and implament it into THE ****Actual Game**** file
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

        # pygame.draw.rect(screen,"red",player_pos_of_p_1, width= 30,border_radius= -1, border_top_left_radius= -1, border_top_right_radius=-1, border_bottom_right_radius= -1, border_bottom_left_radius= -1)
        # charactor_changer(color="pink",shape="rectangle",width=50,height=20,border_raiduis=5 )











# flip() the display to put your work on screen
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()

# goals:
# make a backroung, make a charater, control charatoer

# done



# new goal:  pres key and scren changes color for x timem then back done

# now make camera follow player
