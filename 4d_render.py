import math
import pygame
from camera import * 
from vector import *
from geometry import *
import transform 
from projection import *


mesh_4d = Mesh4D([], [], [])
mesh_4d.load_mesh("data.dots")

camera = Camera4D(Vector4(0,0,0,0), Vector4(1, 1, 1, 1), 5)

mesh_2d = Mesh2D([], [], [])

screen_size = (1600, 900)

rot_cam = True

changing_angle = 10

geometry_changed = True



speed = 0.05


speed_up = Vector4(0, speed, 0, 0)
speed_down = Vector4(0, -speed, 0, 0)
speed_right = Vector4(speed, 0, 0, 0)
speed_left = Vector4(-speed, 0, 0, 0)
speed_forward = Vector4(0, 0, speed, 0)
speed_backward = Vector4(0, 0, -speed, 0)
speed_w_p = Vector4(0, 0, 0, speed)
speed_w_m = Vector4(0, 0, 0, -speed)


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

            if event.key == pygame.K_w:
                camera = camera.move(speed_up)
            if event.key == pygame.K_s:
                camera = camera.move(speed_down)
            if event.key == pygame.K_q:
                camera = camera.move(speed_backward)
            if event.key == pygame.K_e:
                camera = camera.move(speed_forward)
            if event.key == pygame.K_a:
                camera = camera.move(speed_left)
            if event.key == pygame.K_d:
                camera = camera.move(speed_right)
            if event.key == pygame.K_z:
                camera = camera.move(speed_w_p)
            if event.key == pygame.K_x:
                camera = camera.move(speed_w_m)

            if event.key == pygame.K_c:
                rot_cam = not rot_cam

            # ROTATION PLANES

            if event.key == pygame.K_r:
                if rot_cam:
                    camera = camera.rotate("XY", changing_angle)
                else:
                  for i in range(len(mesh_4d.vertices)):   
                    mesh_4d.vertices[i] = transform.XY(mesh_4d.vertices[i], changing_angle)
            if event.key == pygame.K_f:
                if rot_cam:
                    camera = camera.rotate("XY", -changing_angle)
                else:
                  for i in range(len(mesh_4d.vertices)):   
                    mesh_4d.vertices[i] = transform.XY(mesh_4d.vertices[i], -changing_angle)    
            if event.key == pygame.K_t:
                if rot_cam:
                    camera = camera.rotate("XZ", changing_angle)
                else:
                  for i in range(len(mesh_4d.vertices)):   
                    mesh_4d.vertices[i] = transform.XZ(mesh_4d.vertices[i], changing_angle)
            if event.key == pygame.K_g:
                if rot_cam:
                    camera = camera.rotate("XZ", -changing_angle)
                else:
                  for i in range(len(mesh_4d.vertices)):   
                    mesh_4d.vertices[i] = transform.XZ(mesh_4d.vertices[i], -changing_angle)    
            if event.key == pygame.K_y:
                if rot_cam:
                    camera = camera.rotate("XW", changing_angle)
                else:
                  for i in range(len(mesh_4d.vertices)):   
                    mesh_4d.vertices[i] = transform.XW(mesh_4d.vertices[i], changing_angle)
            if event.key == pygame.K_h:
                if rot_cam:
                    camera = camera.rotate("XW", -changing_angle)
                else:
                  for i in range(len(mesh_4d.vertices)):   
                    mesh_4d.vertices[i] = transform.XW(mesh_4d.vertices[i], -changing_angle)
            if event.key == pygame.K_u:
                if rot_cam:
                    camera = camera.rotate("WZ", changing_angle)
                else:
                  for i in range(len(mesh_4d.vertices)):   
                    mesh_4d.vertices[i] = transform.WZ(mesh_4d.vertices[i], changing_angle)    
            if event.key == pygame.K_j:
                if rot_cam: 
                    camera = camera.rotate("WZ", -changing_angle)
                else:
                  for i in range(len(mesh_4d.vertices)):   
                    mesh_4d.vertices[i] = transform.WZ(mesh_4d.vertices[i], -changing_angle)    
            if event.key == pygame.K_i:
                if rot_cam:
                    camera = camera.rotate("WY", changing_angle)
                else:
                  for i in range(len(mesh_4d.vertices)):  
                    mesh_4d.vertices[i] = transform.WY(mesh_4d.vertices[i], changing_angle)   
            if event.key == pygame.K_k:
                if rot_cam:
                    camera = camera.rotate("WY", -changing_angle)
                else:
                  for i in range(len(mesh_4d.vertices)):
                    mesh_4d.vertices[i] = transform.WY(mesh_4d.vertices[i], -changing_angle)    
            if event.key == pygame.K_o:
                if rot_cam:
                    camera = camera.rotate("ZY", changing_angle)
                else:
                  for i in range(len(mesh_4d.vertices)):  
                    mesh_4d.vertices[i] = transform.ZY(mesh_4d.vertices[i], changing_angle)    
            if event.key == pygame.K_l:
                if rot_cam:
                    camera = camera.rotate("ZY", -changing_angle)
                else:
                  for i in range(len(mesh_4d.vertices)):  
                    mesh_4d.vertices[i] = transform.ZY(mesh_4d.vertices[i], -changing_angle)
            geometry_changed = True
    
    
    
    window.fill((0,0,0))
    if geometry_changed:
        mesh_2d = project(camera, mesh_4d)
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
