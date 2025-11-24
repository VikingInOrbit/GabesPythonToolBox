import pytest

from GabesPythonToolBox.Suporting.csvWriter import write_csv
from Tests.UnitTestComon.UntTestUtility import (
    read_csv_test,
    sample_data,
    write_json_test,
)


# Tests
def test_write_csv_creates_file(tmp_path):
    test_file = tmp_path / "test.csv"
    write_csv(test_file, sample_data)
    assert test_file.exists()


def test_write_csv_exception_handling(tmp_path):

    invalid_file_path = tmp_path / "some_dir"
    invalid_file_path.mkdir()

    with pytest.raises(Exception) as exc_info:
        write_csv(invalid_file_path, sample_data)

    assert "some_dir" in str(exc_info.value)


def test_write_csv_headers_and_body(tmp_path):
    test_file = tmp_path / "test.csv"
    write_csv(test_file, sample_data, data_mode="all")
    loaded = read_csv_test(test_file)
    # Check first row content
    assert loaded[0]["name"] == "Alice"
    assert loaded[1]["score"] == "88.2"  # default float symbol


def test_write_csv_float_symbol(tmp_path):
    test_file = tmp_path / "test.csv"
    write_csv(test_file, sample_data, float_symbol=",")
    loaded = read_csv_test(test_file)
    # Floats should have ',' instead of '.'
    assert loaded[0]["score"] == "95,5"
    assert loaded[1]["score"] == "88,2"


def test_write_csv_data_modes(tmp_path):
    test_file_all = tmp_path / "all.csv"
    test_file_head = tmp_path / "head.csv"
    test_file_body = tmp_path / "body.csv"
    test_file_none = tmp_path / "none.csv"

    write_csv(test_file_all, sample_data, data_mode="all")
    write_csv(test_file_head, sample_data, data_mode="head")
    write_csv(test_file_body, sample_data, data_mode="body")
    write_csv(test_file_none, sample_data, data_mode="none")

    # all: header + body
    loaded_all = read_csv_test(test_file_all)
    assert len(loaded_all) == 2
    # head: no body
    with open(test_file_head, encoding="utf-8") as f:
        content_head = f.read()
    assert "Alice" not in content_head
    # body: no header
    with open(test_file_body, encoding="utf-8") as f:
        content_body = f.read()
    assert "name,age,score" not in content_body
    # none: nothing written
    with open(test_file_none, encoding="utf-8") as f:
        content_none = f.read()
    assert content_none.strip() == ""


# TODO write UTF8 data


def test_write_csv_invalid_data(tmp_path):
    test_file = tmp_path / "test.csv"
    with pytest.raises(ValueError):
        write_csv(test_file, {"not": "a list"})
    with pytest.raises(ValueError):
        write_csv(test_file, [])
    with pytest.raises(ValueError):
        write_csv(test_file, [{"valid": 1}, "invalid row"])
