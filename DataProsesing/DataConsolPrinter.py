from ..Utility.Debug import *
from ..DataProsesing.DataHelperFunctions import *

#TODO shood i make the tabele be printed in the Debug format?

def print_table(line, n:int=0, Topper:str=""):
        Debug.log(f"print_table","Header",group="LIB")
    
        print()
        total_length = len(line[0]) - 2 #accounting for | at start and end of line
        Debug.log(f"Get total total_length:{total_length}","Info",group="LIB")
        print("|" + "-" * total_length + "|")

        if Topper:
            Debug.log(f"printing topper: {Topper}","Info",group="LIB")
            print(f"|{Topper: ^{total_length}}|")

        print("|"+" " * total_length+"|")

        if n <= 0:
            Debug.log(f"Print hele data","Info",group="LIB")
            for entry in line:
                print(f"{entry}")
        else:
            n+=2 #accounting for header and n=0
            Debug.log(f"print {n+2} lines","Info",group="LIB")
            for i in range(min(n, len(line))):
                print(line[i])
        
        Debug.log(f"print end","Info",group="LIB")
        print("|"+" " * total_length+"|")
        print("|" + "-" * total_length + "|")

        Debug.log(f"print_table","End",group="LIB")

def format_data(data):
    Debug.log(f"format_data","Header",group="LIB")
    
    Debug.log(f"Get column with","Info",group="LIB")
    col_widths = get_column_widths(data)

    lines = []

    # Header row
    header_line = " | ".join(
        f"{key.ljust(col_widths.get(key, len(key)))}"
        for key in data[0].keys()
    )

    Debug.log(f"make header line: {header_line}","Info",group="LIB")

    lines.append(f"|{header_line}|")
    lines.append("|" + "_" * (len(header_line)) + "|")  # underline

    Debug.log(f"format data","Info",group="LIB")
    # Data rows    
    for row in data:
        cells = []
        for key in data[0].keys():
            val = row.get(key, "")
            if isinstance(val, float):
                # If float, show 2 decimals unless it's an integer value
                if val.is_integer():
                    cell = f"{int(val)}"
                    Debug.log(f"val: {val} is integer","Info",group="LIB")
                else:
                    cell = f"{val:.2f}"
                    Debug.log(f"val: {val} is float","Info",group="LIB")
                    
            elif isinstance(val, int):
                cell = str(val)
                Debug.log(f"val: {val} is int","Info",group="LIB")
                
            else:
                cell = str(val)
                Debug.log(f"val: {val} is str","Info",group="LIB")
                

            # pad to column width
            cell = cell.ljust(col_widths.get(key, len(cell)))
            cells.append(cell)

        line = " | ".join(cells)

        Debug.log(f"finished line: {line}","Info",group="LIB")
        lines.append(f"|{line}|")

    Debug.log(f"format_data","End",group="LIB")
    return lines

