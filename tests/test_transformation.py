from vector import Vector2
from transform import scaled, angle_add

def test_scaling():
    v = Vector2(1, 2)
    scale = 3
    screen_size(50, 100)

    result = scaled(v, scale, screen_size)

    assert result == Vector2(75, -300)


def test_angle_addition():
    angle_a = 90
    angle_b = 180
    result = angle_add(angle_a, angle_b)

    assert result == 270

