N = int(input())
sequencia = []

for _ in range(N):
    sequencia.append(int(input()))

ultimo = sequencia[0]
total = 1

for i in range(1, N):
    if sequencia[i] != ultimo:
        total += 1
        ultimo = sequencia[i]

print(total)