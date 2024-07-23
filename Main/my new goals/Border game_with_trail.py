import pygame as pg
import random
pg.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 780

run = True

# circle atributes, global

radius = 50
x = 50
y = 50
speed = 1

display_output = [SCREEN_WIDTH, SCREEN_HEIGHT]

# the double parenthesis make the input a tuple, as the .display.set_mode() only accepts
# screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen = pg.display.set_mode(display_output)
pg.display.set_caption("can I make a border?, change me")


while run:
    # pg.display.flip()
    keys = pg.key.get_pressed()
    screen.fill("gray20")
    circle = pg.draw.circle(screen, "red", [x, y], radius)
                                        # .rect[x_pos, y_pos, base, height]
    # rectangle = pg.draw.rect(screen, "blue", [30,30,500,300], width=0)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        # if event.type == keys[pg.K_ESCAPE]:
        #     pg.quit()
        #     run = False
        #     run = False #doesn't work for some reason

    # circle movement controls's
    def player_controls(x,y):
        if keys[pg.K_w] or keys[pg.K_UP]:
            y -= speed
        if keys[pg.K_s] or keys[pg.K_DOWN]:
            y += speed
        if keys[pg.K_a] or keys[pg.K_LEFT]:
            x -= speed
        if keys[pg.K_d] or keys[pg.K_RIGHT]:
            x += speed
    if keys[pg.K_ESCAPE]:
        pg.quit()
    #     why does this work here
    # screen border enforcement, border enforced to specified entity
    def border_control(x,y):
        if x < radius:
            x = radius
        if x > SCREEN_WIDTH - radius:
            x = SCREEN_WIDTH - radius
        if y < radius:
            y = radius
        if y > SCREEN_HEIGHT - radius:
            y = SCREEN_HEIGHT - radius
    player_controls(x,y)
    border_control(x,y)
    pg.display.flip()
pg.quit()
