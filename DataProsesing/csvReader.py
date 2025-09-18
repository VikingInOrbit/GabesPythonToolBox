def process_line(line: str, seperator_symbol: str = ',', float_symbol: str = '.') -> list:
    line = line.strip()
    if not line:
        return []

    if seperator_symbol != ',':
        line = line.replace(float_symbol, ',')

    if float_symbol != '.':
        line = line.replace(float_symbol, '.')

    values = [v.strip() for v in line.split(seperator_symbol)]
    return values

def read_csv(file_path, seperator_symbol: str = ',', float_symbol: str = '.', read_from: str = "", read_n_lines: int = 0,encoding:str='utf-8'):

    data = []
    header = []

    with open(file_path, 'r', encoding=encoding) as csv_file:

        # Read header
        header_line = csv_file.readline()
        header = process_line(header_line, seperator_symbol, float_symbol)

        # Decide which lines to read
        if read_from == "head" and read_n_lines > 0:
            lines = []
            for _ in range(read_n_lines):
                line = csv_file.readline()
                if not line:  # stop if end of file
                    break
                lines.append(line)
            
        elif read_from == "tail" and read_n_lines > 0:
            buffer = []
            for line in csv_file:
                if len(buffer) < read_n_lines:
                    buffer.append(line)
                else:
                    buffer.pop(0)
                    buffer.append(line)
            lines = buffer

        else:
            lines = csv_file

        # Process each line using the helper
        for line in lines:
            values = process_line(line, seperator_symbol, float_symbol)
            row = {header[i]: values[i] for i in range(len(header))}
            data.append(row)

    return data
