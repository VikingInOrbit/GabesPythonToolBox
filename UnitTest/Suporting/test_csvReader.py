import pytest
import tempfile
import os
from GabesPythonToolBox.Suporting.csvReader import *


# process_line tests

def test_process_line_basic():
    result = process_line("1,2,3")
    assert result == ["1", "2", "3"]


def test_process_line_empty_line():
    result = process_line("   ")
    assert result == []


def test_process_line_custom_separator():
    result = process_line("1;2;3", seperator_symbol=";")
    assert result == ["1", "2", "3"]


def test_process_line_float_symbol_change():
    # Example where decimal uses ',' instead of '.'
    result = process_line("1,23;4,56", seperator_symbol=";", float_symbol=",")
    assert result == ["1.23", "4.56"]


def test_process_line_trims_spaces():
    result = process_line(" 1 , 2 , 3 ")
    assert result == ["1", "2", "3"]



# read_csv tests


def create_temp_csv(content: str):
    """Helper to write a temporary CSV file and return its path."""
    tmp = tempfile.NamedTemporaryFile(delete=False, mode="w+", encoding="utf-8", suffix=".csv")
    tmp.write(content)
    tmp.flush()
    tmp.close()
    return tmp.name


def test_read_csv_all_rows():
    csv_content = "A,B,C\n1,2,3\n4,5,6\n"
    path = create_temp_csv(csv_content)

    data = read_csv(path)
    os.remove(path)

    assert len(data) == 2
    assert data[0] == {"A": "1", "B": "2", "C": "3"}
    assert data[1] == {"A": "4", "B": "5", "C": "6"}


def test_read_csv_head():
    csv_content = "A,B\n1,2\n3,4\n5,6\n"
    path = create_temp_csv(csv_content)

    data = read_csv(path, read_from="head", read_n_lines=1)
    os.remove(path)

    assert len(data) == 1
    assert data[0] == {"A": "1", "B": "2"}


def test_read_csv_tail():
    csv_content = "A,B\n1,2\n3,4\n5,6\n"
    path = create_temp_csv(csv_content)

    data = read_csv(path, read_from="tail", read_n_lines=1)
    os.remove(path)

    assert len(data) == 1
    assert data[0] == {"A": "5", "B": "6"}


def test_read_csv_empty_file():
    csv_content = ""
    path = create_temp_csv(csv_content)

    data = read_csv(path)
    os.remove(path)

    assert data == []  # Expecting an empty list, not an exception

