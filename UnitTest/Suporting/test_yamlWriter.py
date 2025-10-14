import pytest
from GabesPythonToolBox.Suporting.yamlWriter import write_yaml
import os
import yaml
from GabesPythonToolBox.UnitTest.UnitTestComon.UntTestUtility import read_yaml_test,sample_data,Complex_data,New_data

# Tests
def test_write_yaml_creates_file(tmp_path):
    test_file = tmp_path / "test.yaml"
    write_yaml(test_file, sample_data)
    
    assert test_file.exists()
    assert read_yaml_test(test_file) == sample_data

def test_write_yaml_overwrites_file(tmp_path):
    test_file = tmp_path / "test.yaml"
    write_yaml(test_file, sample_data)
    write_yaml(test_file, New_data)
    
    assert read_yaml_test(test_file) == New_data

def test_write_yaml_merge_append(tmp_path):
    test_file = tmp_path / "test.yaml"
    
    data0=sample_data[0]
    data1=sample_data[1]
    write_yaml(test_file, data0)
    
    # New data to append (merge)
    write_yaml(test_file, data1, mode='a')
    
    expected = data0.copy()
    expected.update(data1)
    assert read_yaml_test(test_file) == expected


def test_write_yaml_append_non_dict_raises(tmp_path):
    test_file = tmp_path / "test.yaml"
    
    # Write non-dict content
    with open(test_file, "w", encoding="utf-8") as f:
        f.write("Just a string")
    
    # Trying to append dict should raise TypeError
    with pytest.raises(TypeError):
        write_yaml(test_file, {"new": "data"}, mode='a')
