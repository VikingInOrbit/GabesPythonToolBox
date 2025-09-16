from ..Utility.Debug import *
from ..DataProsesing.DataHelperFunctions import *

def print_table(line, n:int=0, Topper:str=""):
        
        print()
        total_length = len(line[0]) - 2 #accounting for | at start and end of line
        print("|" + "-" * total_length + "|")

        if Topper:
            print(f"|{Topper: ^{total_length}}|")

        print("|"+" " * total_length+"|")

        if n <= 0:
            for entry in line:
                print(f"{entry}")
        else:
            n+=2 #accounting for header and n=0
            for i in range(min(n, len(line))):
                print(line[i])
        
        print("|"+" " * total_length+"|")
        print("|" + "-" * total_length + "|")

def format_data(data,kepp_data:bool=False,cutoff:float=0):
    col_widths = get_column_widths(data)

    lines = []

    # Header row
    header_line = " | ".join(
        f"{key.ljust(col_widths.get(key, len(key)))}"
        for key in data[0].keys()
    )

    lines.append(f"|{header_line}|")
    lines.append("|" + "_" * (len(header_line)) + "|")  # underline

    # Data rows    
    for row in data:
        cells = []
        for key in data[0].keys():
            val = row.get(key, "")
            if isinstance(val, float):
                # If float, show 2 decimals unless it's an integer value
                if val.is_integer():
                    cell = f"{int(val)}"
                else:
                    cell = f"{val:.2f}"
                    
            elif isinstance(val, int):
                cell = str(val)
                
            else:
                cell = str(val)
                

            # pad to column width
            cell = cell.ljust(col_widths.get(key, len(cell)))
            cells.append(cell)

        line = " | ".join(cells)

        lines.append(f"|{line}|")

    return lines

