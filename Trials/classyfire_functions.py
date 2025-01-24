import pyclassyfire.client as get_entity
import json

from DatabaseAnalysis.InchIKey import get_inchi_from_inchikey
from scr_training import inchi

# Reemplaza 'TU_INCHIKEY' con el InChIKey del compuesto de interés
inchikey = get_inchi_from_inchikey("FOBGJHFRTCZWAF")

# Obtén la clasificación en formato JSON
classification = get_entity(inchikey, return_format='json')

# Extrae el 'Direct Parent' y los 'Alternative Parents'
direct_parent = classification.get('direct_parent')
alternative_parents = classification.get('alternative_parents')

print(f"Direct Parent: {direct_parent}")
print(f"Alternative Parents: {alternative_parents}")