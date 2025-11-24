import pytest

from GabesPythonToolBox.Suporting.csvReader import process_line, read_csv
from GabesPythonToolBox.Tests.UnitTestComon.UntTestUtility import write_csv_for_test

# Sample CSV content
csv_lines = [
    "name,age,score",
    "Alice,30,95.5",
    "Bob,25,88.2",
    "Charlie,28,91.0",
]

csv_lines_empty = ["name,age,score", "Alice,30,95.5", "", ""]


# Tests
def test_process_line_basic():
    line = "Alice,30,95.5"
    result = process_line(line)
    assert result == ["Alice", "30", "95.5"]


def test_process_line_empty_line():
    result = process_line("   ")
    assert result == []


def test_process_line_custom_separators_and_floats():
    line = "Alice;30;95,5"
    result = process_line(line, seperator_symbol=";", float_symbol=",")
    assert result == ["Alice", "30", "95.5"]


def test_read_csv_all_lines(tmp_path):
    test_file = tmp_path / "test.csv"
    write_csv_for_test(test_file, csv_lines)

    data = read_csv(test_file)
    assert len(data) == 3
    assert data[0]["name"] == "Alice"
    assert data[1]["score"] == "88.2"


def test_read_csv_head_lines(tmp_path):
    test_file = tmp_path / "test.csv"
    write_csv_for_test(test_file, csv_lines)

    data = read_csv(test_file, read_from="head", read_n_lines=2)
    assert len(data) == 2
    assert data[0]["name"] == "Alice"


def test_read_csv_tail_lines(tmp_path):
    test_file = tmp_path / "test.csv"
    write_csv_for_test(test_file, csv_lines)

    data = read_csv(test_file, read_from="tail", read_n_lines=2)
    assert len(data) == 2
    assert data[0]["name"] == "Bob"
    assert data[1]["name"] == "Charlie"


def test_read_csv_custom_separator_and_float(tmp_path):
    test_file = tmp_path / "test.csv"
    custom_lines = ["name;age;score", "Alice;30;95,5", "Bob;25;88,2"]
    write_csv_for_test(test_file, custom_lines)

    data = read_csv(test_file, seperator_symbol=";", float_symbol=",")
    assert data[0]["score"] == "95.5"
    assert data[1]["score"] == "88.2"


def test_read_csv_empty_file(tmp_path):
    test_file = tmp_path / "empty.csv"
    write_csv_for_test(test_file, [])

    # Should return empty list
    data = read_csv(test_file)
    assert data == []


def test_read_csv_triggers_empty_line(tmp_path):

    test_file = tmp_path / "test.csv"
    with open(test_file, "w", encoding="utf-8") as f:
        for line in csv_lines_empty:
            f.write(line + "\n")

    # Call read_csv with read_from="head" and read_n_lines=5 (more than actual lines)
    data = read_csv(str(test_file), read_from="head", read_n_lines=5)

    assert len(data) == 1
    assert data[0] == {"name": "Alice", "age": "30", "score": "95.5"}

    empty_line_values = process_line("")
    assert empty_line_values == []
