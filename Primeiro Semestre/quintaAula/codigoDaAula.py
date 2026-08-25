check_3 = []
soma_atual = 0
cont = 0
quant_alunos = int(input("Insira a quantidade de alunos"))

while cont < quant_alunos:
    nota_atual = float(input('Nota ='))
    check_3.append(nota_atual) 
    soma_atual += check_3[cont]
    cont += 1


print(check_3)
check_3.sort()
print(check_3)
check_3.sort(reverse=True)
print(check_3)
print(max(check_3))
print(min(check_3))
print(f'Media = {(soma_atual/len(check_3)):.2f}')

