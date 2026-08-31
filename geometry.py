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
              if obs[0] == "v":
                self.vertices.append(Vector4(float(obs[1]), float(obs[2]), float(obs[3]), float(obs[4])))
              elif obs[0] == "e":
                self.edges.append(Edge(int(obs[1]), int(obs[2])))
              elif obs[0] == "s":       
                self.faces.append(Face(int(obs[1]), int(obs[2]), int(obs[3])))

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

