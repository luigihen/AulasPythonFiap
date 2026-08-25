##Nota do Checkpoint 1
##Nota do Checkpoint 2
##Nota do Checkpoint 3
##Nota da Sprint 1
##Nota da Sprint 2
## Nota da Global Solution
checkpoint = float(input("Insira a nota de 0 a 10 do primeiro Checkpoint"))
checkpoint2 = float(input("Insira a nota de 0 a 10 do segundo Checkpoint"))
checkpoint3 = float(input("Insira a nota de 0 a 10 do terceiro Checkpoint"))

sprint = float(input("Insira a nota de 0 a 10 do primeiro Sprint"))
sprint2 = float(input("Insira a nota de 0 a 10 do segundo Sprint"))

globalsolution = float(input("Insira a nota de 0 a 10 do Global Solution"))

menorcheck = checkpoint
if checkpoint2 <= checkpoint:
    menorcheck = checkpoint2

if checkpoint3 <= checkpoint:
    menorcheck = checkpoint3



media = ((checkpoint + checkpoint2 + checkpoint3 - menorcheck + sprint + sprint2 )/4) * 0.4 + globalsolution * 0.6


mediapeso = media * 0.4

print(f"A média desconsiderando os pesos é de {media:.11f}.")
print()
print(f"Já a média considerando os pesos é de {mediapeso:.1f}.")
