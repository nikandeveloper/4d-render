import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from vector import Vector3, Vector2
import math

def test_vector_3d_subrtaction():
    a = Vector3(1, 2, 3)
    b = Vector3(4, 3, 2)

    assert a.sub(b) == Vector3(-3, -1, 1)

def test_vector_3d_addition():
    a = Vector3(1, 2, 3)
    b = Vector3(0, 5, 8)

    assert a.add(b) == Vector3(1, 7, 11)

def test_vector_3d_dot():
    a = Vector3(1, 2, 3)
    b = Vector3(0, 5, 8)

    assert a.dot(b) == (0 + 10 + 24)

def test_vector_3d_multiply():
    a = Vector3(1, 2, 3)
    b = 2

    assert a.multiply(b) == Vector3(2, 4, 6)

def test_vector_3d_length():
    a = Vector3(1, 2, 3)

    assert a.length() == math.sqrt(1 + 4 + 9)

    
def test_vector_3d_toTuple():
    a = Vector3(2, 4, 6)

    assert a.toTuple() == (2, 4, 6)

def test_vector_Vector2():
    a = Vector3(1, 2, 3)

    assert a.toVector2() == Vector2(1, 2)
