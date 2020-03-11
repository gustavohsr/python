def retangulo(largura,altura):

    print("Criando Retangulo")
    x = 1
    while x <= altura:
        y = 1
        while y <= largura:
            #print("#",end="\t")
            print("#",end='')
            y = y + 1
        print()
        x = x + 1

largura = int(input("Informe a largura: "))
altura = int(input("Informe a altura: "))

retangulo(largura,altura)