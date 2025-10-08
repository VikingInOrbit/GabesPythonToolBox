import pytest
import GabesPythonToolBox.DataProsesing.map as map

def almost_equal(a, b, tol=1e-6):
    return abs(a - b) < tol



# Map tests


def test_map_basic_linear_mapping():
    # Simple case: map 5 from range 0–10 → 0–100
    result = map.Map(5, 0, 10, 0, 100)
    assert almost_equal(result, 50)


def test_map_negative_to_positive_range():
    # Map -5 from -10–10 → 0–100 → should give 25
    result = map.Map(-5, -10, 10, 0, 100)
    assert almost_equal(result, 25)


def test_map_reversed_input_range():
    # Reverse input range should still work correctly
    result = map.Map(5, 10, 0, 0, 100)
    assert almost_equal(result, 50)


def test_map_type_error():
    with pytest.raises(TypeError):
        map.Map("a", 0, 10, 0, 100)
        map.Map(0, "a", 10, 0, 100)
        map.Map(10, 0, "a", 0, 100)
        map.Map(0, 0, 10, "a", 100)
        map.Map(100, 0, 10, 0, "a")



# ClampMap tests


def test_clampmap_within_range():
    # Normal input: should act like Map
    result = map.ClampMap(5, 0, 10, 0, 100)
    assert almost_equal(result, 50)


def test_clampmap_above_max():
    # Input above maxInput should clamp to maxOutput
    result = map.ClampMap(20, 0, 10, 0, 100)
    assert almost_equal(result, 100)


def test_clampmap_below_min():
    # Input below minInput should clamp to minOutput
    result = map.ClampMap(-10, 0, 10, 0, 100)
    assert almost_equal(result, 0)


def test_clampmap_type_error():
    with pytest.raises(TypeError):
        map.Map("a", 0, 10, 0, 100)
        map.Map(0, "a", 10, 0, 100)
        map.Map(10, 0, "a", 0, 100)
        map.Map(0, 0, 10, "a", 100)
        map.Map(100, 0, 10, 0, "a")

# ClampMap tests

def test_clamp_basic():
    assert map.Clamp(5, 0, 10) == 5
    assert map.Clamp(-1, 0, 10) == 0
    assert map.Clamp(15, 0, 10) == 10


def test_clamp_min_only():
    assert map.Clamp(2, minOutput=5) == 5
    assert map.Clamp(10, minOutput=5) == 10


def test_clamp_max_only():
    assert map.Clamp(12, maxOutput=10) == 10
    assert map.Clamp(3, maxOutput=10) == 3


def test_clamp_no_limits():
    assert map.Clamp(7) == 7


def test_clamp_type_error():
    with pytest.raises(TypeError):
        map.Map("a", 0, 10)
        map.Map(0, "a", 10)
        map.Map(10, 0, "a")
        