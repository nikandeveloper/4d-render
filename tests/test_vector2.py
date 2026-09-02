import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from vector import Vector2
import math

def test_vector_2d_subrtaction():
    a = Vector2(1, 2)
    b = Vector2(4, 3)

    assert a.sub(b) == Vector2(-3, -1)

def test_vector_2d_addition():
    a = Vector2(1, 2)
    b = Vector2(0, 5)

    print(a.add(b))

    assert a.add(b) == Vector2(1, 7)

def test_vector_2d_dot():
    a = Vector2(1, 2)
    b = Vector2(0, 5)

    assert a.dot(b) == (0 + 10)

def test_vector_2d_multiply():
    a = Vector2(1, 2)
    b = 2

    assert a.multiply(b) == Vector2(2, 4)

def test_vector_2d_length():
    a = Vector2(1, 2)

    assert a.length() == math.sqrt(1 + 4)

    
def test_vector_2d_toTuple():
    a = Vector2(2, 4)

    assert a.toTuple() == (2, 4)
