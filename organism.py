import pymunk
import pygame


"""
This is not the final type of organism
Have to make changes such that the creation of bodies and shapes is automated via loops increasing readability
create a get info function that returns  [postion, velocity, rotation, angular_velocity] of all the bodies as an array
this array can be said as the state of the organism
which can be used to train the algorithm

Note : for myself
    Try creating a simple organism with only one bar and try training feasibility 
"""
class Organsim:
    def __init__(self, space, width, height):
        self.height     = height
        self.width      = width
        self.density    = 1
        self.friction   = 3
        self.elasticity = 1
        self.pos        = (int(width*0.1), int(height*0.7))

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


        self.bodies = [self.mainbody, self.mainbody_1]          #"""Find a better implementation of this"""
        space.add(self.mainbody, self.mainbody_vis, self.mainbody_1,  self.mainbody_1vis, self.pivotjoint, self.rotatoryjoint)
    
    def getState(self):
        """
        Returns a list of tuple of [postion, velocity, rotation, angular_velocity] for each body in the organism
        """
        data = []
        for body in self.bodies:
            #print(new_org.getShapes()[0].body.rotation_vector, new_org.getShapes()[0].body.angular_velocity, new_org.getShapes()[0].body.position, new_org.getShapes()[0].body.velocity)
            data.append(body.position.x/self.width)
            data.append(body.position.y/self.height)
            data.append(body.velocity.x/self.width)
            data.append(body.velocity.y/self.height)
            data.append(body.rotation_vector.x)
            data.append(body.rotation_vector.y)
            data.append(body.angular_velocity)
            

        #scaling required
        return tuple(data)

    def getFitness(self):
        x = 0
        y = 0
        for body in self.bodies:
            x += body.position.x
            y += body.position.y
        return ((x+y)/(len(self.bodies)*2))/self.width

    def moveAI(self, ouput, force_multiplier = 1):
        force_multiplier = force_multiplier * self.height * self.width
        maxop = max(ouput)
        maxopid = ouput.index(maxop)
        if maxopid == 0:
            self.mainbody_1vis.body.apply_impulse_at_local_point((-force_multiplier, 0), (0,0))
        if maxopid == 1:
            self.mainbody_1vis.body.apply_impulse_at_local_point((0, force_multiplier), (0,0))
        if maxopid == 2:
            self.mainbody_1vis.body.apply_impulse_at_local_point((force_multiplier, 0), (0,0))
        if maxopid == 3:
            self.mainbody_1vis.body.apply_impulse_at_local_point((0, -force_multiplier), (0,0))
        if maxopid == 4:
            self.mainbody_vis.body.apply_impulse_at_local_point((-force_multiplier, 0), (0,0))
        if maxopid == 5:
            self.mainbody_vis.body.apply_impulse_at_local_point((0, force_multiplier), (0,0))
        if maxopid == 6:
            self.mainbody_vis.body.apply_impulse_at_local_point((force_multiplier, 0), (0,0))
        if maxopid == 7:
            self.mainbody_vis.body.apply_impulse_at_local_point((0, -force_multiplier), (0,0))
        
    
    def moveHuman(self, event, force_multiplier = 1):
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
            



