senha = 9842
acesso = int(input())

while (acesso != senha):
    print("Senha Invalida!")
    acesso = int(input())
else:
    print("Acesso Permitido.")