from GabesPythonToolBox.Utility.Debug import Debug

Debug.add_group("Showcase", True)

import GabesPythonToolBox.Utility.ConfigManager as CM
import GabesPythonToolBox.Utility.UnitConverter as UC

# Initialize the ConfigManager to load the unit conversion configuration
config_manager = CM.startConfigManager("exsampleFiles/UnitConverter/UnitConverter.json")

# Create an instance of the UnitsConverter
converter = UC.UnitsConverter(config_manager())

Debug.log("UnitConverter Showcase Started", "Header", group="Showcase")

# Example 1: Length conversion (meters -> kilometers)
length_in_meters = 1500
length_in_km = converter.convert(length_in_meters, "m", "km", "length")
Debug.log(
    f"{length_in_meters} meters is equal to {length_in_km} kilometers.",
    "Info",
    group="Showcase",
)

# Example 2: Mass conversion (grams -> kilograms)
mass_in_grams = 500
mass_in_kg = converter.convert(mass_in_grams, "g", "kg", "mass")
Debug.log(
    f"{mass_in_grams} grams is equal to {mass_in_kg} kilograms.",
    "Info",
    group="Showcase",
)

# Example 3: Time conversion (minutes -> seconds)
time_in_minutes = 5
time_in_seconds = converter.convert(time_in_minutes, "min", "s", "time")
Debug.log(
    f"{time_in_minutes} minutes is equal to {time_in_seconds} seconds.",
    "Info",
    group="Showcase",
)

# Example 4: Temperature conversion (Celsius -> Fahrenheit)
temp_in_celsius = 25
try:
    temp_in_fahrenheit = converter.convert(temp_in_celsius, "C", "F", "temperature")
    Debug.log(
        f"{temp_in_celsius}°C is equal to {temp_in_fahrenheit}°F.",
        "Info",
        group="Showcase",
    )
except Exception as e:
    Debug.log(
        f"Temperature conversion not implemented yet: {e}", "Warning", group="Showcase"
    )

# Example 5: Custom unit conversion (G -> K, suffix example)
number = 77
try:
    new_number = converter.convert(number, "G", "K", "sufix")
    Debug.log(f"{number}G is equal to {new_number}K", "Info", group="Showcase")
except Exception as e:
    Debug.log(f"Custom unit conversion failed: {e}", "Warning", group="Showcase")

Debug.log("UnitConverter Showcase Ended", "End", group="Showcase")
