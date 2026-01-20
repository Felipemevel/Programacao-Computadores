mensagem = input()
crib = input()

m = len(mensagem)
c = len(crib)
contagem = 0

for i in range(m - c + 1):
    valido = True
    for j in range(c):
        if mensagem[i + j] == crib[j]:
            valido = False
            break
    if valido:
        contagem += 1

print(contagem)