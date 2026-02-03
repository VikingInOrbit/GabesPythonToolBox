from GabesPythonToolBox.DataProsesing.DataHelperFunctions import (
    count,
    get_column_widths,
    meet_condition,
    position_handler,
)

# TODO


def test_count_and_column_widths():
    data = [
        {"name": "Alpha", "value": 1},
        {"name": "Beta", "value": 2},
        {"name": "Alpha", "value": 3},
    ]

    assert count(data, "name") == 2

    widths = get_column_widths(data)
    assert widths["name"] >= len("Alpha")
    assert widths["value"] >= len("value")


def test_meet_condition_and_position_handler():
    assert meet_condition(5, 5, "equals") is True
    assert meet_condition(5, 4, "gte") is True
    assert meet_condition(3, 4, "lte") is True

    assert position_handler("start", "*", "A") == "*A"
    assert position_handler("end", "*", "A") == "A*"
    assert position_handler("both", "*", "A") == "*A*"
