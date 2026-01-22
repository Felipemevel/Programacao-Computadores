p_al, p_gaso, r_al, r_gaso = map(float, input().split())

relacao_gaso = r_gaso / p_gaso
relacao_al = r_al / p_al

if (relacao_gaso >= relacao_al):
    print('G')
else:
    print('A')