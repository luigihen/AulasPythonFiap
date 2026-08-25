notas = [0, 0, 0, 0, 0]
soma = 0
x = 0
while x < 5:
    notas[x] = float(input(f"nota {x + 1} = ")) 
    soma = notas[x]
    x+=1

print(f'Media={(soma/len(notas)):.2f}')