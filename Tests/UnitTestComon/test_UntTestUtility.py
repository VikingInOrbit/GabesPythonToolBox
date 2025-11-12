import pytest
from GabesPythonToolBox.Tests.UnitTestComon.UntTestUtility import *

import pytest
from GabesPythonToolBox.Tests.UnitTestComon.UntTestUtility import (
    Nothing,
    almost_equal,
    Generate_sequence,
    write_csv_for_test,
    read_csv_test,
    write_json_test,
    read_json_test,
    write_yaml_test,
    read_yaml_test,
    write_config_test
)

# --- Tests ---

def test_Nothing():
    # Should simply run without errors and return None
    assert Nothing() is None

def test_almost_equal():
    assert almost_equal(1.0000001, 1.0)
    assert not almost_equal(1.001, 1.0)

def test_Generate_sequence():
    seq = Generate_sequence(5)
    assert seq == [1.0, 2.0, 3.0, 4.0, 5.0]
    # Ensure floats
    assert all(isinstance(x, float) for x in seq)

@pytest.mark.parametrize("lines", [
    (["a,b,c", "1,2,3", "4,5,6"])
])
def test_csv_read_write(tmp_path, lines):
    file_path = tmp_path / "test.csv"
    write_csv_for_test(file_path, lines)
    data = read_csv_test(file_path)
    # Expecting list of dicts
    assert data == [{"a": "1", "b": "2", "c": "3"},
                    {"a": "4", "b": "5", "c": "6"}]

def test_json_read_write(tmp_path):
    file_path = tmp_path / "test.json"
    data = {"name": "Alice", "age": 30}
    write_json_test(file_path, data)
    loaded = read_json_test(file_path)
    assert loaded == data

def test_yaml_read_write(tmp_path):
    file_path = tmp_path / "test.yaml"
    data = {"name": "Bob", "active": True, "scores": [1, 2, 3]}
    write_yaml_test(file_path, data)
    loaded = read_yaml_test(file_path)
    assert loaded == data

@pytest.mark.parametrize("ext", [".json", ".yaml", ".yml"])
def test_write_config_test(tmp_path, ext):
    file_path = tmp_path / f"config{ext}"
    data = {"key": "value"}
    write_config_test(file_path, data)
    if ext == ".json":
        loaded = read_json_test(file_path)
    else:
        loaded = read_yaml_test(file_path)
    assert loaded == data

def test_write_config_test_unsupported(tmp_path):
    file_path = tmp_path / "config.txt"
    with pytest.raises(ValueError):
        write_config_test(file_path, {"key": "value"})
