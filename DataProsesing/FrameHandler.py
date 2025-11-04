from copy import deepcopy
from ..DataProsesing.DataRW import read_data, write_data
from ..Utility.ConfigManager import ConfigManager
import struct


class FrameHandler:
    def __init__(self, config_path=None, parsed_data_file=None):
        """
        Initialize FrameHandler.

        :param config_path: Path to frame configuration YAML/JSON
        :param parsed_data_file: csv file path to store parsed frames
        """
        self.config_manager = ConfigManager(config_path) if config_path else None
        self.config = self.config_manager() if self.config_manager else None

        self.parsed_data_file = parsed_data_file

        self.frames_all = []      # all parsed frames
        self.frames_new = []      # new frames since last getLiveData

        if self.config and 'frames' in self.config:
            self.frame_vars = self.config['frames']
        else:
            self.frame_vars = {}

    def parse_line(self, raw_line: str):
        """Parse a single CSV line into a dict according to frame config with type conversion."""
        values = [v.strip() for v in raw_line.split(',')]
        if not values:
            return None

        # Determine frame ID from Flag field #TODO make flags bether (first 12 flag last int?)
        flag_val = values[0]
        try:
            frame_id = int(flag_val.split('-')[1])
        except Exception:
            frame_id = None

        if frame_id not in self.frame_vars:
            return None

        var_entries = self.frame_vars[frame_id]['variables']
        frame_dict = {'FrameID': frame_id}

        for i, var_entry in enumerate(var_entries):
            if i >= len(values):
                break

            val = values[i]

            # Split variable name and optional type
            if ':' in var_entry:
                var_name_raw, var_type = var_entry.split(':')
            else:
                var_name_raw, var_type = var_entry, None

            base_name= var_name_raw

            # Convert value based on type
            converted_val = val
            try:
                if var_type == 'float':
                    # CSV contains 4-byte IEEE float hex
                    converted_val = struct.unpack('>f', bytes.fromhex(val))[0]
                elif var_type == 'int':
                    converted_val = int(val, 16)  # parse 4-byte hex as int
                elif var_type == 'hex':
                    converted_val = val
            except ValueError:
                converted_val = val
            
            frame_dict[base_name] = converted_val

        return frame_dict



    def new_line(self, raw_line: str):
        """Add a live telemetry line."""
        if not raw_line.strip():
            return

        # Parse
        parsed_frame = self.parse_line(raw_line)
        if parsed_frame:
            self.frames_all.append(parsed_frame)
            self.frames_new.append(parsed_frame)

            if self.parsed_data_file: #TODO factor out
                write_data(self.parsed_data_file, [parsed_frame], mode='a',data_mode = "body")



    def getLiveData(self):
        """Return frames received since last call."""
        data = deepcopy(self.frames_new)
        self.frames_new = []
        return data

    def getAllData(self):
        """Return all parsed frames."""
        return deepcopy(self.frames_all)

    def load_raw(self, file_path): #gets raw file of frames
        NotImplementedError

    def clear(self):
        self.frames_all = []
        self.frames_new = []

    def load_parsed(self, file_path):
        """Load parsed JSON/yaml file into memory."""
        self.clear()
        data = read_data(file_path)
        if isinstance(data, list):
            for frame in data:
                self.frames_all.append(frame)
                self.frames_new.append(frame)

    def save(self, file_path): #saves hole data to new file
        NotImplementedError

    def write(self, file_path): #amendts to file
        NotImplementedError

    def combine(self, file_path): #combines data points to get more than 4 byties in a single data point. 
        NotImplementedError