from GabesPythonToolBox.DataProsesing.DataConsolPrinter import format_data, print_table

# TODO


def test_format_data_builds_rows():
    data = [
        {"name": "A", "value": 1, "ratio": 1.5},
        {"name": "B", "value": 2, "ratio": 2.0},
    ]

    lines = format_data(data)

    assert len(lines) >= 3
    assert lines[0].startswith("|")
    assert lines[0].endswith("|")


def test_print_table_outputs(capsys):
    data = [
        {"name": "A", "value": 1},
        {"name": "B", "value": 2},
    ]

    print_table(data, Topper="Test")
    captured = capsys.readouterr().out

    assert "Test" in captured
