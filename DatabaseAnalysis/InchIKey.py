import requests
import csv
import os
from pathlib import Path

"""
Description: 
    The following function is useb to obtain an InchI from a given InChIKey.
    Aimed at research with Classified.
Parameters:
    inchikey (string): InChIKey of a compound
Returns:
    string: InchI of a compound
"""
def get_inchi(inchikey):
    url = f"https://cactus.nci.nih.gov/chemical/structure/{inchikey}/stdinchi"
    response = requests.get(url)

    if response.status_code == 200:
        return response.text.strip()
    else:
        return f"Error: Unable to fetch InChI for {inchikey}. Status code: {response.status_code}"


# Example one compound:
inchikey = "FOBGJHFRTCZWAF"
inchi = get_inchi_from_inchikey(inchikey)
print(f"InChI asociado: {inchi}")


#Example sample from original file:

# Obtaining file location from the one of this script
# TODO: Revise why it doesn't detect file
dir_base = Path(__file__).resolve().parent  # Obtain directory from this file
os.chdir(dir_base)
dir_file = dir_base.parent / 'externalSources' / 'all_classifiedMINI.tsv'
print(dir_file, "\n¿Existe?", os.path.isfile(dir_file))

# List of InChIKey and InChI
inchikey_list = []
inchi_list = []

# Read file and take InChIKeys
try:
    with open(dir_file, mode='r', encoding='utf-8') as file:
        tsv_reader = csv.reader(file, delimiter='\t')
        for fila in tsv_reader:
            if fila:  # Verifica que la fila no esté vacía
                inchikey_list.append(fila[0])

    print("InChIKeys: ", inchikey_list)
except FileNotFoundError:
    print(f"Error: No se encontró el archivo en la ruta especificada: {dir_file}")
except Exception as e:
    print(f"Se produjo un error inesperado: {e}")