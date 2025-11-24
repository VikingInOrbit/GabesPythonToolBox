import pytest

from GabesPythonToolBox.Suporting.yamlReader import read_ymal
from Tests.UnitTestComon.UntTestUtility import (
    Complex_data,
    sample_data,
    write_yaml_test,
)

# Supporting func to help the test


# Tests
def test_read_ymal_reads_correctly(tmp_path):
    test_file = tmp_path / "test.yaml"
    write_yaml_test(test_file, sample_data)

    loaded = read_ymal(test_file)
    assert loaded == sample_data


def test_read_ymal_with_different_encoding(tmp_path):
    test_file = tmp_path / "test.yaml"
    write_yaml_test(test_file, Complex_data)

    loaded = read_ymal(test_file, encoding="utf-8")
    assert loaded == Complex_data


def test_read_ymal_nonexistent_file_raises(tmp_path):
    test_file = tmp_path / "missing.yaml"

    with pytest.raises(FileNotFoundError):
        read_ymal(test_file)
