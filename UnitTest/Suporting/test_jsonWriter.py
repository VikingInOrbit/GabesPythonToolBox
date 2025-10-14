import pytest
from GabesPythonToolBox.Suporting.jsonWriter import write_json
import json
from GabesPythonToolBox.UnitTest.UnitTestComon.UntTestUtility import read_json_test,sample_data,Complex_data,New_data

# Tests
def test_write_json_creates_file(tmp_path):
    test_file = tmp_path / "test.json"
    data = {"key": "value"}
    write_json(test_file, sample_data)
    assert test_file.exists()
    assert read_json_test(test_file) == sample_data

def test_write_json_overwrites_file(tmp_path):
    test_file = tmp_path / "test.json"
    write_json(test_file, sample_data)
    write_json(test_file, New_data)
    assert read_json_test(test_file) == New_data

def test_write_json_merge_append(tmp_path):
    test_file = tmp_path / "test.json"
    data0=sample_data[0]
    data1=sample_data[1]
    write_json(test_file,data0)
    write_json(test_file, data1, mode='a')  # merge dictionaries
    expected = data0.copy()
    expected.update(data1)
    assert read_json_test(test_file) == expected

def test_write_json_append_non_dict_raises(tmp_path):
    test_file = tmp_path / "test.json"
    with open(test_file, "w", encoding="utf-8") as f:
        f.write(json.dumps(["not", "a", "dict"]))
    
    with pytest.raises(TypeError):
        write_json(test_file, {"new": "data"}, mode='a')

def test_write_json_append_invalid_json_raises(tmp_path):
    test_file = tmp_path / "test.json"
    with open(test_file, "w", encoding="utf-8") as f:
        f.write("invalid json")
    
    with pytest.raises(ValueError):
        write_json(test_file, {"new": "data"}, mode='a')

def test_write_json_unicode_support(tmp_path):
    test_file = tmp_path / "test.json"
    data = Complex_data
    write_json(test_file, data)
    loaded = read_json_test(test_file)
    assert loaded == data
