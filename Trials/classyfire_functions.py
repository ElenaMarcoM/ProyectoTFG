from pyclassyfire.client import get_entity
import json
from simplejson import JSONDecodeError
from scr_training import inchi

# Reemplaza 'TU_INCHIKEY' con el InChIKey del compuesto de interés
inchikey = inchi.get_inchikeyComplete("FOBGJHFRTCZWAF")
print(f"InChIKey obtenido: {inchikey}")
inchikeyValido = 'XLYOFNOQVPJJNP-UHFFFAOYSA-N'

# Obtén la clasificación en formato JSON
classification = get_entity(inchikey, return_format='json')

# Si la clasificación es una cadena, convertirla en JSON
if isinstance(classification, str):
    classification = json.loads(classification)

# Verifica el tipo de clasificación
print(f"Tipo de clasificación: {type(classification)}\n")

# Extrae el 'Direct Parent' y los 'Alternative Parents'
direct_parent = classification.get('direct_parent')
alternative_parents = classification.get('alternative_parents')

# Listas para almacenar los nombres
direct_parent_names = []
alternative_parent_names = []

# Añade el nombre del Direct Parent si existe
if direct_parent and 'name' in direct_parent:
    direct_parent_names.append(direct_parent['name'])

# Añade los nombres de los Alternative Parents si existen
if alternative_parents:
    for parent in alternative_parents:
        if 'name' in parent:
            alternative_parent_names.append(parent['name'])

# Mostrar las listas
print("Direct Parent Names:", direct_parent_names)
print("Alternative Parent Names:", alternative_parent_names)