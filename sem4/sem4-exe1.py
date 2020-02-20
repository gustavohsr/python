num = int(input("Informe o numero: "))
i = 1
fatorial = num

while (i < num):
        fatorial = fatorial * (num - i)
        i = i+1

if (num == 0):
       print(fatorial+1)
else:
    print(fatorial)