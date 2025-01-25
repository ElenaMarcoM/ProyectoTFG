import requests
import sqlite3
from Trials.classyfire_functions import getParentNames
from scr_training import functions
from Trials import  functionsSQL

# Finds the whole InChIKey in order to use for the Classyfire API
listinchikey = functions.getInchiKey_fromDB('all_classifiedMINI.db')
list_correctInchiKey = []
for inchikey in listinchikey:
    list_correctInchiKey.append(functions.get_inchikeyComplete(inchikey))
print("25%\n")

# Create the database
functionsSQL.createSQL()
print("Database created\n")

# Insert values
for inchikey in list_correctInchiKey:
    dirpar, altpar = getParentNames(inchikey)
    functionsSQL.insertar_datos('AllParents.db', 'Parents', inchikey, dirpar, altpar)

print("\n End of process")