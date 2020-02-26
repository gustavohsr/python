def éPrimo(k):
    i = 2
    primo = True
    while (i<k):
        if (k%i == 0):
            primo = False
        i = i+1
    return primo
            
def maior_primo(num):
    i = 1
    if (num<2):
        print("Infome um número maior ou igual a 2")
        maior = num
    else:
        while (i <= num):
            ehprimo = éPrimo(i)
            if (ehprimo == True):
                maior = i
            i = i + 1
    return maior

print(maior_primo(1))

