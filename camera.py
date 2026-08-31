from vector import *
from dataclasses import dataclass
import transform

@dataclass
class Camera4D:
    position: Vector4
    normal_vector: Vector4
    distance: float

    def move(self, speed: Vector4):
        return Camera4D(self.position.add(speed), self.normal_vector, self.distance)

    def rotate(self, plane: str, angle):
        if plane == "XY":
            rot_result = transform.XY(self.normal_vector, angle)
        elif plane == "XZ":
            rot_result = transform.XZ(self.normal_vector, angle)
        elif plane == "XW":
            rot_result = transform.XW(self.normal_vector, angle)
        elif plane == "WZ":
            rot_result = transform.WZ(self.normal_vector, angle)
        elif plane == "WY":
            rot_result = transform.WY(self.normal_vector, angle)            
        elif plane == "ZY":
            rot_result = transform.ZY(self.normal_vector, angle)
        else:
            print("Error: no such rotational plate, valid planes: XY, XZ, XW, WZ, WY, ZY")
            return None

        if rot_result is None:
            print("Error: unacceptable angle")
            return None
        else:
            return Camera4D(self.position , rot_result, self.distance)
            
