n = int(input())
tempo = []

while n != 0:
    n -= 1
    c_kg = float(input())
    dias = 0
    while c_kg > 1.0:
        c_kg = c_kg / 2
        dias += 1
    tempo.append(dias)

for tempo in tempo:
    print(f"{tempo} dias")