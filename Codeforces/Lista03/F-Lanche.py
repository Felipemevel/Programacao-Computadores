escolha, quantidade = map(int, input().split())
     
cachorro_quente = float(4.0)
x_salada = float(4.50)
x_bacon = float(5.0)
torrada_simples = float(2.0)
refrigerante = float(1.50)
     
if (escolha == 1):
    print(f"Total: R$ {cachorro_quente * quantidade:.2f}")
elif (escolha == 2):
    print(f"Total: R$ {x_salada * quantidade:.2f}")
elif(escolha == 3):
    print(f"Total: R$ {x_bacon * quantidade:.2f}")
elif(escolha == 4):
    print(f"Total: R$ {torrada_simples * quantidade:.2f}")
elif(escolha == 5):
    print(f"Total: R$ {refrigerante * quantidade:.2f}") 