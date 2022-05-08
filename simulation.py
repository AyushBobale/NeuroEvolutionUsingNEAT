import pygame
import pymunk
import pymunk.pygame_util
import math
from organism import Organsim


class Simulation:
    def __init__(self, width, height, fps):
        pygame.init()
        
        self.width      = width
        self.height     = height
        self.window     = pygame.display.set_mode((width, height))

        self.fps        = fps
        self.run        = True
        self.dt         = 1/fps
        self.clock      = pygame.time.Clock()

        self.space          = pymunk.Space()
        self.space.gravity  = (0, 981)
        self.draw_options   = pymunk.pygame_util.DrawOptions(self.window) 

        
    
    def draw(self):
        self.window.fill("white")
        self.space.debug_draw(self.draw_options)
        pygame.display.update()
    
    def step(self):
        self.space.step(self.dt)
    
    def pauseDraw(self):
        self.window.fill("black")
        pygame.display.update()
    
    def createBoundaries(self):
        rects = [
            [( self.width/2,    self.height-(self.width/100)),          (self.width,            (self.width/100) * 2)],
            [( self.width/2,    (self.width/100)),                      (self.width,            (self.width/100)*2)],
            [((self.width/100), self.height/2),                         ((self.width/100)*2,    self.height)],
            [( self.width -     (self.width/100), self.height/2),       ((self.width/100)*2,    self.height)]
        ]
        for pos, size in rects:
            body                = pymunk.Body(body_type=pymunk.Body.STATIC)
            body.position       = pos
            shape               = pymunk.Poly.create_box(body, size)
            shape.elasticity    = 0.4
            shape.friction      = 0.5
            self.space.add(body, shape)

    def fpsCheck(self):
        self.clock.tick(self.fps)
    
    def getFps(self):
        return self.clock.get_fps()


def run(sim_instance):
    running  = True
    sim_instance.createBoundaries()
    new_org = Organsim(sim.space, sim.width, sim.height)
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        sim.fpsCheck()
        sim_instance.draw()
        sim.step()
    pygame.quit()

if __name__ == "__main__":
    sim = Simulation(1000, 800, 60)
    run(sim)

            