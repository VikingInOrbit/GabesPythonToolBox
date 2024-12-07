class SIUnitsConverter:
    conversion_factors = {
        'length': {
            'm': 1,
            'km': 1e3,
            'cm': 1e-2,
            'mm': 1e-3,
        },
        'mass': {
            'kg': 1,
            'g': 1e-3,
        },
        'time': {
            's': 1,
            'min': 60,
            'hr': 3600,
        },
        'temperature': {
            'K': 1,
            '°C': 1,
            '°F': 1,
        }
    }

    @staticmethod
    def convert(value, from_unit, to_unit, dimension):
        # Handling for temperature conversions with offsets
        if dimension == 'temperature':
            if from_unit == '°C' and to_unit == 'K':
                return value + 273.15
            elif from_unit == '°F' and to_unit == 'K':
                return (value - 32) * 5/9 + 273.15
            elif from_unit == 'K' and to_unit == '°C':
                return value - 273.15
            elif from_unit == '°F' and to_unit == '°C':
                return (value - 32) * 5/9
            elif from_unit == 'K' and to_unit == '°F':
                return (value - 273.15) * 9/5 + 32
            elif from_unit == '°C' and to_unit == '°F':
                return (value * 9/5) + 32
            else:
                raise ValueError(f"Unsupported temperature conversion from {from_unit} to {to_unit}")

        # Convert units in other dimensions (length, mass, time)
        if dimension not in SIUnitsConverter.conversion_factors:
            raise ValueError(f"Unknown dimension: {dimension}")

        if from_unit not in SIUnitsConverter.conversion_factors[dimension]:
            raise ValueError(f"Unknown from_unit: {from_unit}")

        if to_unit not in SIUnitsConverter.conversion_factors[dimension]:
            raise ValueError(f"Unknown to_unit: {to_unit}")

        # Base conversion logic
        from_factor = SIUnitsConverter.conversion_factors[dimension][from_unit]
        to_factor = SIUnitsConverter.conversion_factors[dimension][to_unit]

        base_value = value * from_factor
        return base_value / to_factor
