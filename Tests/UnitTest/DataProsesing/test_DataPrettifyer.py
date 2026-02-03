from GabesPythonToolBox.DataProsesing.DataPrettifyer import (
    HMI_prettify_caracter,
    HMI_prettify_cell,
    HMI_prettify_date,
    HMI_prettify_Header,
    HMI_prettify_line,
)

# TODO


def test_prettify_cell_and_line():
    data = [
        {"name": "A", "value": 1.5, "flag": "ok"},
        {"name": "B", "value": 2.0, "flag": "bad"},
    ]

    pretty = HMI_prettify_cell(data, "value", "V", position="end")
    assert pretty[0]["value"].endswith("V")

    marked = HMI_prettify_line(
        data, "name", "flag", "bad", "!", compare_type="equals", position="end"
    )
    assert marked[1]["name"].endswith("!")


def test_prettify_header_character_and_date():
    data = [
        {"date": "19-11-2012", "text": "A/B"},
        {"date": "20-12-2013", "text": "C/D"},
    ]

    headered = HMI_prettify_Header(data, "date", "dato")
    assert "dato" in headered[0]

    replaced = HMI_prettify_caracter(data, "text", "/", "-")
    assert replaced[0]["text"] == "A-B"

    formatted = HMI_prettify_date(data, "date", "dd-mm-yyyy", "yyyy/mm/dd")
    assert formatted[0]["date"] == "2012/11/19"
