import sqlite3
import json

def createSQL ():
    """
        Description:
            The following function is useb to obtain an InchI from a given InChIKey.
            Aimed at research with Classified.
        Parameters:
            inchiK (str): Full InChIKey of a compound
            dirpar (str): Direct Parent name
            altpar (list): All Alternative Parents names
        Returns:
            gfj
    """
    # Nombre del archivo de la base de datos
    db_path = 'AllParents.db'
    try:
        # Conexión a la base de datos
        conexion = sqlite3.connect(db_path)
        cursor = conexion.cursor()

        # Crear la tabla
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Parents (
                InChIKey TEXT,
                Direct_Parent TEXT,
                Alternative_Parent TEXT
            )
        """)
        print("Tabla creada correctamente.")

    except sqlite3.Error as e:
        print(f"Error al acceder a la base de datos: {e}")

    finally:
        # Cerrar la conexión
        if conexion:
            conexion.close()

def insertar_datos(db_path, tabla, columna1, columna2, columna3):
    """
    Description:
            The following function is used to insert values in an existing table.

    Args:
        db_path (str): Ruta al archivo de la base de datos.
        tabla (str): Nombre de la tabla.
        columna1 (str): Valor de la primera columna (cadena de texto).
        columna2 (str): Valor de la segunda columna (cadena de texto).
        columna3 (list): Valor de la tercera columna (lista).
    """
    try:
        # Conexión a la base de datos
        conexion = sqlite3.connect(db_path)
        cursor = conexion.cursor()


        # Consulta SQL para insertar datos
        consulta = f"INSERT INTO {tabla} (InChIKey, Direct_Parent, Alternative_Parent) VALUES (?, ?, ?)"
        cursor.execute(consulta, (columna1, json.dumps(columna2), json.dumps(columna3)))

        # Confirmar los cambios
        conexion.commit()
        print(f"Datos insertados correctamente en la tabla '{tabla}'.")

    except sqlite3.Error as e:
        print(f"Error al insertar datos en la base de datos: {e}")

    finally:
        # Cerrar la conexión
        if conexion:
            conexion.close()

