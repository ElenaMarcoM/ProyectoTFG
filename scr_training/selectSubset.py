
def selectSubset(dataset, selection_list):
    return dataset

selection_list = ["Organic compounds", "Alkyl chlorides"]
selection_string = "It has to be an organic compound and an alkyl"

# Convertimos a minúsculas para evitar problemas de mayúsculas
selection_string_lower = selection_string.lower()

# Lista para almacenar palabras clave encontradas
keywords_found = []

# Búsqueda de palabras clave parciales
for term in selection_list:
    # Dividimos las palabras de cada término
    words = term.lower().split()
    # Si alguna palabra está en el string, la guardamos
    for word in words:
        if word in selection_string_lower:
            keywords_found.append(word)

print("Palabras clave encontradas:", keywords_found)