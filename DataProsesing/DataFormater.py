from ..Utility.Debug import *

def rebase_data(data, visible_keys, col_widths):
    #tar in data og keys og gir utigjen samme data men kun etter keys
    lines = []

    # Header row
    header_line = " | ".join(
        f"{key.ljust(col_widths.get(key, len(key)))}"
        for key in visible_keys
    )
    lines.append(f"|{header_line}|")

    data_new = []

    # Data rows
    for row in data:
        new_row = {key: row[key] for key in visible_keys if key in row}
        data_new.append(new_row)

    return data_new

def merge_data_by(data, sort_key, value_keys: list = ['Oppslutning prosentvis','Antall stemmeberettigede','Antall forhåndsstemmer','Antall valgtingstemmer','Antall stemmer totalt','Endring % siste tilsvarende valg','Endring % siste ekvivalente valg','Antall mandater','Antall utjevningsmandater']):
    new_data = {}
    #trunkates data by summing up values in value_keys for each unique value in sort_key

    #Fylkenummer;Fylkenavn;Kommunenummer;Kommunenavn;Stemmekretsnummer;Stemmekretsnavn;Partikode;Partinavn; 
    #value_key[Oppslutning prosentvis;Antall stemmeberettigede;Antall forhåndsstemmer;Antall valgtingstemmer;Antall stemmer totalt;Endring % siste tilsvarende valg;Endring % siste ekvivalente valg;Antall mandater;Antall utjevningsmandater;]
    
    for row in data:
        key = row[sort_key]  # e.g., district name
        if key not in new_data:
            # start a new record with 0 for all value_keys
            new_data[key] = {k: 0 for k in value_keys}
            new_data[key][sort_key] = key
        
        # add up all values in value_keys
        for value in value_keys:
            try:
                new_data[key][value] += float(row[value])
            except ValueError:
                pass  # skip if value is not numeric
    
    # convert dict back into list of dicts
    return list(new_data.values())

def sort_data_by(data, sort_key, reverse=False):
    return sorted(
        data,
        key=lambda row: row.get(sort_key, ""),
        reverse=reverse
    )

def filter_data_cutoff(data,key, cutoff,dir: bool=True): #dir is direction, if false it discards above cutoff, if true it discards below cutoff
        if dir:
            return [row for row in data if row.get(key, 0) >= cutoff]
        else:
            return [row for row in data if row.get(key, 0) < cutoff]

def helper_column(data, key, new_key, formula):

    data_new = []
    for row in data:
        # copy the row to avoid modifying original
        new_row = row.copy()
        
        # get source value, default to 0
        value = new_row.get(key, 0)
        try:
            value = float(value)
        except (ValueError, TypeError):
            value = 0
        
        # add new column
        value= formula(value)

        new_row[new_key] = value
        data_new.append(new_row)
    
    return data_new
