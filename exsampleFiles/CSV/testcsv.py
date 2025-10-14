from GabesPythonToolBox.Utility.Debug import Debug
Debug.add_group('Showcase', True)

from GabesPythonToolBox.DataProsesing.csvDataPipeline import *

Debug.log("CSV Data Pipeline Showcase", message_type="Header", group="Showcase")


def main(
    file_path,
    seperator_symbol: str = ',',
    float_symbol: str = '.',
    read_from: str = "head",
    read_n_lines: int = 4,
    encoding:str = "utf-8",
    Topper: str = ""
):
    Debug.log("Main CSV Pipeline", "Header", group="Showcase")
    
    Debug.log("Step 1: Reading CSV data", "Info", group="Showcase")
    data = read_data(file_path, seperator_symbol=seperator_symbol, float_symbol=float_symbol, read_from=read_from, read_n_lines=read_n_lines,encoding=encoding)
    Debug.log(f"Initial data read ({len(data)} rows)", "Info", group="Showcase")

    Debug.log("Step 2: Processing data", "Info", group="Showcase")
    data = helper_column(data,'Oppslutning prosentvis','Oppslutning prosentvis ajusted',lambda x: (float(x) / count(data, 'Fylkenavn')))
    Debug.log("Added adjusted percentage column", "Info", group="Showcase")

    data = merge_data_by(data,'Partinavn',['Antall stemmer totalt', "Antall mandater", 'Oppslutning prosentvis ajusted'])
    Debug.log("Merged data by 'Partinavn'", "Info", group="Showcase")

    data = sort_data_by(data, 'Oppslutning prosentvis ajusted', reverse=True)
    Debug.log("Sorted data by adjusted percentage descending", "Info", group="Showcase")

    data = filter_data_cutoff(data, "Oppslutning prosentvis ajusted", 4)
    Debug.log("Filtered data to show rows above cutoff 4%", "Info", group="Showcase")

    data = rebase_data(data, ["Partinavn", 'Antall stemmer totalt', "Antall mandater"], get_column_widths(data))
    Debug.log("Rebased data to selected columns", "Info", group="Showcase")

    Debug.log("Step 3: HMI Prettify", "Info", group="Showcase")
    data = HMI_prettify_cell(data, "Antall mandater", " md", position="end")
    Debug.log("Prettified 'Antall mandater' column", "Info", group="Showcase")

    data = HMI_prettify_line(data,"Partinavn",'Antall stemmer totalt',400000,"*",compare_type="gte",position="both"
    )
    Debug.log("Applied line-level HMI formatting", "Info", group="Showcase")

    Debug.log("Step 4: Presenting data", "Info", group="Showcase")
    line = data
    print_table(line, n=0, Topper=Topper, edje_seperator="|", data_seperator="|")
    Debug.log("Data table displayed", "Info", group="Showcase")

    Debug.log("Main CSV Pipeline", "End", group="Showcase")

    write_data("exsampleFiles/CSV/temp/party_distributionnew.csv",data=data)


if __name__ == "__main__":
    Debug.log("Running CSV Data Pipeline Showcase", "Header", group="Showcase")
    
    path = "exsampleFiles/CSV/party_distribution_2021-09-30.csv"
    main(path, seperator_symbol=';', float_symbol=',', Topper="Test Data")
    
    Debug.log("CSV Data Pipeline Showcase Complete", "End", group="Showcase")
