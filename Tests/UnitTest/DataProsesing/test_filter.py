import pytest

from GabesPythonToolBox.DataProsesing.filter import Filter, newFilter
from Tests.UnitTestComon.UntTestUtility import Generate_sequence, almost_equal

# Tests


def test_average_filter_basic():
    f = Filter(num_points=3, filter_type="average")
    inputs = Generate_sequence(3)
    outputs = [f(x) for x in inputs]

    # After all inputs, average should be (1 + 2 + 3) / 3 = 2
    assert pytest.approx(outputs[-1], 0.0001) == 2.0


def test_average_filter_window_limit():
    f = Filter(num_points=3, filter_type="average")
    # Add more than 3 points to ensure oldest values are dropped
    val = Generate_sequence(5)
    for x in val:
        out = f(x)
    # Only last 3 points (3,4,5) should remain, avg = 4
    assert almost_equal(out, 4)


def test_new_weighted_filter():
    f = Filter(num_points=3, filter_type="newWeighted")
    for val in [10, 20, 30]:
        out = f(val)
    # Weighted average (1*10 + 2*20 + 3*30) / 6 = 23.33...
    assert almost_equal(out, 23.3333333333)


def test_old_weighted_filter():
    f = Filter(num_points=3, filter_type="oldWeighted")
    for val in [10, 20, 30]:
        out = f(val)
    # Weighted average (3*10 + 2*20 + 1*30) / 6 = 16.67...
    assert almost_equal(out, 16.666666666)


def test_invalid_input_type_raises():
    f = Filter(num_points=3)
    with pytest.raises(TypeError):
        f("invalid")  # not numeric


def test_unsupported_filter_type_raises():
    f = Filter(num_points=3, filter_type="unknownType")
    with pytest.raises(ValueError):
        f(5)


def test_empty_filter_returns_zero():
    f = Filter(num_points=3)
    # Manually clear data_points to simulate empty state
    f.data_points = []
    result = f(1)  # adds one, should average correctly
    assert isinstance(result, float)


def test_window_behavior_pop():
    f = Filter(num_points=3)
    f(1)
    f(2)
    f(3)
    f(4)  # should pop oldest
    assert len(f.data_points) == 3
    assert f.data_points == [2, 3, 4]


def test_newFilter_factory_creates_instance():
    f = newFilter(5, "average")
    assert isinstance(f, Filter)
    assert f.num_points == 5
    assert f.filter_type == "average"
