import pymunk
import pygame

"""
Can work only in 16:9 aspect ratios

"""

class Bipedal:
    def __init__(self, space, width, height):
        """
        Moves : for mannual input
        A: left thigh left side     D: left thigh right side
        Z: left leg left side       C: left leg right side

        G: right thigh left side     J: right thigh right side
        B: right leg left side       M: right leg right side
        """
        self.height         = height
        self.width          = width
        self.density        = 1
        self.friction       = 3
        self.elasticity     = 1
        #==========================================================================
        #control panel make usi for custom creature where the required parameters can be changed
        self.pos            = (200, 300)
        self.size           = (250, 150)
        self.thigh_size     = (0.15, 0.6)
        self.leg_size       = (0.15, 0.6)
        self.leg_pos        = 0.98      # defines how low the leg will be consequently how low the joint
        self.color          = (77, 225, 208, 100) #make colors derived that parts inherit colors
        self.thigh_color    = (int(self.color[0] * 0.9), int(self.color[1] * 0.9), int(self.color[2] * 0.9), 100)
        self.leg_color    = (int(self.color[0] * 0.7), int(self.color[1] * 0.7), int(self.color[2] * 0.7), 100)
        #==========================================================================
        self.filter         = pymunk.ShapeFilter(1)
        """
        height scaling only for better scaling
        """
        #Bodies
        self.mainbody           = pymunk.Body()

        self.head               = pymunk.Body()

        self.left_arm           = pymunk.Body()
        self.left_forearm       = pymunk.Body()
        self.left_thigh         = pymunk.Body()
        self.left_leg           = pymunk.Body()

        self.right_arm          = pymunk.Body()
        self.right_forearm      = pymunk.Body()
        self.right_thigh        = pymunk.Body()
        self.right_leg          = pymunk.Body()

        # Positions
        self.mainbody.position      = self.pos
        # Shapes
        self.mainbody_size                  = self.size  #---------------------------------------Imp global size all sizes are dervied from this size
        self.mainbody_shape                 = pymunk.Poly.create_box(self.mainbody, self.mainbody_size)
        self.mainbody_shape.color           = self.color
        self.mainbody_shape.mass            = self.mainbody_size[0] * self.mainbody_size[1] * self.density + 5000
        self.mainbody_shape.elasticity      = self.elasticity
        self.mainbody_shape.friction        = self.friction
        self.mainbody_shape.filter          = self.filter

        #Shape LEFT THIGH
        self.left_thigh_size                  = (int(self.size[0] * self.thigh_size[0]), int(self.size[1] * self.thigh_size[1]))
        self.left_thigh.position              = (int(self.pos[0] - self.size[0]/2 + self.left_thigh_size[0]/2), int(self.pos[1] * self.leg_pos + self.left_thigh_size[1]))
        self.left_thigh_shape                 = pymunk.Poly.create_box(self.left_thigh, self.left_thigh_size)
        self.left_thigh_shape.color           = self.thigh_color
        self.left_thigh_shape.mass            = self.left_thigh_size[0] * self.left_thigh_size[1] * self.density
        self.left_thigh_shape.elasticity      = self.elasticity
        self.left_thigh_shape.friction        = self.friction
        self.left_thigh_shape.filter          = self.filter

        #Shape RIGHT THIGH
        self.right_thigh_size                  = (int(self.size[0] * self.thigh_size[0]), int(self.size[1] * self.thigh_size[1]))
        self.right_thigh.position              = (int(self.pos[0] + self.size[0]/2 - self.right_thigh_size[0]/2), int(self.pos[1] * self.leg_pos + self.right_thigh_size[1]))
        self.right_thigh_shape                 = pymunk.Poly.create_box(self.right_thigh, self.right_thigh_size)
        self.right_thigh_shape.color           = self.thigh_color
        self.right_thigh_shape.mass            = self.right_thigh_size[0] * self.right_thigh_size[1] * self.density
        self.right_thigh_shape.elasticity      = self.elasticity
        self.right_thigh_shape.friction        = self.friction
        self.right_thigh_shape.filter          = self.filter

        #Shape LEFT LEG
        self.left_leg_size                  = (int(self.size[0] * self.leg_size[0]), int(self.size[1] * self.leg_size[1]))
        self.left_leg.position              = (int(self.pos[0] - self.size[0]/2 + self.left_leg_size[0]/2), int(self.pos[1]* self.leg_pos + self.left_thigh_size[1] * 0.9 + self.left_leg_size[1]))
        self.left_leg_shape                 = pymunk.Poly.create_box(self.left_leg, self.left_leg_size)
        self.left_leg_shape.color           = self.leg_color
        self.left_leg_shape.mass            = self.left_leg_size[0] * self.left_leg_size[1] * self.density
        self.left_leg_shape.elasticity      = self.elasticity
        self.left_leg_shape.friction        = self.friction
        self.left_leg_shape.filter          = self.filter

        #Shape Right LEG
        self.right_leg_size                  = (int(self.size[0] * self.leg_size[0]), int(self.size[1] * self.leg_size[1]))
        self.right_leg.position              = (int(self.pos[0] + self.size[0]/2 - self.right_leg_size[0]/2), int(self.pos[1]* self.leg_pos + self.left_thigh_size[1] * 0.9 + self.right_leg_size[1]))
        self.right_leg_shape                 = pymunk.Poly.create_box(self.right_leg, self.right_leg_size)
        self.right_leg_shape.color           = self.leg_color
        self.right_leg_shape.mass            = self.right_leg_size[0] * self.right_leg_size[1] * self.density
        self.right_leg_shape.elasticity      = self.elasticity
        self.right_leg_shape.friction        = self.friction
        self.right_leg_shape.filter          = self.filter




        #joints
        rotation_limit      = 0.9
        self.lt_mb_pj       = pymunk.constraints.PivotJoint(self.mainbody, self.left_thigh, (self.left_thigh.position[0] , self.left_thigh.position[1] - self.left_thigh_size[1]/2 * 1))
        self.lt_mb_rj       = pymunk.constraints.RotaryLimitJoint(self.mainbody, self.left_thigh, -rotation_limit, rotation_limit)

        self.rt_mb_pj       = pymunk.constraints.PivotJoint(self.mainbody, self.right_thigh, (self.right_thigh.position[0] , self.right_thigh.position[1] - self.right_thigh_size[1]/2 * 1))
        self.rt_mb_rj       = pymunk.constraints.RotaryLimitJoint(self.mainbody, self.right_thigh, -rotation_limit, rotation_limit)

        self.ll_lt_pj       = pymunk.constraints.PivotJoint(self.left_thigh, self.left_leg, (self.left_leg.position[0] , self.left_leg.position[1] - self.left_leg_size[1]/2 * 0.9))
        self.ll_lt_rj       = pymunk.constraints.RotaryLimitJoint(self.left_thigh, self.left_leg, -rotation_limit, rotation_limit)

        self.rl_rt_pj       = pymunk.constraints.PivotJoint(self.right_thigh, self.right_leg, (self.right_leg.position[0] , self.right_leg.position[1] - self.right_leg_size[1]/2 * 0.9))
        self.rl_rt_rj       = pymunk.constraints.RotaryLimitJoint(self.right_thigh, self.right_leg, -rotation_limit, rotation_limit)

        self.bodies = [ self.mainbody, 
                        self.left_thigh, 
                        self.left_leg,
                        self.right_thigh,
                        self.right_leg]
        
        space.add(  self.mainbody,
                    self.mainbody_shape,
                    self.left_thigh,
                    self.left_thigh_shape,
                    self.lt_mb_pj,
                    self.lt_mb_rj,
                    self.right_thigh,
                    self.right_thigh_shape,
                    self.rt_mb_pj,
                    self.rt_mb_rj,
                    self.left_leg,
                    self.left_leg_shape,
                    self.ll_lt_pj,
                    self.ll_lt_rj,
                    self.right_leg,
                    self.right_leg_shape,
                    self.rl_rt_pj,
                    self.rl_rt_rj)
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
        return data

    def getFitness(self):
        x = 0
        y = 0
        for body in self.bodies:
            x += body.position.x
            y += body.position.y
        return ((x+y)/(len(self.bodies)*2))/self.width

    def moveHuman(self, event, force_multiplier=1):
        """
        Moves : for mannual input
        A: left thigh left side     D: left thigh right side
        Z: left leg left side       C: left leg right side

        G: right thigh left side     J: right thigh right side
        B: right leg left side       M: right leg right side
        """
        force_multiplier = force_multiplier * self.height * self.width
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.left_thigh_shape.body.apply_impulse_at_local_point((-force_multiplier, 0), (0,0))
            if event.key == pygame.K_d:
                self.left_thigh_shape.body.apply_impulse_at_local_point((force_multiplier, 0), (0,0))
            if event.key == pygame.K_z:
                self.left_leg_shape.body.apply_impulse_at_local_point((-force_multiplier, 0), (0,0))
            if event.key == pygame.K_c:
                self.left_leg_shape.body.apply_impulse_at_local_point((force_multiplier, 0), (0,0))

            if event.key == pygame.K_g:
                self.right_thigh_shape.body.apply_impulse_at_local_point((-force_multiplier, 0), (0,0))
            if event.key == pygame.K_j:
                self.right_thigh_shape.body.apply_impulse_at_local_point((force_multiplier, 0), (0,0))
            if event.key == pygame.K_b:
                self.right_leg_shape.body.apply_impulse_at_local_point((-force_multiplier, 0), (0,0))
            if event.key == pygame.K_m:
                self.right_leg_shape.body.apply_impulse_at_local_point((force_multiplier, 0), (0,0))
        
    
    def moveAI(self, ouput, force_multiplier = 1):
        force_multiplier = force_multiplier * self.height * self.width
        maxop = max(ouput)
        maxopid = ouput.index(maxop)
        if maxopid == 0:
            self.left_thigh_shape.body.apply_impulse_at_local_point((-force_multiplier, 0), (0,0))
        if maxopid == 1:
            self.left_thigh_shape.body.apply_impulse_at_local_point((force_multiplier, 0), (0,0))
        if maxopid == 2:
            self.left_leg_shape.body.apply_impulse_at_local_point((-force_multiplier, 0), (0,0))
        if maxopid == 3:
            self.left_leg_shape.body.apply_impulse_at_local_point((force_multiplier, 0), (0,0))

        if maxopid == 4:
            self.right_thigh_shape.body.apply_impulse_at_local_point((-force_multiplier, 0), (0,0))
        if maxopid == 5:
            self.right_thigh_shape.body.apply_impulse_at_local_point((force_multiplier, 0), (0,0))
        if maxopid == 6:
            self.right_leg_shape.body.apply_impulse_at_local_point((-force_multiplier, 0), (0,0))
        if maxopid == 7:
            self.right_leg_shape.body.apply_impulse_at_local_point((force_multiplier, 0), (0,0))

