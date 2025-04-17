import requests
import sqlite3


def get_inchikeyComplete(partial_inchikey):
    """
    Obtiene el InChIKey completo a partir de una parte del mismo usando el servicio CACTUS.

    Args:
        partial_inchikey (str): Parte del InChIKey del compuesto.

    Returns:
        str: InChIKey completo si la consulta es exitosa; mensaje de error en caso contrario.
    """
    base_url = "https://cactus.nci.nih.gov/chemical/structure"
    url = f"{base_url}/{partial_inchikey}/stdinchikey"

    try:
        response = requests.get(url, timeout=5)  # Agregamos un tiempo de espera (5s)
        response.raise_for_status()  # Lanza una excepción si hay un error HTTP (4xx, 5xx)

        result = response.text.strip()

        # Verificamos si la respuesta contiene el formato esperado
        if result.startswith("InChIKey="):
            return result.split("=", 1)[1]  # Eliminamos el prefijo "InChIKey="
        else:
            return f"Error: Respuesta inesperada del servidor: {result}"

    except requests.exceptions.ConnectionError:
        return "Error: No se pudo establecer conexión con el servidor. Verifica tu conexión a internet."
    except requests.exceptions.Timeout:
        return "Error: La solicitud tardó demasiado en responder. Inténtalo nuevamente más tarde."
    except requests.exceptions.RequestException as e:
        return f"Error: Ocurrió un problema con la solicitud - {e}"



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
        nombre_tabla = "all_classifiedMINI"
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
