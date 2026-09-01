from geometry import *
from camera import *
import math
import vector

EPSILON = 0.01

def clipping(camera, A, B):


  da = A.sub(camera.position).dot(camera.normal_vector)
  db = B.sub(camera.position).dot(camera.normal_vector)

  Anew = A
  Bnew = B

  if da <= EPSILON and db <= EPSILON:
    return None
  elif da > EPSILON and db <= EPSILON:
    t = (EPSILON - da) / (db - da)
    Bnew = A.add((B.sub(A)).multiply(t))
  elif da <= EPSILON and db > EPSILON:
    t = (EPSILON - da) / (db - da)
    Anew = A.add((B.sub(A)).multiply(t))    
        
  current_vertex = None

  return Anew, Bnew



def project_point_3dto2d(camera: "Camera4D", point: "Vector3"):
  if ((point.sub(camera.position.toVector3())).dot(camera.normal_vector.toVector3())) > EPSILON:
                
    vector_coefficient_3d_projection = ((camera.normal_vector.toVector3()).length()*camera.distance) / (point.sub(camera.position.toVector3())).dot(camera.normal_vector.toVector3())

    point_2d = camera.position.toVector3().add(point.sub(camera.position.toVector3()).multiply(vector_coefficient_3d_projection))

    return point_2d.toVector2()
        
  else:
    return None


def project_point_4dto3d(camera: "Camera4D", current_vertex: "Vector4"):
  if ((current_vertex.sub(camera.position)).dot(camera.normal_vector)) > EPSILON:

    vector_coefficient_4d_projection = (camera.normal_vector.length() * camera.distance) / (current_vertex.sub(camera.position)).dot(camera.normal_vector)

    point = camera.position.add(current_vertex.sub(camera.position).multiply(vector_coefficient_4d_projection))

    return point.toVector3()

  else:
    return None


def project(camera: "Camera4D", mesh: "Mesh4D"):

    vertices_2d = []
        
    vertices_3d = []

    new_edges = []

    for i in range(len(mesh.edges)):


        new_edge_start = len(vertices_2d)



        current_edge = mesh.edges[i]

        A = mesh.vertices[current_edge.a]
        B = mesh.vertices[current_edge.b]

        clipping_result = clipping(camera, A, B)
        
        if clipping_result is None:
          continue
        else:
          Anew, Bnew = clipping_result  




        for current_vertex in (Anew, Bnew):
                       
          point = project_point_4dto3d(camera, current_vertex)

          vertices_3d.append(point)

          if point is not None:
            d_point = project_point_3dto2d(camera, point)
          
            vertices_2d.append(d_point)     

          else:
            vertices_2d.append(None)  
        
        new_edges.append(Edge(new_edge_start, new_edge_start+1))
            

    return Mesh2D(vertices_2d, new_edges, mesh.faces)
