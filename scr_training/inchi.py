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
def get_inchikeyComplete(partial_inchikey):
    url = f"https://cactus.nci.nih.gov/chemical/structure/{partial_inchikey}/stdinchikey"
    response = requests.get(url)
    result = response.text.strip()

    if response.status_code == 200:
        return result.split("=", 1)[1]  # Elimina el prefijo "InChIKey="
    else:
        return f"Error: Unable to fetch full InChIKey for {partial_inchikey}. Status code: {response.status_code}"
