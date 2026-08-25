Cps = []
Sprints = []
Gs = []

for i in range(3):
    nota = float(input("Insira as notas das CPS"))
    Cps.append(nota)

for i in range(2):
    nota = float(input("Insira as notas das Sprints"))
    Sprints.append(nota)

for i in range(1):
    nota = float(input("Insira a nota da Gs"))
    Gs.append(nota)

menor_cp = Cps[0]
for nota in Cps:
    if nota < menor_cp:
        menor_cp = nota


media = (( Cps[0] + Cps[1] + Cps[2] - menor_cp + Sprints[0] + Sprints[1]) / 4) * 0.4 + Gs[0] * 0.6
print(f"a menor nota de checkpoint é: {menor_cp:.1f}")
print(f"a media é de: {media:.1f}")