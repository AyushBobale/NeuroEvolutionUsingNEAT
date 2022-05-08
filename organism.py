import pymunk
import pygame

class Organsim:
    def __init__(self, space, width, height):
        self.height     = height
        self.width      = width
        self.density    = 1
        self.friction   = 1
        self.elasticity = 1
        self.pos        = (int(width*0.5), int(height*0.5))

        self.mainbody           = pymunk.Body()
        self.mainbody.position  = self.pos

        self.size                       = (int(width/50), int(height/4))
        self.mainbody_vis               = pymunk.Poly.create_box(self.mainbody, self.size)
        self.mainbody_vis.color         = (255,255,0,100)
        self.mainbody_vis.mass          = self.size[0] * self.size[1] * self. density
        self.mainbody_vis.elasticity    = self.elasticity
        self.mainbody_vis.friction      = self.friction
        self.mainbody_vis.filter       = pymunk.ShapeFilter(1)


        self.mainbody_1           = pymunk.Body()
        self.mainbody_1.position  = self.pos

        self.size                       = (int(width/50), int(height/4))
        self.mainbody_1vis              = pymunk.Poly.create_box(self.mainbody_1, self.size)
        self.mainbody_1vis.color        = (0,255, 255,100)
        self.mainbody_1vis.mass         = self.size[0] * self.size[1] * self. density
        self.mainbody_1vis.elasticity   = self.elasticity
        self.mainbody_1vis.friction     = self.friction
        self.mainbody_1vis.filter       = pymunk.ShapeFilter(1)

        y_offset = self.size[1]/2 - 10
        self.pivotjoint      = pymunk.constraints.PivotJoint(self.mainbody, self.mainbody_1, (self.pos[0] ,self.pos[1] - y_offset) )
        self.rotatoryjoint   = pymunk.constraints.RotaryLimitJoint(self.mainbody, self.mainbody_1, 0.17, 1.5)

        space.add(self.mainbody, self.mainbody_vis, self.mainbody_1,  self.mainbody_1vis, self.pivotjoint, self.rotatoryjoint)
    
    def getShapes(self):
        return self.mainbody_vis
    
    def move(self, pressed, force_multiplier = 1):
        force_multiplier = force_multiplier * self.height * self.width
        if pressed == 'A':
            self.mainbody_1vis.body.apply_impulse_at_local_point((-force_multiplier, 0), (0,0))
        if pressed == 'S':
            self.mainbody_1vis.body.apply_impulse_at_local_point((0, force_multiplier), (0,0))
        if pressed == 'D':
            self.mainbody_1vis.body.apply_impulse_at_local_point((force_multiplier, 0), (0,0))
        if pressed == 'W':
            self.mainbody_1vis.body.apply_impulse_at_local_point((0, -force_multiplier), (0,0))
    
        if pressed == 'left':
            self.mainbody_vis.body.apply_impulse_at_local_point((-force_multiplier, 0), (0,0))
        if pressed == 'down':
            self.mainbody_vis.body.apply_impulse_at_local_point((0, force_multiplier), (0,0))
        if pressed == 'right':
            self.mainbody_vis.body.apply_impulse_at_local_point((force_multiplier, 0), (0,0))
        if pressed == 'up':
            self.mainbody_vis.body.apply_impulse_at_local_point((0, -force_multiplier), (0,0))
    
    def sMove(self, event, force_multiplier = 1):
        force_multiplier = force_multiplier * self.height * self.width
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.mainbody_1vis.body.apply_impulse_at_local_point((-force_multiplier, 0), (0,0))
            if event.key == pygame.K_s:
                self.mainbody_1vis.body.apply_impulse_at_local_point((0, force_multiplier), (0,0))
            if event.key == pygame.K_d:
                self.mainbody_1vis.body.apply_impulse_at_local_point((force_multiplier, 0), (0,0))
            if event.key == pygame.K_w:
                self.mainbody_1vis.body.apply_impulse_at_local_point((0, -force_multiplier), (0,0))

            if event.key == pygame.K_LEFT:
                self.mainbody_vis.body.apply_impulse_at_local_point((-force_multiplier, 0), (0,0))
            if event.key == pygame.K_DOWN:
                self.mainbody_vis.body.apply_impulse_at_local_point((0, force_multiplier), (0,0))
            if event.key == pygame.K_RIGHT:
                self.mainbody_vis.body.apply_impulse_at_local_point((force_multiplier, 0), (0,0))
            if event.key == pygame.K_UP:
                self.mainbody_vis.body.apply_impulse_at_local_point((0, -force_multiplier), (0,0))
            



