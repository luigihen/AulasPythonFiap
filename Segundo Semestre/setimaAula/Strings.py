palavra1 ="Boa"
palavra2 = "noite"
palavra3 = "!"
print(palavra1 + palavra2 + palavra3)
print(palavra1 + " " + palavra2 + palavra3)
print(palavra1 + " " + palavra2 + palavra3 * 3)

palavra1_lista = list(palavra1)
print(palavra1_lista)
palavra_string1 = "".join(palavra1_lista)
print(palavra_string1)

print(palavra_string1.startswith("Boa"))
print(palavra_string1.endswith("Boa"))
print("Boa" in palavra_string1)
print("Hello" in palavra_string1)

print(palavra_string1.count("o"))
print(palavra_string1.find("o"))
print(palavra_string1.find("u"))

print(palavra_string1.split(" "))

palavra_string1_nova = (palavra_string1.replace("Boa", "boa"))
print (palavra_string1.replace("Boa", "boa"))

titulo = "Checkpoint 2"
print(titulo.center)
print(titulo.center(50, "-"))
print(titulo.rjust(50, "-"))
print(titulo.ljust(50, "-"))

print("boa", end="\n" "\n")
print("noa")

