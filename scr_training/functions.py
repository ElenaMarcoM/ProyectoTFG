import requests
import sqlite3


def get_inchikeyComplete(partial_inchikey):
    """
    Description:
        The following function is useb to obtain an InchI from a given InChIKey.
        Aimed at research with Classified.
    Parameters:
        inchikey (string): partial InChIKey of a compound
    Returns:
        string: Full InChIKey of a compound
    """
    url = f"https://cactus.nci.nih.gov/chemical/structure/{partial_inchikey}/stdinchikey"
    response = requests.get(url)
    result = response.text.strip()

    if response.status_code == 200:
        return result.split("=", 1)[1]  # Elimina el prefijo "InChIKey="
    else:
        return f"Error: Unable to fetch full InChIKey for {partial_inchikey}. Status code: {response.status_code}"



def getInchiKey_fromDB (dbfile):
    """
        Description:
            The following function is used to access the db and return the InChIKey of the compounds.
        Parameters:
            dbfile (string): location of db file
        Returns:
            string: Full InChIKey of a compound
        """
    try:
        # Conexión a la base de datos
        conexion = sqlite3.connect(dbfile)
        cursor = conexion.cursor()

        # Consulta para obtener la primera columna de la tabla
        nombre_tabla = "all_classifiedMINI"  # Cambia esto al nombre de tu tabla
        consulta = f"SELECT * FROM {nombre_tabla} LIMIT 1"
        cursor.execute(consulta)

        # Obteniendo el nombre de la primera columna
        primera_columna = cursor.description[0][0]

        # Extrayendo los valores de la primera columna
        consulta_primera_columna = f"SELECT {primera_columna} FROM {nombre_tabla}"
        cursor.execute(consulta_primera_columna)

        # Creando una lista con los valores de la primera columna
        list_inke = [fila[0] for fila in cursor.fetchall()]

        # Mostrando la lista creada
        return list_inke

    except sqlite3.Error as e:
        print(f"Error al acceder a la base de datos: {e}")

    finally:
        # Cerrar la conexión
        if conexion:
            conexion.close()
