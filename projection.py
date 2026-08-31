from geometry import *
from camera import *
import math

def project(camera: "Camera4D", mesh: "Mesh4D"):
    vertices_2d = []
    vertices_3d = []
    for i in range(len(mesh.vertices)): 

        current_vertex = mesh.vertices[i]
        
        if (current_vertex.sub(camera.position)).dot(camera.normal_vector) != 0:

            vector_coefficient_4d_projection = (camera.normal_vector.length() * camera.distance) / (current_vertex.sub(camera.position)).dot(camera.normal_vector)

            point = camera.position.add(current_vertex.sub(camera.position).multiply(vector_coefficient_4d_projection))

            vertices_3d.append(point.toVector3())

            if (point.toVector3().sub(camera.position.toVector3())).dot(camera.normal_vector.toVector3()) != 0:
                
                vector_coefficient_3d_projection = ((camera.normal_vector.toVector3()).length()*camera.distance) / (point.toVector3().sub(camera.position.toVector3())).dot(camera.normal_vector.toVector3())

                point_2d = camera.position.toVector3().add(point.toVector3().sub(camera.position.toVector3()).multiply(vector_coefficient_3d_projection))

                vertices_2d.append(point_2d.toVector2())
        
            else:
                vertices_2d.append(None)  

        else:
            vertices_3d.append(None)
            vertices_2d.append(None)            

    return Mesh2D(vertices_2d, mesh.edges, mesh.faces)        