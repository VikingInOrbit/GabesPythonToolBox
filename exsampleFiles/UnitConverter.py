import GabesPythonToolBox.Utility.UnitConverter as UC
import GabesPythonToolBox.Utility.ConfigManager as CM

# Initialize the ConfigManager to get config
config_manager = CM.startConfigManager("exsampleFiles\SIUnitsConvertions.json") #a config manager shood be in the converter insted

# Create an instance of the SIUnitsConverter
converter = UC.UnitsConverter(config_manager())

# Example 1: Convert length from meters to kilometers
length_in_meters = 1500  # 1500 meters
length_in_km = converter.convert(length_in_meters, 'm', 'km', 'length')
print(f"{length_in_meters} meters is equal to {length_in_km} kilometers.")

# Example 2: Convert mass from grams to kilograms
mass_in_grams = 500  # 500 grams
mass_in_kg = converter.convert(mass_in_grams, 'g', 'kg', 'mass')
print(f"{mass_in_grams} grams is equal to {mass_in_kg} kilograms.")

# Example 3: Convert time from minutes to seconds
time_in_minutes = 5  # 5 minutes
time_in_seconds = converter.convert(time_in_minutes, 'min', 's', 'time')
print(f"{time_in_minutes} minutes is equal to {time_in_seconds} seconds.")

# Example 4: Convert temperature from Celsius to Fahrenheit
temp_in_celsius = 25  # 25 degrees Celsius
temp_in_fahrenheit = converter.convert(temp_in_celsius, 'C', 'F', 'temperature')
print(f"{temp_in_celsius}°C is equal to {temp_in_fahrenheit}°F.") #temp dont work yet
