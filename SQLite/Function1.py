import sqlite3

def funcion1(molecules,condition):
    conn = sqlite3.connect("all_classifiedMINI.db")
    cursor = conn.cursor()
    query = "SELECT * FROM all_classifiedMINI WHERE field1 = ? AND field2= ?"
    try:
        cursor.execute(query, (molecules,condition))
        mol = cursor.fetchall()
        print("The molecule", mol[0], "Has desired condition", condition)
    except sqlite3.Error as e:  # Si no encuentra un parámetro devuelve string vacio
        print("There has been an issue:", e)
    finally:
        print("---")


funcion1("AQPHBYQUCKHJLT", "Organi compounds")
