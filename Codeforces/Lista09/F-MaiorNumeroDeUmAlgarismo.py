def grau_nove(n):
    if n == 0:
        return 0
    res = n % 9
    if res == 0:
        return 9
    return res

while True:
    try:
        linha = input().split()
        if not linha:
            break
            
        n = int(linha[0])
        m = int(linha[1])
        
        if n == 0 and m == 0:
            break
        
        g_n = grau_nove(n)
        g_m = grau_nove(m)
        
        if g_n > g_m:
            print(1)
        elif g_m > g_n:
            print(2)
        else:
            print(0)
            
    except EOFError:
        break