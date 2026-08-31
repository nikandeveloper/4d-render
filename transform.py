from vector import *

def rot_plane(a: "Vector2", angle):
    c = a.x
    s = a.y
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

    n_angle = angle_add(n_angle, angle)

    c = math.cos(math.radians(n_angle)) * dia
    s = math.sin(math.radians(n_angle)) * dia

    return (c, s)

# the reason for the rotational_planes is purely because i personally found it easier to follow what each button does

def XY(a: "Vector4", angle: float):
    v = Vector2(a.x, a.y)
    j, d = rot_plane(v, angle)
    return Vector4(j, d, a.z, a.w)

def XZ(a: "Vector4", angle: float):
    v = Vector2(a.x, a.z)
    j, d = rot_plane(v, angle)
    return Vector4(j, a.y, d, a.w)

def XW(a: "Vector4", angle: float):
    v = Vector2(a.x, a.z)
    j, d = rot_plane(v, angle)
    return Vector4(j, a.y, a.z, d)

def WZ(a: "Vector4", angle: float):
    v = Vector2(a.z, a.w)
    j, d = rot_plane(v, angle)
    return Vector4(a.x, a.y, d, j)

def WY(a: "Vector4", angle: float):
    v = Vector2(a.w, a.y)
    j, d = rot_plane(v, angle)
    return Vector4(a.x, d, a.z, j)

def ZY(a: "Vector4", angle: float):
    v = Vector2(a.z, a.y)
    j, d = rot_plane(v, angle)
    return Vector4(a.x, d, j, a.w)


def scaled(point: "Vector2", scale: int, screen_size: (int,int)):
    return Vector2(point.x* scale * screen_size[0] /2, -point.y* scale * screen_size[1] / 2)

def angle_add(angle_a: float, angle_b: float):
    angle_a += angle_b
    angle_a %= 360

    return angle_a
