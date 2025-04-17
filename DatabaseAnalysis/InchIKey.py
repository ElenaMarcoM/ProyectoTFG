import requests
from scr_training import functions
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
inchi = functions.get_inchikeyComplete(inchikey)
print(f"InChI asociado: {inchi}")


#Example sample from original file:

# Obtaining file location from the one of this script
