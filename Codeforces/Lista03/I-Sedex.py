diametro = int(input())
altura, largura, profundidade = map(int, input().split())
     
if (diametro <= altura and diametro <= largura 
    and diametro <= profundidade):
    print("S")
else:
    print("N")