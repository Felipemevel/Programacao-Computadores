n = int(input())
div = []

while (len(div) != 2):
    n += 1
    for i in range(1, n+1):
        if n%i == 0:
            div.append(i)
    if len(div) != 2:
        div.clear()

print(n)
