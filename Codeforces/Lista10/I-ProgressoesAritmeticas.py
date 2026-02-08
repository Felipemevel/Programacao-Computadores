n = int(input())

lista = list(map(int, input().split()))

def calcular_minimo_partes(n, lista):
    if n <= 2:
        return 1
    
    partes = 1
    
    diferenca_atual = lista[1] - lista[0]
    
    nova_sequencia = False
    
    for i in range(2, n):
        diff = lista[i] - lista[i-1]
        
        if nova_sequencia:
            diferenca_atual = diff
            nova_sequencia = False
        else:
            if diff != diferenca_atual:
                partes = partes + 1   
                nova_sequencia = True 
                
    return partes

resultado = calcular_minimo_partes(n, lista)
print(resultado)