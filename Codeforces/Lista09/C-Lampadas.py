n = int(input())
comandos = map(int, input().split())

a = 0
b = 0

for cmd in comandos:
    if cmd == 1:
        a = 1 - a
    elif cmd == 2:
        a = 1 - a
        b = 1 - b

print(a)
print(b)