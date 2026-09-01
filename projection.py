from geometry import *
from camera import *
import math
import vector

EPSILON = 0.01

def project(camera: "Camera4D", mesh: "Mesh4D"):
    vertices_2d = []
        
    vertices_3d = []

    new_edges = []

    for i in range(len(mesh.edges)):

        current_edge = mesh.edges[i] 

        A = mesh.vertices[current_edge.a]
        B = mesh.vertices[current_edge.b]

        da = A.sub(camera.position).dot(camera.normal_vector)
        db = B.sub(camera.position).dot(camera.normal_vector)

        Anew = A
        Bnew = B

        if da <= EPSILON and db <= EPSILON:
            continue
        elif da > EPSILON and db <= EPSILON:
            t = (EPSILON - da) / (db - da)
            Bnew = A.add((B.sub(A)).multiply(t))
        elif da <= EPSILON and db > EPSILON:
            t = (EPSILON - da) / (db - da)
            Anew = A.add((B.sub(A)).multiply(t))    
        
        current_vertex = None


        new_edge_start = len(vertices_2d)


        for j in range(2):
          if j == 0:
            current_vertex = Anew
          else:    
            current_vertex = Bnew
        
          if ((current_vertex.sub(camera.position)).dot(camera.normal_vector)) > EPSILON:

            vector_coefficient_4d_projection = (camera.normal_vector.length() * camera.distance) / (current_vertex.sub(camera.position)).dot(camera.normal_vector)

            point = camera.position.add(current_vertex.sub(camera.position).multiply(vector_coefficient_4d_projection))

            vertices_3d.append(point.toVector3())

            if ((point.toVector3().sub(camera.position.toVector3())).dot(camera.normal_vector.toVector3())) > EPSILON:
                
                vector_coefficient_3d_projection = ((camera.normal_vector.toVector3()).length()*camera.distance) / (point.toVector3().sub(camera.position.toVector3())).dot(camera.normal_vector.toVector3())

                point_2d = camera.position.toVector3().add(point.toVector3().sub(camera.position.toVector3()).multiply(vector_coefficient_3d_projection))

                vertices_2d.append(point_2d.toVector2())
        
            else:
                vertices_2d.append(None)

          else:
            vertices_3d.append(None)
            vertices_2d.append(None)                

        
        new_edges.append(Edge(new_edge_start, new_edge_start+1))
            

    return Mesh2D(vertices_2d, new_edges, mesh.faces)        
