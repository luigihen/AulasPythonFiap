velocidade = float(input('insira a velocidade'))


if velocidade > 80:
    multa = (velocidade - 80) * 5
    print('multa de $', multa)

elif velocidade < 80:
    print('suave')

else:
    print(' no limite ')


