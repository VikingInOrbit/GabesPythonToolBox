from GabesPythonToolBox.Suporting.csvWriterLogger import write_csv

# TODO


def test_write_csv_logger(tmp_path):
    path = tmp_path / "log.csv"
    data = [{"name": "A", "value": 1.5}]

    write_csv(str(path), data, float_symbol=",")

    content = path.read_text(encoding="utf-8")
    assert "name" in content
    assert "1,5" in content
