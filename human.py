import pymunk
import pygame

"""
Can work only in 16:9 aspect ratios

"""

class Human:
    def __init__(self, space, width, height):
        self.height         = height
        self.width          = width
        self.density        = 1
        self.friction       = 3
        self.elasticity     = 1
        self.pos            = (600, 300)
        self.size           = (100,150)
        self.thigh_size     = (0.3, 0.9)
        self.leg_size       = (0.3, 0.8)
        self.leg_pos        = 0.98      # defines how low the leg will be consequently how low the joint
        self.color          = (77, 225, 208, 100)
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
        self.mainbody_shape.mass            = self.mainbody_size[0] * self.mainbody_size[1] * self.density
        self.mainbody_shape.elasticity      = self.elasticity
        self.mainbody_shape.friction        = self.friction
        self.mainbody_shape.filter          = self.filter

        #Shape LEFT THIGH
        self.left_thigh_size                  = (int(self.size[0] * self.thigh_size[0]), int(self.size[1] * self.thigh_size[1]))
        self.left_thigh.position              = (int(self.pos[0] - self.size[0]/2 + self.left_thigh_size[0]/2), int(self.pos[1] * self.leg_pos + self.left_thigh_size[1]))
        self.left_thigh_shape                 = pymunk.Poly.create_box(self.left_thigh, self.left_thigh_size)
        self.left_thigh_shape.color           = (255,0,0,100)
        self.left_thigh_shape.mass            = self.left_thigh_size[0] * self.left_thigh_size[1] * self.density
        self.left_thigh_shape.elasticity      = self.elasticity
        self.left_thigh_shape.friction        = self.friction
        self.left_thigh_shape.filter          = self.filter

        #Shape RIGHT THIGH
        self.right_thigh_size                  = (int(self.size[0] * self.thigh_size[0]), int(self.size[1] * self.thigh_size[1]))
        self.right_thigh.position              = (int(self.pos[0] + self.size[0]/2 - self.right_thigh_size[0]/2), int(self.pos[1] * self.leg_pos + self.right_thigh_size[1]))
        self.right_thigh_shape                 = pymunk.Poly.create_box(self.right_thigh, self.right_thigh_size)
        self.right_thigh_shape.color           = (255,0,0,100)
        self.right_thigh_shape.mass            = self.right_thigh_size[0] * self.right_thigh_size[1] * self.density
        self.right_thigh_shape.elasticity      = self.elasticity
        self.right_thigh_shape.friction        = self.friction
        self.right_thigh_shape.filter          = self.filter

        #Shape LEFT LEG
        self.left_leg_size                  = (int(self.size[0] * self.leg_size[0]), int(self.size[1] * self.leg_size[1]))
        self.left_leg.position              = (int(self.pos[0] - self.size[0]/2 + self.left_leg_size[0]/2), int(self.pos[1]* self.leg_pos + self.left_thigh_size[1] * 0.9 + self.left_leg_size[1]))
        self.left_leg_shape                 = pymunk.Poly.create_box(self.left_leg, self.left_leg_size)
        self.left_leg_shape.color           = (255,255,0,100)
        self.left_leg_shape.mass            = self.left_leg_size[0] * self.left_leg_size[1] * self.density
        self.left_leg_shape.elasticity      = self.elasticity
        self.left_leg_shape.friction        = self.friction
        self.left_leg_shape.filter          = self.filter

        #Shape Right LEG
        self.right_leg_size                  = (int(self.size[0] * self.leg_size[0]), int(self.size[1] * self.leg_size[1]))
        self.right_leg.position              = (int(self.pos[0] + self.size[0]/2 - self.right_leg_size[0]/2), int(self.pos[1]* self.leg_pos + self.left_thigh_size[1] * 0.9 + self.right_leg_size[1]))
        self.right_leg_shape                 = pymunk.Poly.create_box(self.right_leg, self.right_leg_size)
        self.right_leg_shape.color           = (255,255,0,100)
        self.right_leg_shape.mass            = self.right_leg_size[0] * self.right_leg_size[1] * self.density
        self.right_leg_shape.elasticity      = self.elasticity
        self.right_leg_shape.friction        = self.friction
        self.right_leg_shape.filter          = self.filter


        #joints
        self.lt_mb_pj       = pymunk.constraints.PivotJoint(self.mainbody, self.left_thigh, (self.left_thigh.position[0] , self.left_thigh.position[1] - self.left_thigh_size[1]/2 * 1))
        self.lt_mb_rj       = pymunk.constraints.RotaryLimitJoint(self.mainbody, self.left_thigh, -1, 1)

        self.rt_mb_pj       = pymunk.constraints.PivotJoint(self.mainbody, self.right_thigh, (self.right_thigh.position[0] , self.right_thigh.position[1] - self.right_thigh_size[1]/2 * 1))
        self.rt_mb_rj       = pymunk.constraints.RotaryLimitJoint(self.mainbody, self.right_thigh, -1, 1)

        self.ll_lt_pj       = pymunk.constraints.PivotJoint(self.left_thigh, self.left_leg, (self.left_leg.position[0] , self.left_leg.position[1] - self.left_leg_size[1]/2 * 0.9))
        self.ll_lt_rj       = pymunk.constraints.RotaryLimitJoint(self.left_thigh, self.left_leg, -1, 1)

        self.rl_rt_pj       = pymunk.constraints.PivotJoint(self.right_thigh, self.right_leg, (self.right_leg.position[0] , self.right_leg.position[1] - self.right_leg_size[1]/2 * 0.9))
        self.rl_rt_rj       = pymunk.constraints.RotaryLimitJoint(self.right_thigh, self.right_leg, -1, 1)

        self.bodies = [ self.mainbody, 
                        self.head, 
                        self.left_arm, 
                        self.left_forearm, 
                        self.left_thigh, 
                        self.left_thigh,
                        self.right_arm,
                        self.right_forearm,
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
