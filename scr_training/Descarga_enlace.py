import gdown
import bz2
import pickle
import zipfile
import os
import shutil
import pandas as pd


def download_fingerprints(url):
    # Enlace de descarga directo de Google Drive
    compressed_path = os.path.join("resources", "fingerprints_og.pklz")

    # Descargar el archivo
    gdown.download(url, compressed_path, fuzzy=True, quiet=False)
    print(f"Descarga completada del pklz")

    # Step 1: Descomprimir correctamente el archivo .pklz
    with bz2.BZ2File(compressed_path, "rb") as f:
        data = pickle.load(f, encoding='latin1')

    # Step 2: Download decompressed pklz
    decompressed_path = os.path.join("resources", "fingerprints.pkl")
    print(f"Descarga completada del pkl")
    with open(decompressed_path, "wb") as f:
        pickle.dump(data, f)

    return data
# print(data)
# print("Tipo clase data: "+ str(type(data)))
# print("Info fila 1: " + data.loc[1])

def download_files (file_id):
    # ID del archivo en Google Drive
    url = f"https://drive.google.com/uc?id="
    url_full = url + file_id
    zip_path = "archivo.zip"
    temp_extract_folder = "archivo_descomprimido"
    final_destination = os.path.join("resources")

    # Descargar el archivo ZIP
    gdown.download(url_full, zip_path, quiet=False)

    # Descomprimir
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(temp_extract_folder)

    # Asegurarse de que la carpeta destino existe
    os.makedirs(final_destination, exist_ok=True)

    # Mover archivos desde archivo_descomprimido a resources
    for item in os.listdir(temp_extract_folder):
        s = os.path.join(temp_extract_folder, item)
        d = os.path.join(final_destination, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)

    # Limpiar: borrar ZIP y carpeta temporal
    os.remove(zip_path)
    shutil.rmtree(temp_extract_folder)






"""
# -------- TRY GUILLERMO WAY TO OBTAIN FINGERPRINTS --------
from rdkit import Chem
from rdkit.Chem import AllChem
import pandas as pd

def inchi_to_morgan(inchi, radius=2, n_bits=2214):
    ""Convierte InChI a Morgan Fingerprint.""
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

# ----------RY GUILLERMO WAY TO OBTAIN FINGERPRINTS --------
"""
