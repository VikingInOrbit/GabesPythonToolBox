import pytest
from GabesPythonToolBox.Suporting.yamlWriter import write_yaml
import os
import yaml

# Supporting func to help the test
def read_yaml(file_path):
    """Helper function to read YAML for test verification."""
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

# Tests
def test_write_yaml_creates_file(tmp_path):
    test_file = tmp_path / "test.yaml"
    data = {"key": "value"}
    
    write_yaml(test_file, data)
    
    assert test_file.exists()
    assert read_yaml(test_file) == data

def test_write_yaml_overwrites_file(tmp_path):
    test_file = tmp_path / "test.yaml"
    initial_data = {"old": "data"}
    write_yaml(test_file, initial_data)
    
    new_data = {"new": "data"}
    write_yaml(test_file, new_data)
    
    assert read_yaml(test_file) == new_data

def test_write_yaml_merge_append(tmp_path):
    test_file = tmp_path / "test.yaml"
    
    # Initial data
    data1 = {"a": 1, "b": 2}
    write_yaml(test_file, data1)
    
    # New data to append (merge)
    data2 = {"b": 3, "c": 4}  # 'b' should be overwritten
    write_yaml(test_file, data2, mode='a')
    
    expected = {"a": 1, "b": 3, "c": 4}
    assert read_yaml(test_file) == expected

def test_write_yaml_append_non_dict_raises(tmp_path):
    test_file = tmp_path / "test.yaml"
    
    # Write non-dict content
    with open(test_file, "w", encoding="utf-8") as f:
        f.write("Just a string")
    
    # Trying to append dict should raise TypeError
    with pytest.raises(TypeError):
        write_yaml(test_file, {"new": "data"}, mode='a')
