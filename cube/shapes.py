import math


def convert_to_2d_vertices(vertices):
    return tuple((x, y) for (x, y, z) in vertices)


def convert_to_2d_center(vector):
    x, y, z = vector
    return (x, y)


def matrix_multiply_loop(old, matrix, org):
    new_x = 0
    new_y = 0
    new_z = 0

    # Translate to (0, 0 ,0)
    org_p1, org_p2, org_p3 = org
    old_x, old_y, old_z = old
    shifted = (old_x - org_p1, old_y - org_p2, old_z - org_p3)

    # Multiply the matrix with the old point vector
    for i, row in enumerate(matrix):
        for j, num in enumerate(row):
            if i == 0:
                new_x += shifted[j] * num
            elif i == 1:
                new_y += shifted[j]  * num
            elif i == 2:
                new_z += shifted[j] * num

    return (new_x + org_p1, new_y + org_p2, new_z + org_p3)


def matrix_generate(axis, ang):
    rad_ang = math.radians(ang)
    cos_ang = math.cos(rad_ang)
    sin_ang = math.sin(rad_ang)
    
    matrix = ()
    if axis ==  "x":
        matrix = ((1, 0, 0),
              (0, cos_ang, -sin_ang),
              (0, sin_ang, cos_ang))
    elif axis == "y":
        matrix = ((cos_ang, 0, sin_ang),
                  (0, 1, 0),
                  (-sin_ang, 0, cos_ang))
    elif axis == "z":
        matrix = ((cos_ang, -sin_ang, 0),
                  (sin_ang, cos_ang, 0),
                  (0, 0, 1))
    return matrix


def update_vertices(axis, vertices, ang, org) -> tuple:

    matrix = matrix_generate(axis, ang)
        
    old_p1, old_p2, old_p3 = vertices
    new_p1 = matrix_multiply_loop(old_p1, matrix, org)
    new_p2 = matrix_multiply_loop(old_p2, matrix, org)
    new_p3 = matrix_multiply_loop(old_p3, matrix, org)
    return tuple((new_p1, new_p2, new_p3))


class Triangle():
    def __init__(self, screen, vertices_3d, center_point, origin, translation_speed):
        self.screen = screen

        self.origin = origin

        self.current_vertices_3d = vertices_3d
        self.current_vertices_2d = convert_to_2d_vertices(self.current_vertices_3d)

        self.center_3d = center_point
        self.center_2d = convert_to_2d_center(self.center_3d)

        self.translation_speed = translation_speed

    def move_right(self):
        speed = self.translation_speed
        x, y, z = self.origin
        self.origin = (x + speed, y, z)

        self.current_vertices_3d = tuple((x + speed, y, z) for (x, y, z) in self.current_vertices_3d)
        self.current_vertices_2d = convert_to_2d_vertices(self.current_vertices_3d)

        x2, y2, z2 = self.center_3d
        self.center_3d = (x2 + speed, y2, z2)
        self.center_2d = (x2 + speed, y2)

    def move_left(self):
        speed = self.translation_speed
        x, y, z = self.origin
        self.origin = (x - speed, y, z)

        self.current_vertices_3d = tuple((x - speed, y, z) for (x, y, z) in self.current_vertices_3d)
        self.current_vertices_2d = convert_to_2d_vertices(self.current_vertices_3d)

        x2, y2, z2 = self.center_3d
        self.center_3d = (x2 - speed, y2, z2)
        self.center_2d = (x2 - speed, y2)
    
    def move_up(self):
        speed = self.translation_speed
        x, y, z = self.origin
        self.origin = (x, y - speed, z)

        self.current_vertices_3d = tuple((x, y - speed, z) for (x, y, z) in self.current_vertices_3d)
        self.current_vertices_2d = convert_to_2d_vertices(self.current_vertices_3d)

        x2, y2, z2 = self.center_3d
        self.center_3d = (x2, y2 - speed, z2)
        self.center_2d = (x2, y2 - speed)

    def move_down(self):
        speed = self.translation_speed
        x, y, z = self.origin
        self.origin = (x, y + speed, z)

        self.current_vertices_3d = tuple((x, y + speed, z) for (x, y, z) in self.current_vertices_3d)
        self.current_vertices_2d = convert_to_2d_vertices(self.current_vertices_3d)

        x2, y2, z2 = self.center_3d
        self.center_3d = (x2, y2 + speed, z2)
        self.center_2d = (x2, y2 + speed)

    def rotate_x(self, angle):
        self.current_vertices_3d = update_vertices("x", self.current_vertices_3d, angle, self.origin)
        self.current_vertices_2d = convert_to_2d_vertices(self.current_vertices_3d)

        matrix = matrix_generate("x", angle)
        self.center_3d = matrix_multiply_loop(self.center_3d, matrix, self.origin)
        self.center_2d = convert_to_2d_center(self.center_3d)

    def rotate_y(self, angle):
        self.current_vertices_3d = update_vertices("y", self.current_vertices_3d, angle, self.origin)
        self.current_vertices_2d = convert_to_2d_vertices(self.current_vertices_3d)

        matrix = matrix_generate("y", angle)
        self.center_3d = matrix_multiply_loop(self.center_3d, matrix, self.origin)
        self.center_2d = convert_to_2d_center(self.center_3d)


    def rotate_z(self, angle):
        self.current_vertices_3d = update_vertices("z", self.current_vertices_3d, angle, self.origin)
        self.current_vertices_2d = convert_to_2d_vertices(self.current_vertices_3d)

        matrix = matrix_generate("z", angle)
        self.center_3d = matrix_multiply_loop(self.center_3d, matrix, self.origin)
        self.center_2d = convert_to_2d_center(self.center_3d)


class Cube():
    def __init__(self, screen, translation_speed, colours,
                 x_left, x_right, x_origin,
                 y_top, y_bottom, y_origin,
                 z_front, z_back, z_origin):
        self.screen = screen
        self.translation_speed = translation_speed

        self.center_f = (x_origin, y_origin, z_front)
        self.center_r = (x_right, y_origin, z_origin)
        self.center_l = (x_left, y_origin, z_origin)
        self.center_b = (x_origin, y_origin, z_back)
        self.center_a = (x_origin, y_top, z_origin)
        self.center_u = (x_origin, y_bottom, z_origin)
        

        # VERTICES -> (point_one(x, y, z), point_two(x, y, z), point_three(x, y, z))
        # Front Bottom
        self.vertices_fb = ((x_left, y_top, z_front), 
                            (x_left, y_bottom, z_front), 
                            (x_right, y_bottom, z_front))
        # Front Top
        self.vertices_ft = ((x_left, y_top, z_front), 
                            (x_right, y_top, z_front),
                            (x_right, y_bottom, z_front))
        # Right Bottom
        self.vertices_rb = ((x_right, y_top, z_front),
                            (x_right, y_bottom, z_front),
                            (x_right, y_bottom, z_back))
        # Right Top
        self.vertices_rt = ((x_right, y_top, z_front),
                            (x_right, y_top, z_back),
                            (x_right, y_bottom, z_back))
        # Left Bottom
        self.vertices_lb = ((x_left, y_top, z_back),
                            (x_left, y_bottom, z_back),
                            (x_left, y_bottom, z_front))
        # Left Top
        self.vertices_lt = ((x_left, y_top, z_back),
                            (x_left, y_top, z_front),
                            (x_left, y_bottom, z_front))
        # Back Bottom
        self.vertices_bb = ((x_right, y_top, z_back),
                            (x_right, y_bottom, z_back), 
                            (x_left, y_bottom, z_back))
        # Back Top
        self.vertices_bt = ((x_right, y_top, z_back),
                            (x_left, y_top, z_back),
                            (x_left, y_bottom, z_back))
        # Above Bottom
        self.vertices_ab = ((x_left, y_top, z_back),
                            (x_left, y_top, z_front),
                            (x_right, y_top, z_front))
        # Above Top
        self.vertices_at = ((x_left, y_top, z_back),
                            (x_right, y_top, z_back),
                            (x_right, y_top, z_front))
        # Under Bottom
        self.vertices_ub = ((x_left, y_bottom, z_front),
                            (x_left, y_bottom, z_back),
                            (x_right, y_bottom, z_back))
        # Under Top
        self.vertices_ut = ((x_left, y_bottom, z_front),
                            (x_right, y_bottom, z_front),
                            (x_right, y_bottom, z_back))
        self.origin = (x_origin, y_origin, z_origin)
        
        t_fb = Triangle(self.screen, self.vertices_fb, self.center_f, self.origin, self.translation_speed)
        t_ft = Triangle(self.screen, self.vertices_ft, self.center_f, self.origin, self.translation_speed)
        t_rb = Triangle(self.screen, self.vertices_rb, self.center_r, self.origin, self.translation_speed)
        t_rt = Triangle(self.screen, self.vertices_rt, self.center_r, self.origin, self.translation_speed)
        t_lb = Triangle(self.screen, self.vertices_lb, self.center_l, self.origin, self.translation_speed)
        t_lt = Triangle(self.screen, self.vertices_lt, self.center_l, self.origin, self.translation_speed)
        t_bb = Triangle(self.screen, self.vertices_bb, self.center_b, self.origin, self.translation_speed)
        t_bt = Triangle(self.screen, self.vertices_bt, self.center_b, self.origin, self.translation_speed)
        t_ab = Triangle(self.screen, self.vertices_ab, self.center_a, self.origin, self.translation_speed)
        t_at = Triangle(self.screen, self.vertices_at, self.center_a, self.origin, self.translation_speed)
        t_ub = Triangle(self.screen, self.vertices_ub, self.center_u, self.origin, self.translation_speed)
        t_ut = Triangle(self.screen, self.vertices_ut, self.center_u, self.origin, self.translation_speed)

        self.triangles: list = [t_fb, t_ft, t_rb, t_rt, t_lb, t_lt, t_bb, t_bt, t_ub, t_ut, t_ab, t_at]

        self.triangle_colours: list = colours