from vector import Vector4
import transform


def test_rotation_XY():
    v = Vector4(1, 0, 0, 0)

    result = transform.rotate(v, "XY", 90)

    assert abs(result.x) < 0.00001
    assert abs(result.y-1) < 0.00001
    assert result.z == 0
    assert result.w == 0


def test_rotation_XZ():
    v = Vector4(1, 0, 0, 0)

    result = transform.rotate(v, "XZ", 90)

    assert abs(result.x) < 0.00001
    assert abs(result.z-1) < 0.00001
    assert result.y == 0
    assert result.w == 0


def test_rotation_XW():
    v = Vector4(1, 0, 0, 0)

    result = transform.rotate(v, "XW", 90)

    assert abs(result.x) < 0.00001
    assert abs(result.w-1) < 0.00001
    assert result.z == 0
    assert result.y == 0


def test_rotation_WZ():
    v = Vector4(0, 0, 0, 1)

    result = transform.rotate(v, "WZ", 90)

    assert abs(result.w) < 0.00001
    assert abs(result.z-1) < 0.00001
    assert result.x == 0
    assert result.y == 0


def test_rotation_WY():
    v = Vector4(0, 0, 0, 1)

    result = transform.rotate(v, "WY", 90)

    assert abs(result.w) < 0.00001
    assert abs(result.y-1) < 0.00001
    assert result.z == 0
    assert result.x == 0


def test_rotation_ZY():
    v = Vector4(0, 0, 1, 0)

    result = transform.rotate(v, "ZY", 90)

    assert abs(result.z) < 0.00001
    assert abs(result.y-1) < 0.00001
    assert result.x == 0
    assert result.w == 0


def test_rotation_reverse_XY():
    v = Vector4(1, 0, 0, 0)

    result = transform.rotate(v, "XY", 90)
    result = transform.rotate(result, "XY", -90)


    assert abs(result.x-1) < 0.00001
    assert abs(result.y) < 0.00001
    assert result.z == 0
    assert result.w == 0


def test_rotation_reverse_XZ():
    v = Vector4(1, 0, 0, 0)

    result = transform.rotate(v, "XZ", 90)
    result = transform.rotate(result, "XZ", -90)

    assert abs(result.x-1) < 0.00001
    assert abs(result.z) < 0.00001
    assert result.y == 0
    assert result.w == 0


def test_rotation_reverse_XW():
    v = Vector4(1, 0, 0, 0)

    result = transform.rotate(v, "XW", 90)
    result = transform.rotate(result, "XW", -90)

    assert abs(result.x-1) < 0.00001
    assert abs(result.w) < 0.00001
    assert result.z == 0
    assert result.y == 0


def test_rotation_reverse_WZ():
    v = Vector4(0, 0, 0, 1)

    result = transform.rotate(v, "WZ", 90)
    result = transform.rotate(result, "WZ", -90)

    assert abs(result.w-1) < 0.00001
    assert abs(result.z) < 0.00001
    assert result.x == 0
    assert result.y == 0


def test_rotation_reverse_WY():
    v = Vector4(0, 0, 0, 1)

    result = transform.rotate(v, "WY", 90)
    result = transform.rotate(result, "WY", -90)

    assert abs(result.w-1) < 0.00001
    assert abs(result.y) < 0.00001
    assert result.z == 0
    assert result.x == 0


def test_rotation_reverse_ZY():
    v = Vector4(0, 0, 1, 0)

    result = transform.rotate(v, "ZY", 90)
    result = transform.rotate(result, "ZY", -90)

    assert abs(result.z-1) < 0.00001
    assert abs(result.y) < 0.00001
    assert result.x == 0
    assert result.w == 0
