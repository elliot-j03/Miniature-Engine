import pygame
from shapes import Cube


pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("3D Cube Engine")
icon_surface = pygame.image.load("assets/cube_logo.png")
pygame.display.set_icon(icon_surface)
screen_center = (screen.get_width() / 2, screen.get_height() / 2)
clock = pygame.time.Clock()
running = True

# KEYBOARD TRACKER COORDS
w_key = ((1220, 10), (1200, 10), (1200, 30), (1220, 30))
s_key = ((1224, 32), (1204, 32), (1204, 52), (1224, 52))
a_key = ((1202, 32), (1182, 32), (1182, 52), (1202, 52))
d_key = ((1246, 32), (1226, 32), (1226, 52), (1246, 52))
shift_key = ((1162, 54), (1132, 54), (1132, 74), (1162, 74))
space_key = ((1270, 54), (1164, 54), (1164, 74), (1270, 74))
e_key = ((1242, 10), (1222, 10), (1222, 30), (1242, 30))
q_key = ((1198, 10), (1178, 10), (1178, 30), (1198, 30))
r_key = ((1264, 10), (1244, 10), (1244, 30), (1264, 30))
f_key = ((1268, 32), (1248, 32), (1248, 52), (1268, 52))

key_vertices: list = [w_key, s_key, a_key, d_key, shift_key, space_key, e_key, q_key, r_key, f_key]

# SHAPE DIMENSIONS
WIDTH = 200
HEIGHT = 200
TRANSLATION_SPEED = 3
ROTATION_ANGLE = 3

# STARTING COORDS CUBE ONE
xl_one = (screen.get_width()/2 - 250) - (WIDTH/2)
xr_one = (screen.get_width()/2 - 250) + (WIDTH/2)
xo_one = (screen.get_width()/2 - 250)
yt_one = screen.get_height()/2 - (HEIGHT/2)
yb_one = screen.get_height()/2 + (HEIGHT/2)
yo_one = screen.get_height()/2
zf_one = (WIDTH/2)
zb_one = -(WIDTH/2)
zo_one = 0

cols_one = ["#ffffff", "#eaeaea", 
            "#ffa6a6", "#c68787", 
            "#f0b4ff", "#f570ff",
            "#8593fc", "#373efa",
            "#fff6c1", "#ffda6b",
            "#b5ff84", "#46ff4f"]

# STARTING COORDS CUBE TWO
xl_two = (screen.get_width()/2 + 250) - (WIDTH/2)
xr_two = (screen.get_width()/2 + 250) + (WIDTH/2)
xo_two = (screen.get_width()/2 + 250)
yt_two = screen.get_height()/2 - (HEIGHT/2)
yb_two = screen.get_height()/2 + (HEIGHT/2)
yo_two = screen.get_height()/2
zf_two = (WIDTH/2)
zb_two = -(WIDTH/2)
zo_two = 0

cols_two = ["#ffffff" for _ in range(12)]

c_fill = Cube(screen, TRANSLATION_SPEED, cols_one, xl_one, xr_one, xo_one, yt_one, yb_one, yo_one, zf_one, zb_one, zo_one)
c_wire = Cube(screen, TRANSLATION_SPEED, cols_two, xl_two, xr_two, xo_two, yt_two, yb_two, yo_two, zf_two, zb_two, zo_two)


def render_order(triangles, cols) -> tuple:
    z_points = []

    for t in triangles:
        z_points.append(t.center_3d[2])
    
    sorted_zp = sorted(enumerate(z_points), key=lambda x: x[1])
    sorted_triangles = [triangles[i] for i, value in sorted_zp]
    sorted_cols = [cols[i] for i, value in sorted_zp]

    return sorted_triangles, sorted_cols


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")

    # Key Tracker
    for key in key_vertices:
        pygame.draw.polygon(screen, "#454545", key)

    # Cube Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        pygame.draw.polygon(screen, "#a7c1ff", w_key)
        for t in c_fill.triangles:
            t.move_up()
        for t in c_wire.triangles:
            t.move_up()
    if keys[pygame.K_s]:
        pygame.draw.polygon(screen, "#a7c1ff", s_key)
        for t in c_fill.triangles:
            t.move_down()
        for t in c_wire.triangles:
            t.move_down()
    if keys[pygame.K_a]:
        pygame.draw.polygon(screen, "#a7c1ff", a_key)
        for t in c_fill.triangles:
            t.move_left()
        for t in c_wire.triangles:
            t.move_left()
    if keys[pygame.K_d]:
        pygame.draw.polygon(screen, "#a7c1ff", d_key)
        for t in c_fill.triangles:
            t.move_right()
        for t in c_wire.triangles:
            t.move_right()
    if keys[pygame.K_LSHIFT]:
        pygame.draw.polygon(screen, "#ffffff", shift_key)
        for t in c_fill.triangles:
            t.rotate_x(-ROTATION_ANGLE)
        for t in c_wire.triangles:
            t.rotate_x(-ROTATION_ANGLE)
    if keys[pygame.K_SPACE]:
        pygame.draw.polygon(screen, "#ffffff", space_key)
        for t in c_fill.triangles:
            t.rotate_x(ROTATION_ANGLE)
        for t in c_wire.triangles:
            t.rotate_x(ROTATION_ANGLE)
    if keys[pygame.K_e]:
        pygame.draw.polygon(screen, "#ffffff", e_key)
        for t in c_fill.triangles:
            t.rotate_y(ROTATION_ANGLE)
        for t in c_wire.triangles:
            t.rotate_y(ROTATION_ANGLE)
    if keys[pygame.K_q]:
        pygame.draw.polygon(screen, "#ffffff", q_key)
        for t in c_fill.triangles:
            t.rotate_y(-ROTATION_ANGLE)
        for t in c_wire.triangles:
            t.rotate_y(-ROTATION_ANGLE)
    if keys[pygame.K_r]:
        pygame.draw.polygon(screen, "#ffffff", r_key)
        for t in c_fill.triangles:
            t.rotate_z(-ROTATION_ANGLE)
        for t in c_wire.triangles:
            t.rotate_z(-ROTATION_ANGLE)
    if keys[pygame.K_f]:
        pygame.draw.polygon(screen, "#ffffff", f_key)
        for t in c_fill.triangles:
            t.rotate_z(ROTATION_ANGLE)
        for t in c_wire.triangles:
            t.rotate_z(ROTATION_ANGLE)

    # Cube Rendering
    fill_t_order, fill_cols_order = render_order(c_fill.triangles, c_fill.triangle_colours)
    wire_t_order, wire_cols_order = render_order(c_wire.triangles, c_wire.triangle_colours)

    for i, t in enumerate(fill_t_order):
        pygame.draw.polygon(screen, fill_cols_order[i], t.current_vertices_2d)
    for i, t in enumerate(wire_t_order):
        pygame.draw.polygon(screen, wire_cols_order[i], t.current_vertices_2d, width=2)
        pygame.draw.circle(screen, "red", t.center_2d, 5)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

