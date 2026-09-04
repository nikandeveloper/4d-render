import math
import pygame
import camera
import vector
import geometry
import transform 
import projection
import matrix


mesh_4d = geometry.Mesh4D([], [], [])
mesh_4d.load_mesh("data.dots")

camera = camera.Camera4D(vector.Vector4(0,0,0,0), vector.Vector4(1, 1, 1, 1), 5)

mesh_2d = geometry.Mesh2D([], [], [])

screen_size = (1600, 900)

rot_cam = True

changing_angle = 10

geometry_changed = True



speed = 0.05


speed_up = vector.Vector4(0, -speed, 0, 0)
speed_down = vector.Vector4(0, speed, 0, 0)
speed_right = vector.Vector4(speed, 0, 0, 0)
speed_left = vector.Vector4(-speed, 0, 0, 0)
speed_forward = vector.Vector4(0, 0, speed, 0)
speed_backward = vector.Vector4(0, 0, -speed, 0)
speed_w_p = vector.Vector4(0, 0, 0, speed)
speed_w_m = vector.Vector4(0, 0, 0, -speed)


rotation_map_old = {
    pygame.K_r: ("XY", changing_angle),
    pygame.K_f: ("XY", -changing_angle),
    pygame.K_t: ("XZ", changing_angle),
    pygame.K_g: ("XZ", -changing_angle),
    pygame.K_y: ("XW", changing_angle),
    pygame.K_h: ("XW", -changing_angle),
    pygame.K_u: ("WZ", changing_angle),
    pygame.K_j: ("WZ", -changing_angle),
    pygame.K_i: ("WY", changing_angle),
    pygame.K_k: ("WY", -changing_angle),
    pygame.K_o: ("ZY", changing_angle),
    pygame.K_l: ("ZY", -changing_angle)
}

rotation_map_new = {
    pygame.K_r: matrix.rot_matrix(changing_angle, 0, 1),
    pygame.K_f: matrix.rot_matrix(-changing_angle, 0, 1),
    pygame.K_t: matrix.rot_matrix(changing_angle, 0, 2),
    pygame.K_g: matrix.rot_matrix(-changing_angle, 0, 2),
    pygame.K_y: matrix.rot_matrix(changing_angle, 0, 3),
    pygame.K_h: matrix.rot_matrix(-changing_angle, 0, 3),
    pygame.K_u: matrix.rot_matrix(changing_angle, 2, 3),
    pygame.K_j: matrix.rot_matrix(-changing_angle, 2, 3),
    pygame.K_i: matrix.rot_matrix(changing_angle, 1, 3),
    pygame.K_k: matrix.rot_matrix(-changing_angle, 1, 3),
    pygame.K_o: matrix.rot_matrix(changing_angle, 1, 2),
    pygame.K_l: matrix.rot_matrix(-changing_angle, 1, 2)
}


movement_map = {
    pygame.K_w: speed_up,
    pygame.K_s: speed_down,
    pygame.K_q: speed_backward,
    pygame.K_e: speed_forward,
    pygame.K_a: speed_left,
    pygame.K_d: speed_right,
    pygame.K_z: speed_w_p,
    pygame.K_x: speed_w_m
}

scale = 0.1

pygame.init()

window = pygame.display.set_mode(screen_size, pygame.RESIZABLE)

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            # CAMERA MOVEMENT

            if event.key in movement_map:
                speed_oriens = movement_map[event.key]
                camera = camera.move(speed_oriens)
                geometry_changed = True
    

            if event.key == pygame.K_c:
                rot_cam = not rot_cam

            # ROTATION PLANES

            if event.key in rotation_map_new:
                rotation_matrix = rotation_map_new[event.key]

                if rot_cam:
                    camera = camera.rotate(rotation_matrix)
                else:
                  for i in range(len(mesh_4d.vertices)):   
                    mesh_4d.vertices[i] = rotation_matrix * mesh_4d.vertices[i]
            
                geometry_changed = True
    
    
    
    window.fill((0,0,0))
    if geometry_changed:
        mesh_2d = projection.project(camera, mesh_4d)
        geometry_changed = False

    vertices_2d = mesh_2d.vertices

    edges = mesh_2d.edges
    faces = mesh_2d.faces

    #RENDERING

    for e in edges:
     if vertices_2d[e.a] is not None and vertices_2d[e.b] is not None:
       start_pos = transform.scaled(vertices_2d[e.a], scale, window.get_size()).toTuple()
       end_pos = transform.scaled(vertices_2d[e.b], scale, window.get_size()).toTuple()
       pygame.draw.line(window, (255, 255, 255), start_pos, end_pos)

    for s in faces:
     if vertices_2d[s.a] is not None and (vertices_2d[s.b] is not None and vertices_2d[s.c] is not None):
       pygame.draw.polygon(window, (255, 255, 255), [vertices_2d[s.a], vertices_2d[s.b],  vertices_2d[s.c]])


    pygame.display.flip()
