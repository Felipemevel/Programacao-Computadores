item = int(input())
qtd = int(input())
pago = int(input())
     
total_itens = item * qtd
troco = pago - total_itens
     
print(f"A pagar: {total_itens}\nTroco  : {troco}")