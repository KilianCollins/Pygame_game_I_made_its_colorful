import pygame as pg
from pygame.math import Vector2


class Player(pg.sprite.Sprite):

    def __init__(self, pos, *groups):
        super().__init__(*groups)
        self.image = pg.Surface((50, 50), pg.SRCALPHA)
        pg.draw.circle(self.image, pg.Color('dodgerblue'), (25, 25), 25)
        self.rect = self.image.get_rect(center=pos)
        self.vel = Vector2(0, 0)
        self.pos = Vector2(pos)

    global screen


    def update(self):
        self.pos += self.vel
        self.rect.center = self.pos



def main():
    pg.init()
    screen = pg.display.set_mode((640, 480))
    # Blit objects with trails onto this surface instead of the screen.
    alpha_surf = pg.Surface(screen.get_size(), pg.SRCALPHA)
    clock = pg.time.Clock()
    global all_sprites
    all_sprites = pg.sprite.Group()
    player = Player((150, 150), all_sprites)

    # def border_control(player):
        # player = all_sprites
        # if player.pos.y >= 480:
        #     player.pos = (320,240)
        #     print("I can't exit screen, I'm afraid of heights :(")
        # if player.pos.x >= screen.get_width():
        #     player.pos = (320, 240)
        #     print("I can't exit screen, I'm afraid of the undefined x axis :(")

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_d:
                    # border_control(player)
                    player.vel.x = 5
                elif event.key == pg.K_a:
                    # border_control()
                    player.vel.x = -5
                elif event.key == pg.K_w:
                    # border_control()
                    player.vel.y = -5
                elif event.key == pg.K_s:
                    # border_control()
                    player.vel.y = 5
            elif event.type == pg.KEYUP:
                if event.key == pg.K_d and player.vel.x > 0:
                    # border_control()
                    player.vel.x = 0
                elif event.key == pg.K_a and player.vel.x < 0:
                    # border_control()
                    player.vel.x = 0
                elif event.key == pg.K_w:
                    # border_control()
                    player.vel.y = 0
                elif event.key == pg.K_s:
                    # border_control()
                    player.vel.y = 0

        # Reduce the alpha of all pixels on this surface each frame.
        # Control the fade speed with the alpha value.
        alpha_surf.fill("dodgerblue2", special_flags=pg.BLEND_RGBA_MULT)


        all_sprites.update()
        screen.fill("dodgerblue")  # Clear the screen.
        all_sprites.draw(alpha_surf)  # Draw the objects onto the alpha_surf.

        screen.blit(alpha_surf, (0, 0))  # Blit the alpha_surf onto the screen.
        pg.display.flip()
        clock.tick(60)




if __name__ == '__main__':
    main()
    pg.quit()
