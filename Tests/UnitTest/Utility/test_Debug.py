import os
import re
from types import SimpleNamespace

import pytest

from GabesPythonToolBox.Utility import Logger
from GabesPythonToolBox.Utility.Debug import Debug, LogGroup, LogType


def reset_debug(monkeypatch):
    monkeypatch.setattr(Debug, "debug_enabled", True)
    monkeypatch.setattr(Debug, "logger_enabled", False)
    monkeypatch.setattr(Debug, "verbosity", 1)
    monkeypatch.setattr(
        Debug,
        "groups",
        {
            LogGroup.LIB.value: False,
            LogGroup.LIB_Debug.value: False,
            LogGroup.ExampleFiles.value: False,
            LogGroup.WarningError.value: True,
            LogGroup.Showcase.value: True,
        },
    )


@pytest.mark.parametrize(
    "message_type,text",
    [
        ("Header", "Custom Header Message"),
        ("Error", "This is an error message"),
        ("Fail", "This is a failed message"),
        ("Unachievable", "This is a Unachievable message"),
        ("Success", "This is a success message"),
        ("Warning", "This is a warning message"),
        ("Info", "This is an info message"),
        ("InProgress", "This is an in-progress message"),
        ("None", "This is an None Format message"),
        ("End", "This is an End message"),
        ("-", "This has a wrong type"),
    ],
)
def test_string_message_types_print(monkeypatch, capsys, message_type, text):
    reset_debug(monkeypatch)
    Debug.set_debug_enabled(True, verbosity=1)
    Debug.log(text, message_type=message_type)
    out = capsys.readouterr().out
    assert text in out


def test_enum_and_old_style_message_types(monkeypatch, capsys):
    reset_debug(monkeypatch)
    Debug.set_debug_enabled(True, verbosity=1)

    Debug.log("New style message", message_type=LogType.Success)
    assert "New style message" in capsys.readouterr().out

    Debug.log("Old style message", message_type="Success")
    assert "Old style message" in capsys.readouterr().out


def test_group_filtering_and_toggle(monkeypatch, capsys):
    reset_debug(monkeypatch)
    Debug.set_debug_enabled(True, verbosity=1)

    Debug.add_group("LIB", True)
    Debug.add_group("Database", False)
    Debug.add_group("Showcase", True)

    # LIB enabled -> prints
    Debug.log("show lib", message_type="Info", group="LIB")
    assert "show lib" in capsys.readouterr().out

    # Database disabled -> suppressed
    Debug.log("hide db", message_type="Info", group="Database")
    assert "hide db" not in capsys.readouterr().out

    # enable Database -> prints
    Debug.enable_group("Database")
    Debug.log("show db", message_type="Info", group="Database")
    assert "show db" in capsys.readouterr().out

    # disable LIB -> suppressed, then re-enable -> prints
    Debug.disable_group("LIB")
    Debug.log("now hide lib", message_type="Info", group="LIB")
    assert "now hide lib" not in capsys.readouterr().out

    Debug.enable_group("LIB")
    Debug.log("now show lib", message_type="Info", group="LIB")
    assert "now show lib" in capsys.readouterr().out


def test_list_groups_add_remove_affects_listing(monkeypatch, capsys):
    reset_debug(monkeypatch)
    Debug.set_debug_enabled(True, verbosity=1)

    Debug.log("list groups", message_type="Info", group="Showcase")
    Debug.log(Debug.list_groups(), message_type="Info", group="Showcase")
    out = capsys.readouterr().out
    assert LogGroup.Showcase.value in out or LogGroup.WarningError.value in out

    Debug.add_group("test")
    Debug.log(Debug.list_groups(), message_type="Info", group="Showcase")
    out = capsys.readouterr().out
    assert "'test'" in out or '"test"' in out

    Debug.remove_group("test")
    Debug.log(Debug.list_groups(), message_type="Info", group="Showcase")
    out = capsys.readouterr().out
    assert "'test'" not in out and '"test"' not in out


def test_set_log_enabled_uses_Logger(monkeypatch):
    reset_debug(monkeypatch)
    calls = []

    def fake_start(cls, path=None):
        calls.append(("start", path))

    def fake_log(cls, message, message_type=None, group=None, verbose=None):
        calls.append(
            ("log", message, message_type, group, hasattr(verbose, "filename"))
        )

    # patch the Logger class methods on the module's Logger class object
    monkeypatch.setattr(Logger.Logger, "start_logger", classmethod(fake_start))
    monkeypatch.setattr(Logger.Logger, "log", classmethod(fake_log))

    # call twice to exercise both enabled=False and enabled=True paths
    Debug.set_log_enabled(path="somepath", enabled=False)
    Debug.set_log_enabled(path="somepath", enabled=True)
    assert Debug.logger_enabled is True

    Debug.log("hello logger", message_type=LogType.Info, group=LogGroup.LIB)
    assert any(c[0] == "log" and c[1] == "hello logger" for c in calls)


@pytest.mark.parametrize(
    "verbosity, expect_file, expect_func, expect_lineno",
    [
        (1, False, False, False),
        (2, True, False, False),
        (3, True, True, False),
        (4, True, True, True),
    ],
)
def test_verbosity_levels(
    monkeypatch, capsys, verbosity, expect_file, expect_func, expect_lineno
):
    reset_debug(monkeypatch)
    Debug.set_debug_enabled(True, verbosity=verbosity)
    Debug.log("vtest", message_type=LogType.Info)
    out = capsys.readouterr().out
    assert "vtest" in out
    if expect_file:
        assert os.path.basename(__file__) in out
    else:
        assert os.path.basename(__file__) not in out
    if expect_func:
        assert "test_verbosity_levels" in out
    if expect_lineno:
        # check there's a colon + digits somewhere near the end (simple heuristic)
        assert re.search(r":\s*\d+", out)


def test_unknown_message_type_default_branch_shows_file_and_marker(monkeypatch, capsys):
    reset_debug(monkeypatch)
    Debug.set_debug_enabled(True, verbosity=4)
    Debug.log("fallback", message_type="SOMETHING_UNKNOWN")
    out = capsys.readouterr().out
    assert "fallback" in out
    assert os.path.basename(__file__) in out
    # example code prints a "..." marker when building fallback verbose info
    assert "..." in out
