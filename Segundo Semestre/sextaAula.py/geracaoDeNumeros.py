L = [1, 7, 2, 4]
maximo = L[0]

for i in L:
    if i>maximo:
        maximo = i
print(maximo)

herois = {"mulher maravilha":["laço da verdade",2017], "homem aranha":["sentido aranha",2002],"flash":["força de aceleração", 2008]}
print(herois["flash"])
herois["homem aranha"] = "voar"
print("qualquer coisa" in herois)
print('mulher maravilha' in herois)
print(herois.keys())
print(herois.values())
print(herois["super homem"][1])