import sqlite3

def funcion1(molecules,condition):
    # Conexion con db
    conn = sqlite3.connect("all_classifiedMINI.db")
    cursor = conn.cursor()
    # Instrucción
    query = "SELECT * FROM all_classifiedMINI WHERE field1 = ? AND field2= ?"
    try:
        cursor.execute(query, (molecules,condition))
        mol = cursor.fetchall()
        if mol != None:
            print("The molecule", molecules, "Has desired condition", condition)

    except sqlite3.Error as e:  # Si no encuentra un parámetro devuelve string vacio
        print("There has been an issue:", e)
    except Exception as er:
        print("There has been an error:", er)
    finally:
        print("---")

def funcion2(molecules, condition):
    # Conexion con db
    conn = sqlite3.connect("all_classifiedMINI.db")
    cursor = conn.cursor()
    # Instrucción
    query = "SELECT * FROM all_classifiedMINI WHERE field1 = ? AND field2= ? AND field3= ?"
    try:
        cursor.execute(query, (molecules, condition[0]), condition[1])
        mol = cursor.fetchall()
        if mol != None:
            print("The molecule", molecules, "Has desired condition", condition)

    except sqlite3.Error as e:  # Si no encuentra un parámetro devuelve string vacio
        print("There has been an issue:", e)
    except Exception as er:
        print("There has been an error:", er)
    finally:
        print("---")

