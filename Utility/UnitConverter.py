import GabesPythonToolBox.Utility.ConfigManager as CM

class SIUnitsConverter:
    def __init__(self,config = None):
        self.config = config

    def NewCovertionTable(self,config = None):
        self.config = config
    
    def convert(self, value, from_unit, to_unit, dimension):
        # Get the conversion factor for the dimension (e.g., length, mass, etc.)
        if dimension not in self.config:
            raise ValueError(f"Unknown dimension: {dimension}")
        
        dimension_config = self.config[dimension]
        
        # Check if both the from_unit and to_unit exist in the dimension configuration
        if from_unit not in dimension_config or to_unit not in dimension_config:
            raise ValueError(f"Unknown units: {from_unit} or {to_unit}")
        
        # Get the conversion coefficient for the from and to units
        from_coefficient = dimension_config[from_unit]["coefficient"]
        to_coefficient = dimension_config[to_unit]["coefficient"]
        
        # Convert the value to the base unit (SI unit)
        value_in_base_unit = value * from_coefficient
        
        # Convert the value from the base unit to the target unit
        converted_value = value_in_base_unit / to_coefficient
        
        return converted_value 
