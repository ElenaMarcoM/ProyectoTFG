import bz2
import pickle
import numpy as np
print(np.__version__)

# Nombre del archivo comprimido
file_path = 'fingerprints.pklz'

# Paso 1: Descomprimir correctamente el archivo .pklz
with bz2.BZ2File("fingerprints.pklz", "rb") as f:
    data = pickle.load(f)
    print(data)


"""
# Ruta al archivo descomprimido
file_path = output_path

# Paso 2: Intentar cargar el archivo con pickle de forma segura
try:
    with open(file_path, 'rb') as f:
        data = pickle.load(f)
    print("Datos cargados con éxito.")
    print(type(data))  # Ver el tipo de dato cargado
except Exception as e:
    print(f"Error al cargar el archivo pickle: {e} \n")

# Paso 3: Intentar cargarlo como DataFrame (si aplica)
if isinstance(data, pd.DataFrame):  # Verifica si es un DataFrame antes de usar pandas
    try:
        print("DataFrame detectado, mostrando primeras filas:")
        print(data.head())
    except Exception as e:
        print(f"Error al mostrar el DataFrame: {e}")
else:
    print("El archivo descomprimido no contiene un DataFrame.")

"""