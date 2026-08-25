distancia = float(input('insira a distania que quer viajar'))

if distancia <= 200:
    
    valor = 200 * 0.50
    print('pague: $', valor) 

else:
    valor = 200 * 0.45
    print('pague: $', valor) 