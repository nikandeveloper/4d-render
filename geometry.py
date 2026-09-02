from vector import *
from dataclasses import dataclass

@dataclass
class Mesh4D:
    vertices: list[Vector4]
    edges: list[Edge]
    faces: list[Face]

    def load_mesh(self, filename):
        with open(filename, "r") as file:
          for line in file:
            if line.strip():

              line = line.rstrip('\n')
              obs = line.split()
              values = []

              
              if obs[0] == "v":

                if len(obs) != 5:
                  raise ValueError("wrong amount of values there needs to be 4 not " + str(len(obs)-1))

                error = ""
                try:
                  for x in obs[1:]:
                    error = x
                    values.append(float(x))
                    error = ""
                    
                except ValueError:
                  raise ValueError("unacceptable value for a vertex axis, must be float: " + error)    

                
                self.vertices.append(Vector4(float(obs[1]), float(obs[2]), float(obs[3]), float(obs[4])))
              
              elif obs[0] == "e":

                if len(obs) != 3:
                  raise ValueError("wrong amount of values there needs to be 2 not " + str(len(obs)-1))

                error = ""
                try:
                  for x in obs[1:]:
                    error = x
                    values.append(int(x))
                    error = ""
                    
                except ValueError:
                  raise ValueError("unacceptable value: " + error)    


                for value in values:
                  if value < 0:
                    raise ValueError("the value for an edge must be positive. This is not acceptable: " + str(value))  
              

                self.edges.append(Edge(int(obs[1]), int(obs[2])))
              
              elif obs[0] == "s":       

                if len(obs) != 4:
                  raise ValueError("wrong amount of values there needs to be 3 not " + str(len(obs)-1))

                error = ""
                try:
                  for x in obs[1:]:
                    error = x
                    values.append(int(x))
                    error = ""
                    
                except ValueError:
                  raise ValueError("unacceptable value: " + error)    


                for value in values:
                  if value < 0:
                    raise ValueError("the value for an edge must be positive. This is not acceptable: " + str(value))  

                self.faces.append(Face(int(obs[1]), int(obs[2]), int(obs[3])))

              values.clear()  

@dataclass
class Mesh3D:
    vertices: list[Vector3]
    edges: list[Edge]
    faces: list[Face]

@dataclass
class Mesh2D:
    vertices: list[Vector2]
    edges: list[Edge]
    faces: list[Face]

@dataclass
class Edge:
    a: int
    b: int 

@dataclass
class Face:
    a: int
    b: int
    c: int

