checkpoint3 = []

print(len(checkpoint3))
#isso printa 0, ja que ate esse comando de cima a lista esta vazia
checkpoint3 = [10, 0, 1 ,2 , 4, 5, 4]
checkpoint3[5] = 7
print(checkpoint3)
print(checkpoint3[5])

soma = 0
x = 0

while x <= len(checkpoint3):
    soma = soma + checkpoint3[x]
    x += 1
print(f'Media = {(soma/len(checkpoint3)):.2f}')