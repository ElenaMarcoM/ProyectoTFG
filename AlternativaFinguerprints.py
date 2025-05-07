from rdkit import Chem
from rdkit.Chem import AllChem
import pandas as pd

# ----- CÓDIGO GUILLERMO -----
def inchi_to_morgan(inchi, radius=2, n_bits=2214):
    """Convierte InChI a Morgan Fingerprint."""
    mol = Chem.MolFromInchi(inchi)
    if mol:
        fp = AllChem.GetMorganFingerprintAsBitVect(mol, radius=radius, nBits=n_bits)
        return fp
    else:
        print(f"Error al convertir InChI: {inchi}")
        return None

# Ejemplo con 3 InChIs (reemplázalos con los que necesites)
inchi_list = [
    "InChI=1S/C8H10N4O2/c1-10-4-9-6-5(10)7(13)12(3)8(14)11(6)2/h4H,1-3H3",  # Cafeína
    "InChI=1S/C6H12O6/c7-1-2-3(8)4(9)5(10)6(11)12-2/h2-11H,1H2/t2-,3-,4+,5-,6+/m1/s1",  # D-Glucosa
    "InChI=1S/C9H8O4/c1-6(10)13-8-5-3-2-4-7(8)9(11)12/h2-5H,1H3,(H,11,12)"  # Aspirina
]

# Generar fingerprints
morgan_fps = []
for inchi in inchi_list:
    fp = inchi_to_morgan(inchi)
    if fp is not None:
        morgan_fps.append((inchi, fp))
