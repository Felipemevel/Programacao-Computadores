def maior5(a, b, c, d, e):
    if (a >= b and a >= c and a >= d and a >= e):
        maior = a
    elif (b >= a and b >= c and b >= d and b >= e):
        maior = b
    elif (c >= a and c >= b and c >= d and c >= e):
        maior = c
    elif (d >= a and d >= b and d >= c and d >= e):
        maior = d
    else:
        maior = e
    return maior