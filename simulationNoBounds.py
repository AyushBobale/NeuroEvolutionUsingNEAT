import pygame
import pymunk
import pymunk.pygame_util
import math
from organism import Organsim
import neat

"""
This simulation wont properly scale with all resolutions
prefered aspect ration 16:9 prefered resolution 1980,1080 1270, 720
"""

def run(sim_instance):
    running  = True
    sim_instance.createBoundaries()
    new_org = Organsim(sim_instance.space, sim_instance.width, sim_instance.height)
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            #new_org.moveHuman(event)
            sim_instance.moveCamera(event)
        sim_instance.fpsCheck()
        sim_instance.draw()
        sim_instance.step()
    pygame.quit()

class SimulationNoBounds:
    def __init__(self, width, height, fps, dt=None):
        pygame.init()
        pygame.font.init()

        self.font = pygame.font.SysFont('Calibri', 15)
        
        self.width      = width
        self.height     = height
        self.window     = pygame.display.set_mode((width, height))

        self.fps        = fps
        self.run        = True
        self.dt         = 1/fps
        if dt:
            self.dt = dt
        
        self.clock      = pygame.time.Clock()

        self.space          = pymunk.Space()
        self.space.gravity  = (0, 981)

        self.camera         = [0,0]
        self.translation    = pymunk.Transform()
        self.draw_options   = pymunk.pygame_util.DrawOptions(self.window) 
        self.debug_draw     = pymunk.SpaceDebugDrawOptions()
    
    def draw(self):
        self.window.fill("white")
        self.draw_options.transform = (self.translation)
        self.space.debug_draw(self.draw_options)
        self.showMarkers()
        pygame.display.update()
    
    def step(self):
        self.space.step(self.dt)
    
    def pauseDraw(self):
        self.window.fill("black")
        pygame.display.update()
    
    def fpsCheck(self):
        self.clock.tick(self.fps)
    
    def getFps(self):
        return self.clock.get_fps()

    def createBoundaries(self):
        rects = [ 
            [( self.width/2,    self.height - 10),          (self.width * 10,            20)]
        ]
        for pos, size in rects:
            body                = pymunk.Body(body_type=pymunk.Body.STATIC)
            body.position       = pos
            shape               = pymunk.Poly.create_box(body, size)
            shape.elasticity    = 0.4
            shape.friction      = 0.5
            self.space.add(body, shape)
        
        
        self.mark_length     = 200
        marker_size     = (5, 20)
        self.text_surface = []
        for i in range(10):
            body                = pymunk.Body(body_type=pymunk.Body.STATIC)
            body.position       = (int(i*self.mark_length), self.height)
            shape               = pymunk.Poly.create_box(body, marker_size)
            shape.elasticity    = 0.4
            shape.friction      = 0.5
            self.space.add(body, shape)

            self.text_surface.append(self.font.render(str(i*self.mark_length) , False, (0, 0, 0))) 
    
    def showMarkers(self):
        for i, text_surface in enumerate(self.text_surface):
            self.window.blit(text_surface, (int(i * self.mark_length) + self.camera[0],self.height- 20 + self.camera[1]))
    
    def moveCamera(self, event):
        multiplier = 10
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.translation    = self.translation.translated(1 * multiplier, 0)
                self.camera[0] += 1 * multiplier
            if event.key == pygame.K_RIGHT:
                self.translation    = self.translation.translated(-1 * multiplier, 0)
                self.camera[0] -= 1 * multiplier
        


    def trainAI(self, networks, frames):
        frame_count = 0
        run = True
        self.createBoundaries()
        #organisms = [Organsim(self.space, self.width, self.height) for network in networks]
        """ Add the new class here """
        while run:
            if frame_count > frames:
                fitness = []
                for organism in organisms:
                    fitness.append(organism.getFitness())
                return fitness
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            
            for i, organism in enumerate(organisms):
                inputs = organism.getState()
                output = networks[i].activate(inputs)
                organism.moveAI(output, force_multiplier=0.1)

            self.step()
            self.fpsCheck()
            self.draw()
            frame_count += 1

if __name__ == "__main__":
    sim = SimulationNoBounds(1270, 720, 60)
    run(sim)