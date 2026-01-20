qtd = int(input())
n = list(map(int, input().split()))

media = sum(n)/qtd
acima_media = []
abaixo_media = []
qtd_acima = 0
qtd_abaixo = 0

for i in range(0, len(n)):
    if n[i] >= media:
        acima_media.append(n[i])
        qtd_acima += 1
    else:
        abaixo_media.append(n[i])
        qtd_abaixo += 1

print(f"{media:.01f}")
print(qtd_abaixo, *abaixo_media)
print(qtd_acima, *acima_media)