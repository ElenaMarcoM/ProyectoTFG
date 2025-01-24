import requests
import gzip
import pickle
import pandas as pd


def descargar_y_procesar_enlace(url):
    """
    Descarga un archivo .pklz desde una URL, verifica el contenido, lo descomprime y carga los datos.
    Args:
        url (str): Enlace al archivo en Google Drive.
    Returns:
        pd.DataFrame: DataFrame con el contenido del archivo, si es compatible.
    """
    try:
        # Descargar el archivo desde la URL
        print("Descargando archivo...")
        response = requests.get(url)
        response.raise_for_status()  # Verificar si la descarga fue exitosa

        # Revisar si el contenido es un archivo válido o una página HTML
        content_type = response.headers.get('Content-Type', '')
        if "html" in content_type:
            print("Error: La URL no contiene un archivo válido. Se descargó una página HTML.")
            print("Contenido descargado:")
            print(response.text[:500])  # Imprimir los primeros 500 caracteres del HTML
            return None

        # Guardar el archivo comprimido localmente
        archivo_comprimido = "archivo.pklz"
        with open(archivo_comprimido, "wb") as f:
            f.write(response.content)
        print("Archivo descargado exitosamente.")

        # Descomprimir el archivo
        archivo_descomprimido = "archivo.pkl"
        with gzip.open(archivo_comprimido, "rb") as f_in:
            with open(archivo_descomprimido, "wb") as f_out:
                f_out.write(f_in.read())
        print("Archivo descomprimido exitosamente.")

        # Cargar el contenido con pickle
        print("Cargando contenido del archivo...")
        with open(archivo_descomprimido, "rb") as f:
            data = pickle.load(f)

        # Convertir a DataFrame si es posible
        if isinstance(data, (list, dict)):
            df = pd.DataFrame(data)
            print("Contenido cargado y convertido a DataFrame.")
            return df
        else:
            print("El contenido no es compatible con DataFrame.")
            return data

    except Exception as e:
        print(f"Error: {e}")
        return None


# URL del archivo en Google Drive
url = "https://drive.google.com/uc?export=download&id=1QQRP559jyjFUQwQVJzZNrEQtlLnIfH8v"

# Llamar a la función y procesar el archivo
resultado = descargar_y_procesar_enlace(url)

# Mostrar resultado
if isinstance(resultado, pd.DataFrame):
    print("Primeras filas del DataFrame:")
    print(resultado.head())
else:
    print("Contenido del archivo:", resultado)