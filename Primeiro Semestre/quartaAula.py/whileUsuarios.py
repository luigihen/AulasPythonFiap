
x1 = 0
fim = int(input("digite o numero final"))
while x1 <= fim:
    print(x1)
    x1 += 1



limite = int(input("Até que número quer contar? "))
x2 = 1 
print(f"Números ímpares até {limite}:")
while x2 <= limite:
    print(x2)
    x2 += 2 



contador = int(input("digite qual taboada voce quer"))
print("Os 10 primeiros múltiplos de 3 são:")
while contador <= 10:
    multiplo = contador * 3
    print(f"{contador}º múltiplo: {multiplo}")
    contador += 1
