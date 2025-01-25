from pyclassyfire.client import get_entity
import json
from simplejson import JSONDecodeError
from scr_training import functions
# METER NOTAS
def getParentNames(inchikey):
    """
        Description:
            The following function is used to access the db and return the InChIKey of the compounds.
        Parameters:
            dbfile (string): location of db file
        Returns:
            string: Full InChIKey of a compound
    """
    classification = get_entity(inchikey, return_format='json')
    direct_parent_names = []
    alternative_parent_names = []

    # Si la clasificación es una cadena, convertirla en JSON
    if isinstance(classification, str):
        classification = json.loads(classification)

    # Extrae el 'Direct Parent' y los 'Alternative Parents'
    direct_parent = classification.get('direct_parent')
    alternative_parents = classification.get('alternative_parents')

    # Añade el nombre del Direct Parent si existe
    if direct_parent and 'name' in direct_parent:
        direct_parent_names.append(direct_parent['name'])

    # Añade los nombres de los Alternative Parents si existen
    if alternative_parents:
        for parent in alternative_parents:
            if 'name' in parent:
                alternative_parent_names.append(parent['name'])

    return direct_parent_names,alternative_parent_names