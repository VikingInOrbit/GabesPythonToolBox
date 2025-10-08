import pytest
from GabesPythonToolBox.Suporting.jsonReader import read_json
import json

# Supporting func to help the test
def write_json_for_test(file_path, data):
    """Helper function to create JSON files for testing read_json."""
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# Tests
def test_read_json_basic(tmp_path):
    test_file = tmp_path / "test.json"
    data = {"key": "value"}
    write_json_for_test(test_file, data)
    
    loaded = read_json(test_file)
    assert loaded == data

def test_read_json_with_unicode(tmp_path):
    test_file = tmp_path / "test.json"
    data = {"greeting": "こんにちは", "key": "üñîçødë"}
    write_json_for_test(test_file, data)
    
    loaded = read_json(test_file, encoding="utf-8")
    assert loaded == data

def test_read_json_nonexistent_file_raises(tmp_path):
    test_file = tmp_path / "missing.json"
    
    with pytest.raises(FileNotFoundError):
        read_json(test_file)

def test_read_json_invalid_json_raises(tmp_path):
    test_file = tmp_path / "invalid.json"
    with open(test_file, "w", encoding="utf-8") as f:
        f.write("invalid json content")
    
    with pytest.raises(json.JSONDecodeError):
        read_json(test_file)
