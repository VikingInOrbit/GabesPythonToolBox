def read_csv(file_path,seperator_symbol:str = ',',float_symbol:str = '.'):
    data = [] #saving data as list of dictionaries
    header = [] 

    with open(file_path, 'r', encoding='utf-8') as csv_file:


        #make seperator "," from seperator_symbol and make float_symbol to "." simultainulsy
        #remove whitspace 
        #remove begining end end seporator ,header,header2, (remove seproators not between headers)
        #seperator_symbol = ","

        header = csv_file.readline().strip().split(seperator_symbol)
        for line in csv_file:  
            values = line.strip().split(";")
            row = {header[i]: values[i] for i in range(len(header))}
            data.append(row)
    return data 
