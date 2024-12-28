from SQLite import *
from scr_training import *
from nipype.utils.filemanip import loadpkl

moleculeList = ["AQPHBYQUCKHJLT", "SLGOCMATMKJJCE", "ADANNTOYRVPQLJ", "RYFZYYUIAZYQLC", "JOHCVVJGGSABQY"]
condition = "Organic compounds"

# if === main
#     select

dataset = "https://drive.google.com/u/0/uc?id=1QQRP559jyjFUQwQVJzZNrEQtlLnIfH8v&export=download"
selection_list = ["Organic compounds", "Alkyl chlorides"]
selection_string = "It has to be an organic compound and an alkyl"
keyword_list = []

for term in selection_list:
    keyword = term.lower().split()
    print("We have: ", keyword)
    for word in keyword:
        print(word)
        if word in selection_string.lower():
            keyword_list.append(word)
            print("saved!")

print("This were the key words:", keyword_list)

# Para abrir el pklz
res = loadpkl('C:/Users/Usuario/OneDrive - Fundación Universitaria San Pablo CEU/CEU/Curso 24-25/TFG/fingerprints.pklz')