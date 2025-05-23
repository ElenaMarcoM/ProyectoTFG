from scr_training.Descarga_enlace import  *
from scr_training.MySQL_compound_db import  *
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import KFold
import mysql.connector
import pandas as pd

# --- DOWNLOAD ALL RESOURCES ---

# Download resources
fingerprints = download_fingerprints("https://drive.google.com/uc?export=download&id=1QQRP559jyjFUQwQVJzZNrEQtlLnIfH8v")
download_files("1W_7BjoAqTjsRd_BNuMbGyElljoKUqr0g")
download_files("1Tl0Vf2o8UsSBEVw8lGJbXi63NRYZr1r0")

compound_path = os.path.join("resources", "all_classified.tsv")

max_col = 0
with open(compound_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        col = line.rstrip('\n').split('\t')
        if len(col) > max_col:
            max_col = len(col)
print(f"Máximo número de columnas detectado: {max_col}")

column_name = [f"col_{i}" for i in range(max_col)]

our50Mcompounds = pd.read_csv(
    compound_path,
    sep='\t',
    header=None,
    names=column_name,
    engine='python',
)
# --------------------------

# --- PREPROCESSING DATA ---
conn = mysql.connector.connect( # Change depending on user...
    host='127.0.0.1',
    user='root',
    password='r0oT_e33$sChaTGTpitn2',
    database='compounds_dbTFG'
)

super_class = "Lipids and lipid-like molecules"
valid_parents = subgroup(conn, super_class)
conn.close()

valid_set = set(valid_parents)
list_compounds =[]

for index, row in our50Mcompounds.iterrows():
    fila_dict = row.to_dict()
    list_compounds.append(fila_dict)

list_valid_compounds = [
    compound for compound in list_compounds
    if any(parent in valid_set for parent in compound.values())
]

df_valid = pd.DataFrame(list_valid_compounds)
nombre_archivo = f"compounds_{super_class.replace(' ', '_')}.csv"
ruta_salida = os.path.join("resources", nombre_archivo)
df_valid.to_csv(ruta_salida, index=False)

# TODO: Associate valid compounds to fingerprint

scaler = MinMaxScaler()
fingerprints['rt'] = scaler.fit_transform(fingerprints[['rt']])

kf = KFold(n_splits=3, shuffle=True)
splits = []

for train_index, test_index in kf.split(fingerprints):
    training_set = fingerprints.iloc[train_index]
    test_set = fingerprints.iloc[test_index]
    mid = len(training_set) // 2
    train_set = training_set.iloc[:mid]
    validation_set = training_set.iloc[mid:]
    splits.append((train_set, validation_set, test_set))
    break

train_set, validation_set, test_set = splits[0]


