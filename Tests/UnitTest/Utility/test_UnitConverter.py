import pytest
from GabesPythonToolBox.Utility.UnitConverter import *
from GabesPythonToolBox.Tests.UnitTestComon.UntTestUtility import Nothing
#TODO

config = '''{"time": {
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
}}'''

confi2 = '''"length": {
    "m": {"coefficient": 1},
    "km": {"coefficient": 1e3},
    "cm": {"coefficient": 1e-2},
    "mm": {"coefficient": 1e-3},
    "mile": {"coefficient": 1609.34},
    "yard": {"coefficient": 0.9144},
    "inch": {"coefficient": 0.0254}
},
"mass": {
    "kg": {"coefficient": 1},
    "g": {"coefficient": 1e-3},
    "mg": {"coefficient": 1e-6},
    "lb": {"coefficient": 0.453592},
    "oz": {"coefficient": 0.0283495}
}'''

def test_doc():
    UC = UnitsConverter(config)
    assert True

def test_init():
    ...

def test_convert_simple(): 
    UC = UnitsConverter(config)

    test = 60
    con = UC.convert(test, 's', 'min', 'time')
    assert con == 1 #cheks from base to nr

    test = 1
    con = UC.convert(test, 'min', 's', 'time')
    assert con == 60 #cheks from nr to base


def test_convert_scaler():
    UC = UnitsConverter(config)
    test = 60
    con = UC.convert(test, 'min', 'hr', 'time')
    assert con == 1

def test_convert_offser():
    ...

def test_convert_mixsed():
    ...

def test_Change_config():
    ...