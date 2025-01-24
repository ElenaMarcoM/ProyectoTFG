import bz2
import pickle
import pandas as pd

# Nombre del archivo (suponiendo que está en la misma carpeta que el script)
file_path = 'fingerprints.pklz'

# Paso 1: Descomprimir el archivo .pklz
try:
    with bz2.BZ2File(file_path, 'rb') as f_in:
        with open(file_path.replace('.pklz', '.pkl'), 'wb') as f_out:
            f_out.write(f_in.read())
    print("Archivo descomprimido con éxito. \n")
except Exception as e:
    print(f"Error al descomprimir el archivo: {e} \n")

# Ruta al archivo descomprimido
file_path = 'fingerprints.pkl'

# Cargar el archivo .pkl
try:
    with open(file_path, 'rb') as f:
        data = pickle.load(f)
    print("Datos cargados con éxito.")
    # Mostrar una muestra de los datos cargados
    print(data)
except Exception as e:
    print(f"Error al cargar el archivo pickle: {e} \n          ")

# Intentar cargar el archivo .pkl si contiene un DataFrame
try:
    df = pd.read_pickle(file_path)
    print("DataFrame cargado con éxito.")
    print(df.head())  # Mostrar las primeras filas del DataFrame
except Exception as e:
    print(f"Error al cargar el archivo pickle con pandas: {e}")