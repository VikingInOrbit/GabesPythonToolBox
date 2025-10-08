import pytest
from GabesPythonToolBox.Suporting.yamlReader import read_ymal
import yaml
import os

# Supporting func to help the test
def write_yaml_for_test(file_path, data):
    """Helper to write YAML files for testing read function."""
    with open(file_path, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True)

# Tests
def test_read_ymal_reads_correctly(tmp_path):
    test_file = tmp_path / "test.yaml"
    data = {"key": "value"}
    write_yaml_for_test(test_file, data)
    
    loaded = read_ymal(test_file)
    assert loaded == data

def test_read_ymal_with_different_encoding(tmp_path):
    test_file = tmp_path / "test.yaml"
    data = {"key": "üñîçødë"}
    write_yaml_for_test(test_file, data)
    
    loaded = read_ymal(test_file, encoding="utf-8")
    assert loaded == data

def test_read_ymal_nonexistent_file_raises(tmp_path):
    test_file = tmp_path / "missing.yaml"
    
    with pytest.raises(FileNotFoundError):
        read_ymal(test_file)
