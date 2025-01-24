from pyclassyfire.client import get_entity
import json
from scr_training import inchi

# Reemplaza 'TU_INCHIKEY' con el InChIKey del compuesto de interés
inchikey = inchi.get_inchikeyComplete("FOBGJHFRTCZWAF")
print(inchikey)
inchikeyValido = 'XLYOFNOQVPJJNP-UHFFFAOYSA-N'

# Obtén la clasificación en formato JSON
classification = get_entity(inchikey, return_format='json')
print(type(classification), "\n")
classification = json.loads(classification)  # Convierte la cadena a JSON
print(type(classification), "\n")


# Extrae el 'Direct Parent' y los 'Alternative Parents'
direct_parent = classification.get('direct_parent')
alternative_parents = classification.get('alternative_parents')
if direct_parent and 'name' in direct_parent:
    print(f"Direct Parent: {direct_parent['name']}")
if alternative_parents and 'name' in alternative_parents:
    print(f"Alternative Parents: {alternative_parents['name']}")