from dataclasses import dataclass
import math
from vector import Vector4

@dataclass(frozen=True)
class Matrix4D:
    values: list[float]

    def __mul__(self, vector: "Vector4"):
        x_row = Vector4(self.values[0], self.values[1], self.values[2], self.values[3])
        new_x = x_row.dot(vector)
        y_row = Vector4(self.values[4], self.values[5], self.values[6], self.values[7])
        new_y = y_row.dot(vector)
        z_row = Vector4(self.values[8], self.values[9], self.values[10], self.values[11])
        new_z = z_row.dot(vector)
        w_row = Vector4(self.values[12], self.values[13], self.values[14], self.values[15])
        new_w = w_row.dot(vector)

        return Vector4(new_x, new_y, new_z, new_w)


    def identity(self):
        identity_matrix = []
        for i in range(4):
            for x in range(4):
                if x == i:
                    identity_matrix.append(1)
                else:
                    identity_matrix.append(0)    
        return Matrix4D(identity_matrix)

    
    def rot_matrix(self, angle, axis_a, axis_b):
        cosinus = math.cos(math.radians(angle))
        sinus = math.sin(math.radians(angle))

        rot_matrice = self.identity().values
        for i in range(4):
            for x in range(4):
                if i == axis_a and x == axis_a:
                    rot_matrice[i*4 + x] = cosinus
                if i == axis_a and x == axis_b:
                    rot_matrice[i*4 + x] = -sinus
                if i == axis_b and x == axis_a:
                    rot_matrice[i*4 + x] = sinus
                if i == axis_b and x == axis_b:
                    rot_matrice[i*4 + x] = cosinus

        return Matrix4D(rot_matrice)                   

