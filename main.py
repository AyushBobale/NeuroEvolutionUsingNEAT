import pygame
import pymunk
import pymunk.pygame_util
import math

pygame.init()
WIDTH, HEIGHT = 1980,1080
window = pygame.display.set_mode((WIDTH, HEIGHT))


def draw(window, space, draw_options):
    window.fill("white")
    space.debug_draw(draw_options)
    pygame.display.update()

def pause_draw(window):
    window.fill("black")
    #space.debug_draw(draw_options)
    pygame.display.update()


def create_boundaries(space, width, height):
    rects = [
        [(width/2, height-(WIDTH/100)), (width, (WIDTH/100) * 2)],
        [(width/2, (WIDTH/100)), (width, (WIDTH/100)*2)],
        [((WIDTH/100), height/2), ((WIDTH/100)*2, height)],
        [(width-(WIDTH/100), height/2), ((WIDTH/100)*2, height)]
    ]
    for pos, size in rects:
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = pos
        shape = pymunk.Poly.create_box(body, size)
        shape.elasticity = 0.4
        shape.friction = 0.5
        space.add(body, shape)



def run(window, width, height):
    run = True
    clock = pygame.time.Clock()
    fps = 60
    dt = 1/(fps)

    space = pymunk.Space()
    space.gravity = (0, 981)

    create_boundaries(space, WIDTH, HEIGHT)
    draw_options = pymunk.pygame_util.DrawOptions(window)

    from organism import Organsim
    new_org = Organsim(space, WIDTH, HEIGHT)
    set_draw = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            new_org.sMove(event)
        space.step(dt)
        if set_draw:
            draw(window, space, draw_options)
        #print(clock.get_fps())
        clock.tick(fps)
    
    pygame.quit()


if __name__ == "__main__":
    run(window, WIDTH, HEIGHT)

