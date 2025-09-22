from GabesPythonToolBox.Utility.Debug import Debug
from GabesPythonToolBox.DataProsesing.csvDataPipeline import * 


def main(file_path, seperator_symbol: str = ',', float_symbol: str = '.', read_from: str = "head", read_n_lines: int = 4,Topper:str=""):
    
    #Simple test bed
    Debug.log()
    Debug.log("Combine all into a data pipeline.")

    #the pipeline 

    #-----------------first we need data

    data = read_csv(file_path, seperator_symbol, float_symbol, read_from, read_n_lines)
    
    #-----------------then we need to process the data

    data = helper_column(data,'Oppslutning prosentvis','Oppslutning prosentvis ajusted',lambda x: (float(x) / count(data, 'Fylkenavn'))) #adds a new column based on a formula
    data = merge_data_by(data, 'Partinavn', ['Antall stemmer totalt',"Antall mandater",'Oppslutning prosentvis ajusted']) #merging (truncating) on key (se coments in function), and summing up all numeric values 
    data = sort_data_by(data, 'Oppslutning prosentvis ajusted', reverse=True) #sorts data by key
    data = filter_data_cutoff(data, "Oppslutning prosentvis ajusted", 4) #filters data to only show rows with value above cutoff in key
    data = rebase_data(data, ["Partinavn", 'Antall stemmer totalt',"Antall mandater"], get_column_widths(data)) #strips data to only show these keys

    #-----------------then we need to process the data del2. 
    #disse burde bli brukt til slutt får å gjøre datae penere

    data = HMI_prettify_cell(data, "Antall mandater", " md", position = "end") #endrer enkelt verdier som å sette % etter et tall
    data = HMI_prettify_line(data, "Partinavn", 'Antall stemmer totalt', 400000, "*", compare_type = "gte", position = "both") #endrer en verdi etter som hva en anden verdi er
    
    #depending on wat you want to do you can skip some of the above steps or change the order

    #-----------------finally we format and present the data
    line = format_data(data)
    print_table(line,n=0,Topper=Topper)


if __name__ == "__main__":
    

    path="exsampleFiles\party_distribution_2021-09-30.csv"
    main(path,seperator_symbol = ';', float_symbol=',',Topper="test data")
    