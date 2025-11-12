import pytest
from GabesPythonToolBox.Suporting.jsonReader import read_json
from GabesPythonToolBox.Tests.UnitTestComon.UntTestUtility import write_json_test,sample_data,Complex_data

import json

# Tests
def test_read_json_basic(tmp_path):
    test_file = tmp_path / "test.json"
    write_json_test(test_file, sample_data)
    loaded = read_json(test_file)
    assert loaded == sample_data

def test_read_json_with_unicode(tmp_path):
    test_file = tmp_path / "test.json"
    write_json_test(test_file, Complex_data)
    
    loaded = read_json(test_file, encoding="utf-8")
    assert loaded == Complex_data

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
