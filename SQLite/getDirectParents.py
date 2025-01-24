from scr_training import inchi
from pyclassyfire.client import get_entity
import json

def getDirectParents(inchikey):
    """
    Description:
        The following function is useb to obtain an InchI from a given InChIKey.
        Aimed at research with Classified.
    Parameters:
        inchikey (string): Complete InChIKey of a compound
    Returns:
        dirparents: list with names of all direct parents of a compound
    """

    # Obtain informatin from Classyfire API
    classification = get_entity(inchikey, return_format='json')

    #Transform given str into json type
    classification = json.loads(classification)

    # Extract "Direct parent(s)" name
    dirparents = []
    direct_parent = classification.get('direct_parent')
    if direct_parent and 'name' in direct_parent:
        dirparents.append(direct_parent['name'])
