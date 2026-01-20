def sublista_sem_menor(lista):
    menor_valor = min(lista)
    nova_lista = list(lista)
    nova_lista.remove(menor_valor)
    return nova_lista