numero1 = float(input('insira um numero'))
numero2 = float(input('insira um outro numero'))
numero3 = float(input('insira um outro numero'))

maior = numero1

menor = numero1

if numero2 > maior:
    maior = numero2

if numero3 > maior:
    maior = numero3



if numero2 < menor:
    menor = numero2

if numero3 < menor:
    menor = numero3

print('o maior numero é:', maior, 'o menor numero é:', menor)