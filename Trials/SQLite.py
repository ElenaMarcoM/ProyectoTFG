import sqlite3
from pathlib import Path

# TODO: Comprobar código con Guillermo

# Obtener la ruta absoluta del directorio del proyecto, subiendo dos niveles
project_dir = Path(__file__).resolve().parent.parent

# Ruta a la base de datos existente en la carpeta "externalSources"
database_path = project_dir / 'externalSources' / 'all_classifiedMINI.db'

# Verificar si la base de datos existe
print("Ruta generada:", database_path.resolve())
if not database_path.exists():
    print(f"Error: La base de datos no se encuentra en {database_path}")
else:
    # Conexión a la base de datos
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # Instrucción SQL para obtener todas las instancias de la columna field1
    query = "SELECT field1 FROM all_classifiedMINI"

    # Inicializar la variable field1_values para evitar problemas si la consulta falla
    field1_values = []

    try:
        # Ejecutar la consulta
        cursor.execute(query)

        # Recuperar todos los resultados
        resultados = cursor.fetchall()  # fetchall() devuelve una lista de tuplas

        # Almacenar los resultados en una lista de Python
        field1_values = [fila[0] for fila in resultados]  # Convertimos las tuplas en una lista plana

        # Imprimir los resultados
        print("Valores de field1:", field1_values)

    except sqlite3.Error as e:
        print("Error al ejecutar la consulta:", e)

    finally:
        # Cerrar la conexión
        cursor.close()
        conn.close()