medicoes = int(input())
qtd_batimentos = []

for i in range(0, medicoes):
    batimentos = int(input())
    qtd_batimentos.append(batimentos)

media = sum(qtd_batimentos) // len(qtd_batimentos)
media_abaixo = (90 * media)//100
media_acima = (110 * media)//100
irregular = 0

for j in range(len(qtd_batimentos)):
    if qtd_batimentos[j] < media_abaixo or qtd_batimentos[j] > media_acima:
        irregular += 1

print(media)
print(irregular)