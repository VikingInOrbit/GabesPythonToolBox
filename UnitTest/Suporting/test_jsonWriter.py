import pytest
from GabesPythonToolBox.Suporting.jsonWriter import write_json
import json

# Supporting func
def read_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

# Tests
def test_write_json_creates_file(tmp_path):
    test_file = tmp_path / "test.json"
    data = {"key": "value"}
    write_json(test_file, data)
    assert test_file.exists()
    assert read_json(test_file) == data

def test_write_json_overwrites_file(tmp_path):
    test_file = tmp_path / "test.json"
    write_json(test_file, {"old": "data"})
    write_json(test_file, {"new": "data"})
    assert read_json(test_file) == {"new": "data"}

def test_write_json_merge_append(tmp_path):
    test_file = tmp_path / "test.json"
    write_json(test_file, {"a": 1, "b": 2})
    write_json(test_file, {"b": 3, "c": 4}, mode='a')  # merge dictionaries
    expected = {"a": 1, "b": 3, "c": 4}
    assert read_json(test_file) == expected

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
    data = {"greeting": "こんにちは", "key": "üñîçødë"}
    write_json(test_file, data)
    loaded = read_json(test_file)
    assert loaded == data
