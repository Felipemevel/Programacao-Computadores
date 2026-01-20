teste = 1
while True:
    try:
        line = input().split()
        if not line:
            break
        n = int(line[0])
        
        if n == 0:
            break
            
        ix, iy, iu, iv = map(int, input().split())
        
        for _ in range(n - 1):
            x, y, u, v = map(int, input().split())
            ix = max(ix, x)
            iy = min(iy, y)
            iu = min(iu, u)
            iv = max(iv, v)
            
        print(f"Teste {teste}")
        
        if ix < iu and iv < iy:
            print(f"{ix} {iy} {iu} {iv}")
        else:
            print("nenhum")
            
        print()
        teste += 1
        
    except EOFError:
        break