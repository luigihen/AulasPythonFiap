salario = float(input('insira seu salario:'))

if salario > 1250:
    aumento10 = (salario / 100) * 10
    final1 = salario + aumento10 
    print(final1)
elif salario <= 1250:
    aumento15 = (salario / 100) * 15
    final2 = salario + aumento15
    print(final2)
