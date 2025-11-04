from GabesPythonToolBox.DataProsesing.FrameHandler import FrameHandler

# Initialize FrameHandler
handler = FrameHandler(
    config_path="exsampleFiles/FrameHandler/frame_config.yaml",
    parsed_data_file="exsampleFiles/FrameHandler/temp/parsed_test.csv"
)


# Simulate live telemetry lines
live_lines = [
    "flag-1,00000001,00000001,3f8ccccd,41200000,40466666,40833333,AA",
    "flag-2,00000002,00000002,3f99999a,41a00000,40a33333,40c33333,BB",
    "flag-3,00000003,00000003,3fa66666,41f00000,40533333,40e9999a,CC",
    "flag-4,00000004,00000004,3fb33333,42200000,40accccd,41066666,DD",
    "flag-1,00000005,00000005,3fc00000,42480000,40600000,40900000,EE",
    "flag-2,00000006,00000006,3fcccccd,42700000,40b33333,40d33333,FF",
    "flag-3,00000007,00000007,3fd9999a,428c0000,406ccccd,40f66666,11",
    "flag-4,00000008,00000008,3fe66666,42a00000,40b9999a,410ccccd,22",
    "flag-1,00000009,00000009,3ff33333,42b40000,4079999a,409ccccd,33",
    "flag-2,0000000a,0000000a,40000000,42c80000,40a00000,40c00000,44",
    "flag-3,0000000b,0000000b,40066666,42dc0000,40466666,40e33333,55",
    "flag-4,0000000c,0000000c,400ccccd,42f00000,40a66666,41033333,66",
]





# Print result
for line in live_lines:
    print(line)

# Feed lines into FrameHandler
for line in live_lines:
    handler.new_line(line)

# Retrieve only new frames
live_data = handler.getLiveData()
print("Live Data:")
for frame in live_data:
    print(frame)

# Retrieve all frames
all_data = handler.getAllData()
print("\nAll Data:")
for frame in all_data:
    print(frame)

# Optionally, load existing parsed JSON
handler.load_parsed("exsampleFiles\FrameHandler\parsed_test.json")

all_data = handler.getAllData()
print("\nload_parsed:")
for frame in all_data:
    print(frame)
