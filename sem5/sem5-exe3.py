def vogal(letra):
    ehvogal = False
    vogais = ["a","e","i","o","u","A","E","I","O","U"]
    for x in vogais:
        if (letra == x):
            ehvogal = True
    
    return ehvogal

print(vogal("p"))
