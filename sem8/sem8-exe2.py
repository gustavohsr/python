def soma_elementos(lista):
    soma = 0
    for i in range(len(lista)):
        soma = soma + lista[i]

    return soma
    
lista = [1, 1, 1, 1, 1, 1, 1]

print(soma_elementos(lista))