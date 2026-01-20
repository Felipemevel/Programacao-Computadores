p, n = map(int, input().split())
alt = list(map(int, input().split()))
perdeu = False


for i in range(1, n):
    if (abs(alt[i] - alt[i-1]) > p):
        print("GAME OVER")
        perdeu = True
        break

if perdeu == False:
    print("YOU WIN")       