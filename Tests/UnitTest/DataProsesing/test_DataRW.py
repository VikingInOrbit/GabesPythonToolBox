from GabesPythonToolBox.DataProsesing import csvDataPipeline
from GabesPythonToolBox.DataProsesing.DataRW import read_data, write_data


# TODO
def test_csv_data_pipeline_import():
    assert csvDataPipeline is not None


def test_write_and_read_json(tmp_path):
    path = tmp_path / "sample.json"
    data = [{"name": "A", "value": 1}]

    write_data(str(path), data)
    loaded = read_data(str(path))

    assert loaded == data
