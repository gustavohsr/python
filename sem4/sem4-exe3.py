num = int(input("Digite um número inteiro: "))
resto = 0
soma = 0
while (num != 0):
    resto = num % 10
    soma = soma + resto
    num = num // 10
print(soma)