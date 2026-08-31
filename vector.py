from dataclasses import dataclass
import math

@dataclass(frozen=True)
class Vector4:
    x: float
    y: float
    z: float
    w: float

    def sub(self, other: "Vector4") -> Vector4:

        return Vector4(        
            self.x - other.x,
            self.y - other.y,
            self.z - other.z,
            self.w - other.w,
        )


    def add(self, other: "Vector4") -> Vector4:

        return Vector4(  
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
            self.w + other.w
        )


    def multiply(self, other: "float") -> Vector4:

        return Vector4(
            self.x * other,
            self.y * other,
            self.z * other,
            self.w * other

        )    


    def dot(self, other: "Vector4") -> float:
        return (
            self.x * other.x +
            self.y * other.y +
            self.z * other.z +
            self.w * other.w
        )   


    def length(self) -> float:
        return math.sqrt(self.dot(self))


    def toVector3(self) -> Vector3:
        return Vector3(self.x, self.y, self.z)


    def toVector2(self) -> Vector2:
        return Vector2(self.x, self.y)

    def toTuple(self) -> tuple:
        return (self.x, self.y, self.z, self.w)    


@dataclass(frozen=True)
class Vector3:
    x: float
    y: float
    z: float

    def sub(self, other: "Vector3") -> Vector3:

        return Vector3(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z

        )


    def add(self, other: "Vector3") -> Vector3:

        return Vector3(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z

        )


    def multiply(self, other: "float") -> Vector3:
        return Vector3(
            self.x * other,
            self.y * other,
            self.z * other
        )    


    def dot(self, other: "Vector3") -> float:
        return (
            self.x * other.x +
            self.y * other.y +
            self.z * other.z 
        )   


    def length(self) -> float:
        return math.sqrt(self.dot(self))


    def toVector2(self) -> Vector2:
        return Vector2(self.x, self.y)


    def toTuple(self) -> tuple:
        return (self.x, self.y, self.z)    


@dataclass(frozen=True)
class Vector2:
    x: float
    y: float

    def sub(self, other: "Vector2") -> Vector2:

        return Vector2(        
            self.x - other.x,
            self.y - other.y
        )


    def add(self, other: "Vector2") -> Vector2:

        return Vector2(
            self.x + other.x,
            self.y + other.y

        )


    def multiply(self, other: "float") -> Vector2:

        return Vector2(
            self.x * other,
            self.y * other
        )    


    def dot(self, other: "Vector2") -> float:
        return (
            self.x * other.x +
            self.y * other.y 
        )   


    def length(self) -> float:
        return math.sqrt(self.dot(self))

    def toTuple(self) -> tuple:
        return (self.x, self.y)    
