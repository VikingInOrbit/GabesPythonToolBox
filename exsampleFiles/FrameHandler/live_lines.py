import struct
import json

# Load parsed JSON
with open("exsampleFiles/FrameHandler/parsed_test.json", "r") as f:
    parsed_data = json.load(f)

live_lines = []

for frame in parsed_data:
    # Convert values to 4-byte representations
    flag = frame['Flag']  # keep string
    count = struct.pack('>I', int(frame['Count'])).hex()      # 4-byte int
    time = struct.pack('>I', int(frame['Time'])).hex()        # 4-byte int

    def to_float32_hex(val):
        return struct.pack('>f', float(val)).hex()  # 4-byte float

    values_hex = []

    # frame variables: var1, var2.x, var3/var5, var4/var6/var7/var8
    for key in frame:
        if key in ['FrameID', 'Flag', 'Count', 'Time', 'Cs']:
            continue
        if 'float' in str(type(frame[key])) or isinstance(frame[key], float):
            values_hex.append(to_float32_hex(frame[key]))
        else:
            values_hex.append(struct.pack('>I', int(frame[key])).hex())

    cs = frame['Cs']  # checksum string

    line = ",".join([flag, count, time] + values_hex + [cs])
    live_lines.append(line)

# Print live_lines as Python list
print("live_lines = [")
for l in live_lines:
    print(f'    "{l}",')
print("]")
