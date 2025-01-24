import requests

"""
Description: 
    The following function is useb to obtain an InchI from a given InChIKey.
    Aimed at research with Classified.
Parameters:
    inchikey (string): InChIKey of a compound
Returns:
    string: InchI of a compound
"""
def get_inchi_from_inchikey(inchikey):
    url = f"https://cactus.nci.nih.gov/chemical/structure/{inchikey}/stdinchi"
    response = requests.get(url)

    if response.status_code == 200:
        return response.text.strip()
    else:
        return f"Error: Unable to fetch InChI for {inchikey}. Status code: {response.status_code}"
