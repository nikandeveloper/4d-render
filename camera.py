from vector import *
from dataclasses import dataclass

@dataclass
class Camera4D:
    position: Vector4
    normal_vector: Vector4
    distance: float

    def move(self, speed: Vector4):
        return Camera4D(self.position.add(speed), self.normal_vector, self.distance)

    def rotate(self, plane: string, angle):
        if plane == "XY":
            rot_result = XY(normal_vector, angle)
        elif plane == "XZ":
            rot_result = XZ(normal_vector, angle)
        elif plane == "XW":
            rot_result = XW(normal_vector, angle)
        elif plane == "WZ":
            rot_result = WZ(normal_vector, angle)
        elif plane == "WY":
            rot_result = WY(normal_vector, angle)            
        elif plane == "ZY":
            rot_result = ZY(normal_vector, angle)
        else:
            print("Error: no such rotational plate, valid planes: XY, XZ, XW, WZ, WY, ZY")

        if rot_result is None:
            print("Error: unacceptable angle")
            return None
        else:
            return Vector4(self.position , rot_result, self.distance)
            
