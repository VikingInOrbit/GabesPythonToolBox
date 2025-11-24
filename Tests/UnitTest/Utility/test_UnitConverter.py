import json

import pytest

from GabesPythonToolBox.Utility.UnitConverter import *
from Tests.UnitTestComon.UntTestUtility import Nothing, read_config

# TODO

config = """{"time": {
    "s": {"coefficient": 1},
    "min": {"coefficient": 60},
    "hr": {"coefficient": 3600},
    "day": {"coefficient": 86400},
    "week": {"coefficient": 604800}
},
"temperature": {
    "K": {"coefficient": 1, "offset": 0},
    "C": {"coefficient": 1, "offset": -273.15},
    "F": {"coefficient": 1.8, "offset": -459.67}
}}"""


def test_doc():
    UC = UnitsConverter(read_config(config))
    assert True


def test_init():
    UC = UnitsConverter(read_config(config))
    assert UC.config == read_config(config)


def test_convert_simple():
    UC = UnitsConverter(read_config(config))
    test = 60
    con = UC.convert(test, "s", "min", "time")
    assert con == 1  # cheks from base to nr

    test = 1
    con = UC.convert(test, "min", "s", "time")
    assert con == 60  # cheks from nr to base


def test_convert_scaler():
    UC = UnitsConverter(read_config(config))
    test = 60
    con = UC.convert(test, "min", "hr", "time")
    assert con == 1


def test_init_with_dict():
    cfg = read_config(config)
    UC = UnitsConverter(cfg)
    assert UC.config == cfg


def test_convert_simple_with_dict():
    cfg = read_config(config)
    UC = UnitsConverter(cfg)
    assert UC.convert(60, "s", "min", "time") == pytest.approx(1)
    assert UC.convert(1, "min", "s", "time") == pytest.approx(60)


def test_convert_scaler_with_dict():
    cfg = read_config(config)
    UC = UnitsConverter(cfg)
    assert UC.convert(60, "min", "hr", "time") == pytest.approx(1)


def test_temperature_conversions():
    cfg = read_config(config)
    UC = UnitsConverter(cfg)
    # Celsius -> Kelvin and back
    assert UC.convert(0, "C", "K", "temperature") == pytest.approx(273.15)
    assert UC.convert(273.15, "K", "C", "temperature") == pytest.approx(0)
    # Fahrenheit -> Celsius (32°F == 0°C)
    assert UC.convert(32, "F", "C", "temperature") == pytest.approx(0)


def test_invalid_dimension_and_unit_errors():
    cfg = read_config(config)
    UC = UnitsConverter(cfg)
    with pytest.raises(ValueError):
        UC.convert(
            1, "m", "km", "length"
        )  # 'length' not present in provided config string
    with pytest.raises(ValueError):
        UC.convert(1, "s", "unknown_unit", "time")


def test_NewConversionTable_and_usage():
    cfg = read_config(config)
    UC = UnitsConverter(cfg)
    new_cfg = {"length": {"m": {"coefficient": 1}, "km": {"coefficient": 1000}}}
    UC.NewConversionTable(new_cfg)
    assert UC.config == new_cfg
    # 1000 m -> 1 km using stored coefficients
    assert UC.convert(1000, "m", "km", "length") == pytest.approx(1)
