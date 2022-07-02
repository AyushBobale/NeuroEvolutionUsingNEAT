import pygame
import pymunk
import pymunk.pygame_util
import math
import neat
import os
import sys
sys.path.insert(0, 'C:\\Users\\Ayush\\Documents\\Documents folder\\NeuroEvolutionUsingNEAT\\')

from organism import Organsim
from human import Human
from bipedal import Bipedal


class SimulationDistributed:
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
        self.camerasensi    = 10
        self.left           = False
        self.right          = False
        self.translation    = pymunk.Transform()
        self.draw_options   = pymunk.pygame_util.DrawOptions(self.window) 
        self.debug_draw     = pymunk.SpaceDebugDrawOptions()

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

    
    def draw(self):
        
        if self.left:
            self.translation    = self.translation.translated(self.camerasensi, 0)
            self.camera[0] += self.camerasensi
        if self.right:
            self.translation    = self.translation.translated(-self.camerasensi, 0)
            self.camera[0] -=self.camerasensi

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
        n = int((self.width * 10)/ 200)
        for i in range(n):
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.left = True
            if event.key == pygame.K_RIGHT:
                self.right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.left = False
            if event.key == pygame.K_RIGHT:
                self.right = False
