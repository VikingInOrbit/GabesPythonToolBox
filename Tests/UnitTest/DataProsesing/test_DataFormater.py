from GabesPythonToolBox.DataProsesing.DataFormater import (
    filter_data_cutoff,
    helper_column,
    merge_data_by,
    rebase_data,
    sort_data_by,
)

# TODO


def test_merge_sort_filter_and_helper():
    data = [
        {"name": "A", "value": 1},
        {"name": "B", "value": 3},
        {"name": "A", "value": 2},
    ]

    merged = merge_data_by(data, "name", ["value"])
    assert any(row["name"] == "A" and row["value"] == 3 for row in merged)

    sorted_rows = sort_data_by(data, "value", reverse=True)
    assert sorted_rows[0]["value"] == 3

    filtered = filter_data_cutoff(data, "value", cutoff=2, dir=True)
    assert all(row["value"] >= 2 for row in filtered)

    with_helper = helper_column(data, "value", "double", lambda v: v * 2)
    assert with_helper[0]["double"] == 2


def test_rebase_data_keeps_visible_keys():
    data = [
        {"name": "A", "value": 1, "extra": 9},
        {"name": "B", "value": 2, "extra": 8},
    ]
    col_widths = {"name": 4, "value": 5}

    rebased = rebase_data(data, ["name", "value"], col_widths)

    assert list(rebased[0].keys()) == ["name", "value"]
