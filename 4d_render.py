import math
import pygame

surfaces = []
edges = []
vertices_4d = []


with open("data.dots", "r") as file:
    for line in file:
      if line.strip():
        line = line.rstrip('\n')
        obs = line.split(" ")
        if obs[0] == "v":
            vertices_4d.append([float(obs[1]), float(obs[2]), float(obs[3]), float(obs[4])])
        elif obs[0] == "e":
            edges.append([int(obs[1]), int(obs[2])])
        elif obs[0] == "s":       
            surfaces.append([int(obs[1]), int(obs[2]), int(obs[3])])


def sub(a, b):
    ans = []
    for i in range(len(a)):
       ans.append(a[i]- b[i]) 
    return ans

def mul(a, c):
    ans = []
    for i in range(len(a)):
        ans.append(a[i]*c)
    return ans     

def add(a, b):
    ans = []
    for i in range(len(a)):
       ans.append(a[i] + b[i]) 
    return ans

def squeeze_3(a):
    return [a[0], a[1], a[2]]    

def squeeze_2(a):
    return [a[0], a[1]]    

def angle_add(a, b):
    a += b
    a %= 360

    return a

def dot(a, b):
    ans = 0
    for i in range(len(a)):
        ans += a[i]*b[i]
    return ans    

def vector_length(a):
    ans = 0
    for i in range(len(a)):
        ans += a[i]*a[i]
    ans = math.sqrt(ans)
    return  ans


def rot_plane(a, ngle):
    c = a[0]
    s = a[1]
    dia = math.sqrt(c*c + s*s)
    
    #rim_angle = math.degrees(math.asin(s/dia))
 
    #if pos(s) < 1 and pos(c) < 1:
     #   n_angle = rim_angle
    #elif pos(s) == 1 and pos(c) < 1:
      #  n_angle = 0
    #elif pos(s) < 1 and pos(c) == 1:
     #   n_angle = 90   
    #elif pos(s) < 1 and pos(c) > 1:
      #  n_angle = 180 - rim_angle
    #elif pos(s) == 1 and pos(c) > 1:
     #   n_angle = 180     
    #elif pos(s) > 1 and pos(c) > 1:   
     #   n_angle = 180 + rim_angle
    #elif pos(s) > 1  and pos(c) == 1:
     #   n_angle = 270
    #elif pos(s) > 1 and pos(c) < 1:
     #   n_angle = 360 - rim_angle    

    n_angle = math.degrees(math.atan2(s, c))

    n_angle = angle_add(n_angle, ngle)

    c = math.cos(math.radians(n_angle)) * dia
    s = math.sin(math.radians(n_angle)) * dia

    return (c, s)

# the reason for the rotational_planes is purely because i personally found it easier to follow what each button does

def XY(a, angle):
    v = (a[0], a[1])
    j, d = rot_plane(v, angle)
    return [j, d, a[2], a[3]]

def XZ(a, angle):
    v = (a[0], a[2])
    j, d = rot_plane(v, angle)
    return [j, a[1], d, a[3]]

def XW(a, angle):
    v = (a[0], a[3])
    j, d = rot_plane(v, angle)
    return [j, a[1], a[2], d]

def WZ(a, angle):
    v = (a[3], a[2])
    j, d = rot_plane(v, angle)
    return [a[0], a[1], d, j]

def WY(a, angle):
    v = (a[3], a[1])
    j, d = rot_plane(v, angle)
    return [a[0], d, a[2], j]

def ZY(a, angle):
    v = (a[2], a[1])
    j, d = rot_plane(v, angle)
    return [a[1], d, j, a[3]]
    
    


camera = [0, 0, 0, 0]
distance = 0.5
normal_vector = [1, 1, 1, 1]

vertices_3d = []
vertices_2d = []

rot_cam = True

changing_angle = 10

geometry_changed = True

speed = 0.3

pygame.init()

print(vertices_2d)

window = pygame.display.set_mode((1600, 900), pygame.RESIZABLE)

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            # CAMERA MOVEMENT

            if event.key == pygame.K_w:
                camera[1] += speed
            if event.key == pygame.K_s:
                camera[1] -= speed
            if event.key == pygame.K_q:
                camera[2] += speed
            if event.key == pygame.K_e:
                camera[2] -= speed
            if event.key == pygame.K_a:
                camera[0] += speed
            if event.key == pygame.K_d:
                camera[0] -= speed
            if event.key == pygame.K_z:
                camera[3] += speed
            if event.key == pygame.K_x:
                camera[3] -= speed
                print(camera)

            if event.key == pygame.K_c:
                rot_cam = not rot_cam

            # ROTATION PLANES

            if event.key == pygame.K_r:
                if rot_cam:
                    normal_vector = XY(normal_vector, changing_angle)
                else:
                  for i in range(len(vertices_4d)):   
                    vertices_4d[i] = XY(vertices_4d[i], changing_angle)
            if event.key == pygame.K_f:
                if rot_cam:
                    normal_vector = XY(normal_vector, -changing_angle)
                else:
                  for i in range(len(vertices_4d)):   
                    vertices_4d[i] = XY(vertices_4d[i], -changing_angle)    
            if event.key == pygame.K_t:
                if rot_cam:
                    normal_vector = XZ(normal_vector, changing_angle)
                else:
                  for i in range(len(vertices_4d)):   
                    vertices_4d[i] = XZ(vertices_4d[i], changing_angle)
            if event.key == pygame.K_g:
                if rot_cam:
                    normal_vector = XZ(normal_vector, -changing_angle)
                else:
                  for i in range(len(vertices_4d)):   
                    vertices_4d[i] = XZ(vertices_4d[i], -changing_angle)    
            if event.key == pygame.K_y:
                if rot_cam:
                    normal_vector = XW(normal_vector, changing_angle)
                else:
                  for i in range(len(vertices_4d)):   
                    vertices_4d[i] = XW(vertices_4d[i], changing_angle)
            if event.key == pygame.K_h:
                if rot_cam:
                    normal_vector = XW(normal_vector, -changing_angle)
                else:
                  for i in range(len(vertices_4d)):   
                    vertices_4d[i] = XW(vertices_4d[i], -changing_angle)
            if event.key == pygame.K_u:
                if rot_cam:
                    normal_vector = WZ(normal_vector, changing_angle)
                else:
                  for i in range(len(vertices_4d)):   
                    vertices_4d[i] = WZ(vertices_4d[i], changing_angle)    
            if event.key == pygame.K_j:
                if rot_cam: 
                    normal_vector = WZ(normal_vector, -changing_angle)
                else:
                  for i in range(len(vertices_4d)):   
                    vertices_4d[i] = WZ(vertices_4d[i], -changing_angle)    
            if event.key == pygame.K_i:
                if rot_cam:
                    normal_vector = WY(normal_vector, changing_angle)
                else:
                  for i in range(len(vertices_4d)):  
                    vertices_4d[i] = WY(vertices_4d[i], changing_angle)   
            if event.key == pygame.K_k:
                if rot_cam:
                    normal_vector = WY(normal_vector, -changing_angle)
                else:
                  for i in range(len(vertices_4d)):
                    vertices_4d[i] = WY(vertices_4d[i], -changing_angle)    
            if event.key == pygame.K_o:
                if rot_cam:
                    normal_vector = ZY(normal_vector, changing_angle)
                else:
                  for i in range(len(vertices_4d)):  
                    vertices_4d[i] = ZY(vertices_4d[i], changing_angle)    
            if event.key == pygame.K_l:
                if rot_cam:
                    normal_vector = ZY(normal_vector, -changing_angle)
                else:
                  for i in range(len(vertices_4d)):  
                    vertices_4d[i] = ZY(vertices_4d[i], -changing_angle)
            geometry_changed = True
    
                    

    if geometry_changed:
      
      geometry_changed = False
      vertices_2d.clear()
      vertices_3d.clear()

      for i in range(len(vertices_4d)):
      
        current_vertex = vertices_4d[i]
      
        if dot(sub(current_vertex, camera), normal_vector) != 0:
            #4D PROJECTION
            vector_coefficient_4d_projection = (vector_length(normal_vector) * distance)/dot(sub(current_vertex, camera), normal_vector)
            
            point = add(camera, mul(c=vector_coefficient_4d_projection, a=sub(current_vertex, camera)))
            
            vertices_3d.append(squeeze_3(point))
      
            if dot(sub(squeeze_3(point), squeeze_3(camera)), squeeze_3(normal_vector)) != 0:
              #3D PROJECTION
              
              vector_coefficient_3d_projection = (vector_length(squeeze_3(normal_vector)) * distance) / dot(sub(squeeze_3(point), squeeze_3(camera)), squeeze_3(normal_vector))
              
              dpoint = add(squeeze_3(camera), mul(c=vector_coefficient_3d_projection, a=sub(squeeze_3(point), squeeze_3(camera))))
              
              vertices_2d.append(squeeze_2(dpoint))
            else:
                vertices_2d.append(None)  
      
        else:
            vertices_3d.append(None)
            vertices_2d.append(None)    
    
    window.fill((0,0,0))

    #RENDERING

    for e in edges:
     if vertices_2d[e[0]] is not None and vertices_2d[e[1]] is not None:
       pygame.draw.line(window, (255, 255, 255), vertices_2d[e[0]], vertices_2d[e[1]])

    for s in surfaces:
     if vertices_2d[s[0]] is not None and (vertices_2d[s[1]] is not None and vertices_2d[s[2]] is not None):
       pygame.draw.polygon(window, (255, 255, 255), [vertices_2d[s[0]], vertices_2d[s[1]],  vertices_2d[s[2]]])


    pygame.display.flip()