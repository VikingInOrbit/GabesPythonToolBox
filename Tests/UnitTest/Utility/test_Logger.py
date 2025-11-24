import csv
import os
import sys
from datetime import datetime
from types import ModuleType, SimpleNamespace

import pytest

from GabesPythonToolBox.Utility.Logger import Logger


def reset_logger_state():
    Logger.path = None
    Logger.encoding = None
    Logger.first_write = True


def test_before_start_raises():
    reset_logger_state()
    with pytest.raises(RuntimeError):
        Logger.log("no start")


def test_default_folder(tmp_path, monkeypatch):
    reset_logger_state()
    # run in tmp_path so default "log/" is created there
    monkeypatch.chdir(tmp_path)
    Logger.start_logger(file_path="", character_encoding="utf-8")

    assert Logger.path is not None
    # path should be inside tmp_path / "log_*.csv"
    assert str(tmp_path) in Logger.path
    assert os.path.exists(Logger.path)
    with open(Logger.path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        assert next(reader) == Logger.headers


def test_existing_file_kept(tmp_path):
    reset_logger_state()
    file_path = tmp_path / "existing.csv"
    file_path.write_text("PREEXISTING\n", encoding="utf-8")

    # start_logger should respect existing file and not rewrite header
    Logger.start_logger(file_path=str(file_path), character_encoding="utf-8")
    assert Logger.path == os.path.abspath(str(file_path))
    content = open(Logger.path, encoding="utf-8").read()
    assert "PREEXISTING" in content


def test_dir_only_creates_file(tmp_path):
    reset_logger_state()
    dir_path = str(tmp_path / "logs") + os.sep
    Logger.start_logger(file_path=dir_path, character_encoding="utf-8")

    assert Logger.path is not None
    assert os.path.isdir(os.path.dirname(Logger.path))
    assert os.path.exists(Logger.path)
    with open(Logger.path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        assert next(reader) == Logger.headers


def test_save_modes_and_log(tmp_path, monkeypatch):
    reset_logger_state()
    logfile = str(tmp_path / "log.csv")
    Logger.start_logger(file_path=logfile)

    module_name = "GabesPythonToolBox.Suporting.csvWriterLogger"
    mod = ModuleType(module_name)
    calls = []

    def fake_write_csv(path, data, mode, data_mode):
        calls.append({"path": path, "data": data, "mode": mode, "data_mode": data_mode})

    mod.write_csv = fake_write_csv
    monkeypatch.setitem(sys.modules, module_name, mod)

    # Current state after start_logger: Logger.first_write == False -> save_to_file should treat as first write (mode "w", data_mode "all")
    sample_data1 = [{"message": "first"}]
    Logger.save_to_file(sample_data1)
    assert calls[-1]["path"] == Logger.path
    assert calls[-1]["mode"] == "w"
    assert calls[-1]["data_mode"] == "all"
    assert calls[-1]["data"] == sample_data1
    # save_to_file sets Logger.first_write = True
    assert Logger.first_write is True

    # Force the alternate branch by setting first_write True before calling save_to_file
    Logger.first_write = True
    sample_data2 = [{"message": "second"}]
    Logger.save_to_file(sample_data2)
    # now first_write was True -> mode "a","body"
    assert calls[-1]["mode"] == "a"
    assert calls[-1]["data_mode"] == "body"
    assert calls[-1]["data"] == sample_data2

    # Test Logger.log building an entry (verbose=None)
    Logger.log("hello", message_type="INFO", group="grp", verbose=None)
    last = calls[-1]
    entry = last["data"][0]
    assert entry["message"] == "hello"
    assert entry["message_type"] == "INFO"
    assert entry["group"] == "grp"
    assert entry["filename"] == ""
    assert entry["filepath"] == ""
    assert entry["lineno"] == 0
    datetime.fromisoformat(entry["timestamp"])  # should not raise

    # Test Logger.log with a verbose object containing filename and lineno
    verbose = SimpleNamespace(filename=str(tmp_path / "sub" / "file.py"), lineno=42)
    Logger.log("v", verbose=verbose)
    entry2 = calls[-1]["data"][0]
    assert entry2["filename"] == os.path.basename(verbose.filename)
    assert entry2["filepath"] == os.path.dirname(verbose.filename)
    assert entry2["lineno"] == 42
