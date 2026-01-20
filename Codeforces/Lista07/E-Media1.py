qtd_n = int(input())
n = list(map(int, input().split()))

media = sum(n) / qtd_n
abaixo_media = 0
igual_acima_media = 0

for i in range(0, qtd_n):
    if n[i] < media:
        abaixo_media += 1
    else:
        igual_acima_media += 1

print(f"{media:.01f}")
print(abaixo_media)
print(igual_acima_media)
