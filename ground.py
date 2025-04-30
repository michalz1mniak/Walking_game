import pygame, pymunk

class Ground():
    def __init__(self):
        self.color = (95, 99, 102)
        self.ground_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.ground_body.position = 0, 700
        self.ground_shape = pymunk.Poly.create_box(self.ground_body, (10000, 60))
        self.ground_shape.friction = 1

    def add_to_space(self, space):
        space.add(self.ground_body, self.ground_shape)

    def draw(self, screen, offset):
        vert = self.ground_shape.get_vertices()
        vert = [self.ground_body.local_to_world(v) - offset for v in vert]
        pygame.draw.polygon(screen, self.color, vert)