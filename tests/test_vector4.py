import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from vector import Vector4, Vector3, Vector2
import math

def test_vector_4d_subrtaction():
    a = Vector4(1, 2, 3, 4)
    b = Vector4(4, 3, 2, 1)

    assert a.sub(b) == Vector4(-3, -1, 1, 3)

def test_vector_4d_addition():
    a = Vector4(1, 2, 3, 4)
    b = Vector4(0, 5, 8, 6)

    assert a.add(b) == Vector4(1, 7, 11, 10)

def test_vector_4d_dot():
    a = Vector4(1, 2, 3, 4)
    b = Vector4(0, 5, 8, 6)

    assert a.dot(b) == (0 + 10 + 24 + 24)

def test_vector_4d_multiply():
    a = Vector4(1, 2, 3, 4)
    b = 2

    assert a.multiply(b) == Vector4(2, 4, 6, 8)

def test_vector_4d_length():
    a = Vector4(1, 2, 3, 4)

    assert a.length() == math.sqrt(1 + 4 + 9 + 16)

    
def test_vector_4d_toTuple():
    a = Vector4(2, 4, 6, 8)

    assert a.toTuple() == (2, 4, 6, 8)

def test_vector_Vector2():
    a = Vector4(1, 2, 3, 4)

    assert a.toVector2() == Vector2(1, 2)

def test_vector_Vector3():
    a = Vector4(2, 4, 6, 7)
    
    assert a.toVector3() == Vector3(2, 4, 6)
