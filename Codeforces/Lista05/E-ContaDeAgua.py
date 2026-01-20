N = int(input())

total_conta = 7

if N > 10:
    if N <= 30:
        total_conta = total_conta + (N - 10) * 1
    else:
        total_conta = total_conta + (20 * 1)
        
        if N > 30:
            if N <= 100:
                total_conta = total_conta + (N - 30) * 2
            else:
                total_conta = total_conta + (70 * 2)
                
                if N > 100:
                    total_conta = total_conta + (N - 100) * 5

print(total_conta)