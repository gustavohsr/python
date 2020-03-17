def remove_repetidos(lista):
    newlista = []
    
    for index in lista:
        if index not in newlista:
            newlista.append(index)
    return newlista

lista = [2, 4, 2, 2, 3, 3, 1]

print (sorted(remove_repetidos(lista)))
