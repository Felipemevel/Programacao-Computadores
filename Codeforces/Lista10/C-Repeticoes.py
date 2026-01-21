contador = 1
contador_maior = 1

dna = input()
lista = list(dna)

for i in range(1, len(lista)):
    if lista[i] == lista[i - 1]:
        contador += 1
    else:
        if contador > contador_maior:
            contador_maior = contador
        contador = 1
    if contador > contador_maior:
        contador_maior = contador

print(contador_maior)
