import GabesPythonToolBox.Utility.ConfigManager as CM  # will be used in future
from ..Utility.Debug import Debug


class UnitsConverter:
    def __init__(self, config=None):
        Debug.log("UnitsConverter init", "Header", group="LIB")
        self.config = config
        Debug.log("UnitsConverter init", "End", group="LIB")

    def NewConversionTable(self, config=None):
        """Update or set a new conversion table."""
        Debug.log("NewConversionTable called", "Header", group="LIB")
        self.config = config
        Debug.log("NewConversionTable finished", "End", group="LIB")

    def convert(self, value, from_unit, to_unit, dimension):
        """
        Convert a value from one unit to another within the same dimension.

        Linear units: value * (from_coef / to_coef)
        Temperature units: ((value - from_offset) / from_coef) * to_coef + to_offset
        """
        Debug.log(f"Convert called: {value} {from_unit} -> {to_unit} ({dimension})", "Header", group="LIB")

        if dimension not in self.config:
            Debug.log(f"Unknown dimension: {dimension}", "Error", group="WarningError")
            raise ValueError(f"Unknown dimension: {dimension}")

        dim_conf = self.config[dimension]

        if from_unit not in dim_conf or to_unit not in dim_conf:
            Debug.log(f"Unknown units: {from_unit} or {to_unit}", "Error", group="WarningError")
            raise ValueError(f"Unknown units: {from_unit} or {to_unit}")

        from_conf = dim_conf[from_unit]
        to_conf = dim_conf[to_unit]

        # Determine if this is a temperature-style unit (has offset)
        if "offset" in from_conf or "offset" in to_conf:
            from_coef = from_conf.get("coefficient", 1)
            from_offset = from_conf.get("offset", 0)
            to_coef = to_conf.get("coefficient", 1)
            to_offset = to_conf.get("offset", 0)

            # Convert to base (e.g., Kelvin) then to target
            value_in_base = (value - from_offset) / from_coef
            converted = value_in_base * to_coef + to_offset
        else:
            # Linear units: simple ratio of coefficients
            converted = value * (from_conf["coefficient"] / to_conf["coefficient"])

        Debug.log(f"Conversion result: {converted}", "Info", group="LIB")
        Debug.log(f"Convert finished: {value} {from_unit} -> {converted} {to_unit}", "End", group="LIB")
        return converted
